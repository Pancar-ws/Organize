from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "kunci_rahasia_quiz"

# Data soal dan jawaban
bank_soal = [
    {
        "pertanyaan": "Pulau Komodo terletak di provinsi?",
        "pilihan": ["A. Bali", "B. NTT", "C. NTB", "D. Jawa Timur"],
        "jawaban_benar": "B"
    },
    {
        "pertanyaan": "Siapa Presiden Indonesia ketiga?",
        "pilihan": ["A. B.J Habibie", "B. Jokowi", "C. Soekarno", "D. Abdurahman Wahid"],
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
        "pilihan": ["A. 17 Agustus", "B. 1 Maret", "C. 1 Juni", "D. 1 Desember"],
        "jawaban_benar": "C"
    },
    {
        "pertanyaan": "Apa julukan terkenal dari negara Korea Selatan?",
        "pilihan": ["A. Negeri Tirai Bambu", "B. Negeri Ginseng", "C. Zamrud Khatulistiwa", "D. Negeri Kincir Angin"],
        "jawaban_benar": "B"
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
            umpan_balik = "Jawaban Anda BENAR!"
            warna = 
        else:
            umpan_balik = f"Jawaban Anda SALAH! Jawaban yang benar adalah {jawaban_benar}."
            warna =

        session["umpan_balik"] = umpan_balik
        session["warna"] = warna
        session["soal_saat_ini"] += 1
        return redirect(url_for("kuis"))

    if soal_saat_ini >= len(bank_soal):
        return redirect(url_for("hasil"))

    soal = bank_soal[soal_saat_ini]
    umpan_balik = session.pop("umpan_balik", None)
    warna = session.pop("umpan_balik", None)
    return render_template("kuis.html", soal=soal, umpan_balik=umpan_balik, nomor_soal=soal_saat_ini + 1, total_soal=len(bank_soal))

@app.route("/hasil")
def hasil():
    skor = session.get("skor", 0)
    total_soal = len(bank_soal)
    return render_template("hasil.html", skor=skor, total_soal=total_soal)


