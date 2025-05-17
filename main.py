import socket
import get_data_pb2
import time


class Device():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_msg = 0
        self.socket_device.connect((host, port))
        self.set_state = 0
        self.client_msg = get_data_pb2.ClientMessage()

    def set_light_on(self):
        set_state = get_data_pb2.SetState()
        set_state.state = get_data_pb2.States.LightOn
        self.client_msg.set_state.CopyFrom(set_state)
        print("\nSending SetState (LightOn):")
        print(self.client_msg)
        self.socket_device.sendall(self.client_msg.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)
            print("\nOperation status:",
                  "OK" if response.status == get_data_pb2.Statuses.Ok else "Error")

    def set_light_off(self):
        set_state = get_data_pb2.SetState()
        set_state.state = get_data_pb2.States.LightOff
        self.client_msg.set_state.CopyFrom(set_state)
        print("\nSending SetState (LightOff):")
        print(self.client_msg)
        print(self.client_msg.SerializeToString())
        self.socket_device.sendall(self.client_msg.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)
            print("\nOperation status:",
                  "OK" if response.status == get_data_pb2.Statuses.Ok else "Error")

    def get_temp(self):
        self.client_msg.get_state.CopyFrom(get_data_pb2.GetState())
        print("\nSending GetState request:")
        print(self.client_msg)
        self.socket_device.sendall(self.client_msg.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)
            print(f"Temperature: {response.state.temperature}°C")


    def get_humidity(self):
        self.client_msg.get_state.CopyFrom(get_data_pb2.GetState())
        print("\nSending GetState request:")
        print(self.client_msg)
        self.socket_device.sendall(self.client_msg.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)
            print(f"Humidity: {response.state.humidity}%")
            return response.state.humidity

    def get_door(self):
        self.client_msg.get_state.CopyFrom(get_data_pb2.GetState())
        print("\nSending GetState request:")
        print(self.client_msg)
        self.socket_device.sendall(self.client_msg.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)
            print(f"Light: {'On' if response.state.light_on == get_data_pb2.LightStates.On else 'Off'}")
            return response.state.temperature

    def get_light(self):
        self.client_msg.get_state.CopyFrom(get_data_pb2.GetState())
        print("\nSending GetState request:")
        print(self.client_msg)
        self.socket_device.sendall(self.client_msg.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)
            print(f"Humidity: {response.state.humidity}%")
            return response.state.light_on


    def set_open(self):
        set_state = get_data_pb2.SetState()
        set_state.state = get_data_pb2.States.DoorLockOpen
        self.client_msg.set_state.CopyFrom(set_state)
        self.socket_device.sendall(self.client_msg.SerializeToString())

    def set_close(self):
        set_state = get_data_pb2.SetState()
        set_state.state = get_data_pb2.States.DoorLockClose
        self.client_msg.set_state.CopyFrom(set_state)
        self.socket_device.sendall(self.client_msg.SerializeToString())

    def get_info(self):
        request = get_data_pb2.ClientMessage()
        request.get_info.CopyFrom(get_data_pb2.GetInfo())

        # Отправляем запрос
        self.socket_device.sendall(request.SerializeToString())

        # Получаем ответ
        response_data = self.socket_device.recv(1024)
        if response_data:
            response = get_data_pb2.ControllerResponse()
            response.ParseFromString(response_data)

            # Проверяем тип ответа
            if response.HasField('info'):
                print(f"Device Info:")
                print(f"IP: {response.info.ip}")
                print(f"MAC: {response.info.mac}")
                print(f"BLE Name: {response.info.ble_name}")
                print(f"token: {response.info.token}")
                return response.status

        return None

def main():
    host = "192.168.1.100"
    port = 7000
    device = Device(host, port)
    device.set_close()

if __name__ == "__main__":
    main()