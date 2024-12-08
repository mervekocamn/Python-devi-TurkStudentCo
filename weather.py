class City:
    def __init__(self, name, temperature=None):
        self.name = name
        self.temperature = temperature

class Weather:
    def __init__(self):
        self.cities = {}

    def addCity(self, cityName, citytemperature):
        newCity = City(cityName, citytemperature)
        self.cities[cityName.lower()] = newCity
        print(f"{cityName} şehri eklendi, sıcaklık: {citytemperature}°C.")

    def updateWeather(self, cityName, citytemperature):
        city = self.cities.get(cityName.lower())
        if city:
            city.temperature = citytemperature
            print(f"{cityName} şehrinin sıcaklığı güncellendi: {citytemperature}°C.")
        else:
            print(f"{cityName} şehri bulunamadı.")

    def getWeather(self, cityName):
        city = self.cities.get(cityName.lower())
        if city:
            print(f"{city.name} şehri için sıcaklık: {city.temperature}°C.")
            self.tavsiye_ver(city.temperature)
        else:
            print(f"{cityName} şehri bulunamadı.")

    def tavsiye_ver(self, temperature):
        if temperature < 0:
            print("Soğuk, sıkı giyinin.")
        elif 0 <= temperature <= 15:
            print("Serin, mont almayı unutmayın.")
        else:
            print("Hava güzel, rahat giyin.")

def main():
    app = Weather()

    while True:
        print("\n1. Şehir Ekle")
        print("2. Sıcaklık Güncelle")
        print("3. Hava Durumu Sorgula")
        print("4. Çıkış")

        chose = input("Bir seçenek seçin: ")

        if chose == "1":
            cityName = input("Şehir adı girin: ")
            temperature = float(input(f"{cityName} için sıcaklık girin: "))
            app.addCity(cityName, temperature)
        elif chose == "2":
            cityName = input("Sıcaklık güncellenecek şehir adı: ")
            temperature = float(input(f"{cityName} için yeni sıcaklık: "))
            app.updateWeather(cityName, temperature)
        elif chose == "3":
            cityName = input("Hava durumunu sorgulamak istediğiniz şehir adı: ")
            app.getWeather(cityName)
        elif chose == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
