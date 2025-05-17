import asyncio
from bleak import BleakClient, BleakScanner
import get_data_pb2


class BLEDevice:
    def __init__(self, device_name="ROOM_27", auth_token="I382CdOWG1Tr014J"):
        self.device_name = device_name
        self.auth_token = auth_token
        self.client = None

        # UUID характеристик
        self.CHAR_WRITE_UUID = "0000ff02-0000-1000-8000-00805f9b34fb"
        self.CHAR_STATE_UUID = "0000ff01-0000-1000-8000-00805f9b34fb"

    async def connect(self):
        """Подключение к BLE-устройству"""
        print(f"Поиск BLE-устройства '{self.device_name}'...")
        devices = await BleakScanner.discover()
        device = next((d for d in devices if d.name == self.device_name), None)

        if not device:
            raise ConnectionError("Устройство не найдено")

        self.client = BleakClient(device.address)
        await self.client.connect()
        print("Подключено к устройству.")

        # Авторизация
        auth_msg = get_data_pb2.IdentifyRequest(Token=self.auth_token)
        await self.client.write_gatt_char(
            self.CHAR_WRITE_UUID,
            auth_msg.SerializeToString(),
            response=True
        )
        return True

    async def disconnect(self):
        """Отключение от устройства"""
        if self.client and self.client.is_connected:
            await self.client.disconnect()
            print("Отключено от устройства")

    async def _send_state_command(self, state):
        """Общий метод для отправки команд"""
        if not self.client or not self.client.is_connected:
            raise ConnectionError("Не подключено к устройству")

        set_state = get_data_pb2.SetState(state=state)
        await self.client.write_gatt_char(
            self.CHAR_STATE_UUID,
            set_state.SerializeToString(),
            response=True
        )

    async def set_light_on(self):
        """Включить свет"""
        await self._send_state_command(get_data_pb2.States.LightOn)
        print("Свет включен")

    async def set_light_off(self):
        """Выключить свет"""
        await self._send_state_command(get_data_pb2.States.LightOff)
        print("Свет выключен")

    async def set_door_open(self):
        """Открыть дверь"""
        await self._send_state_command(get_data_pb2.States.DoorLockOpen)
        print("Дверь открыта")

    async def set_door_close(self):
        """Закрыть дверь"""
        await self._send_state_command(get_data_pb2.States.DoorLockClose)
        print("Дверь закрыта")


# Пример использования
async def main():
    device = BLEDevice()
    try:
        await device.connect()

        # Управление устройством
        await device.set_light_on()
        await asyncio.sleep(1)
        await device.set_door_open()
        await asyncio.sleep(3)
        await device.set_door_close()
        await asyncio.sleep(1)
        await device.set_light_off()

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        await device.disconnect()


if __name__ == "__main__":
    asyncio.run(main())