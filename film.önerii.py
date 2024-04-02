import random

# Kullanıcı profillerini saklamak için sözlük
user_profiles = {}

# Film veritabanı
films = {
    "Aksiyon": ["Matrix", "Gladyatör", "Yıldız Savaşları", "Başlangıç"],
    "Drama": ["Yeşil Yol", "Titanic", "Schindler'in Listesi", "Forrest Gump"],
    "Komedi": ["Süperstar", "Süperbad", "Monty Python ve Kutsal Kase", "Ayı Paddington"],
    "Bilim Kurgu": ["Geleceğe Dönüş", "Yıldızlararası", "Dünya Savaşı Z", "Yerçekimi"]
}

def get_user_profile():
    """Kullanıcı profili oluşturur veya mevcut bir profili döndürür."""
    user_name = input("Adınızı girin: ")
    if user_name in user_profiles:
        print(f"Hoş geldiniz, {user_name}!")
        return user_profiles[user_name]
    else:
        print("Yeni kullanıcı profili oluşturuluyor.")
        user_profiles[user_name] = {"izlenen_filmler": [], "begendiği_türler": []}
        return user_profiles[user_name]

def get_random_movie(genre):
    """Belirli bir türde rastgele bir film döndürür."""
    return random.choice(films[genre])

if __name__ == "__main__":
    user_profile = get_user_profile()

    print("Lütfen aşağıdaki türlerden birini seçin:")
    for genre in films.keys():
        print(genre)

    selected_genre = input("Tür seçin: ").capitalize()

    if selected_genre in films:
        recommended_movie = get_random_movie(selected_genre)
        print("Önerilen film:", recommended_movie)
        user_profile["izlenen_filmler"].append(recommended_movie)
        user_profile["begendiği_türler"].append(selected_genre)
        print("Profiliniz güncellendi:", user_profile)
    else:
        print("Geçersiz tür seçimi. Lütfen listeden bir tür seçin.")
