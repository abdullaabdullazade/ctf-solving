import base64

def apply_rot(text, shift, rotate_upper=True, rotate_lower=True):
    result = ""
    for c in text:
        if c.isupper() and rotate_upper:
            result += chr((ord(c) - 65 + shift) % 26 + 65)
        elif c.islower() and rotate_lower:
            result += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            result += c
    return result

def find_flag(encoded_b64):
    decoded = base64.b64decode(encoded_b64).decode()

    for first_rot in range(1, 26):
        first_step = apply_rot(decoded, first_rot, rotate_upper=True, rotate_lower=True)

        for second_rot in range(1, 26):
            final_step = apply_rot(first_step, second_rot, rotate_upper=False, rotate_lower=True)

            if final_step.startswith("CIT{"):
                print(f"[✅] TAPILDI! ROT1: {first_rot}, ROT2: {second_rot}")
                print("Flaq:", final_step)
                return final_step

    print("[❌] Heç bir uyğunluq tapılmadı.")
    return None

encoded = "TFJDe0gzeV9ldmlfdzMzX0FYQ0M2V19Wa1hidldINDYxTXR1YlgyOXZnYn0="

find_flag(encoded)
