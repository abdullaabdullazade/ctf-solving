import subprocess

# Fayllar
input_file = "last_output.wav"
converted_file = "output.wav"

# 1. Səsi çevirmək (44100 Hz, mono)
subprocess.run(["ffmpeg", "-y", "-i", input_file, "-ac", "1", "-ar", "44100", converted_file])

# 2. Baud rate-ləri test et
baud_rates = [300, 600, 1200, 2400, 4800, 9600]

for baud in baud_rates:
    print(f"\n[*] Trying baud rate: {baud}")
    result = subprocess.run(["minimodem", "--rx", str(baud), "-f", converted_file],
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output = result.stdout.decode(errors="ignore")
    if "flag" in output.lower():
        print("[+] Possible Flag Found!")
        print(output)
