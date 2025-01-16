from flask import Flask, render_template, request, redirect, url_for, session # type: ignore

app = Flask(__name__)
app.secret_key = "kunci_jawaban"

bank_soal = [
    {
        "pertanyaan": "Pulau Komodo terletak di provinsi?",
        "pilihan": ["A. Bali", 
                    "B. NTT", 
                    "C. NTB", 
                    "D. Jawa Timur"],
        "jawaban_benar": "B"
    },
    {
        "pertanyaan": "Siapa Presiden Indonesia ketiga?",
        "pilihan": ["A. B.J Habibie", 
                    "B. Jokowi", 
                    "C. Soekarno", 
                    "D. Abdurahman Wahid"],
        "jawaban_benar": "A"
    },
    {
        "pertanyaan": "Apa singkatan dari MPR?",
        "pilihan": [
            "A. Majelis Perwakilan Rakyat",
            "B. Majelis Permusyawaratan Rakyat",
            "C. Majelis Perhimpunan Rakyat",
            "D. Majelis Perserikatan Rakyat"
        ],
        "jawaban_benar": "B"
    },
    {
        "pertanyaan": "Pada tanggal berapakah Hari Lahir Pancasila diperingati?",
        "pilihan": ["A. 17 Agustus", 
                    "B. 1 Maret", 
                    "C. 1 Juni", 
                    "D. 1 Desember"],
        "jawaban_benar": "C"
    },
    {
        "pertanyaan": "Apa julukan terkenal dari negara Korea Selatan?",
        "pilihan": ["A. Negeri Tirai Bambu", 
                    "B. Negeri Ginseng", 
                    "C. Zamrud Khatulistiwa", 
                    "D. Negeri Kincir Angin"],
        "jawaban_benar": "B"
    },
    {
        "pertanyaan": "100 x 9 - 500 + 2 =...",
        "pilihan": ["A. 402", 
                    "B. 418", 
                    "C. 408", 
                    "D. 502"],
        "jawaban_benar" : "A"
    },
    {
        "pertanyaan": "Apa bahasa Inggris angka sepuluh?",
        "pilihan": ["A. Ten", 
                    "B. Tono",
                    "C. Tina", 
                    "D. Tani"],
        "jawaban_benar" : "A"
    },
    {
        "pertanyaan": "Apa yang bisa bergerak lebih cepat dari suara?",
        "pilihan": ["A. Kaki", 
                    "B. Tangan", 
                    "C. Burung", 
                    "D. Pikiran"],
        "jawaban_benar" : "D"
    },
    {
        "pertanyaan": "Apa yang bisa dipegang tetapi tidak bisa disentuh?",
        "pilihan": ["A. Janji", 
                    "B. Hatimu", 
                    "C. Tanganmu", 
                    "D. Pancar"],
        "jawaban_benar" : "A"
    },
    {
        "pertanyaan": "Pemain Sepak Bola Terbaik sepanjang masa ialah?",
        "pilihan": ["A. Shin Tae-Young", 
                    "B. Fahri", 
                    "C. Messi", 
                    "D. Ambappe"],
        "jawaban_benar" : "B"
    }
]

@app.route("/")
def halaman_utama():
    session.clear()
    return render_template("index.html")

@app.route("/kuis", methods=["GET", "POST"])
def kuis():
    if "soal_saat_ini" not in session:
        session["soal_saat_ini"] = 0
        session["skor"] = 0
    
    soal_saat_ini = session["soal_saat_ini"]

    if request.method == "POST":
        jawaban_pengguna = request.form.get("jawaban")
        jawaban_benar = bank_soal[soal_saat_ini]["jawaban_benar"]

        if jawaban_pengguna == jawaban_benar:
            session["skor"] += 1
            tanggapan = "Jawaban Anda BENAR!"
            warna = "#2ca934"
        else:
            tanggapan = f"Jawaban Anda SALAH! Jawaban yang benar adalah {jawaban_benar}."
            warna = "red"

        session["tanggapan"] = tanggapan
        session["warna"] = warna
        session["soal_saat_ini"] += 1
        return redirect(url_for("kuis"))

    if soal_saat_ini >= len(bank_soal):
        return redirect(url_for("hasil"))

    soal = bank_soal[soal_saat_ini]
    tanggapan = session.pop("tanggapan", None)
    warna = session.pop("warna", None)
    return render_template("kuis.html", soal=soal, tanggapan=tanggapan, warna=warna, nomor_soal=soal_saat_ini + 1, total_soal=len(bank_soal))

@app.route("/hasil")
def hasil():
    skor = session.get("skor", 0)
    total_soal = len(bank_soal)
    return render_template("hasil.html", skor=skor, total_soal=total_soal)

if __name__ == '__main__':
    app.run(debug=True)