# First: De-Camouflage "FlagHere.txt" from "bernie.jpg" with empty passphrase
# Then:
bxl_str = "\28x\32x\38x\28x\32x\38x\28x\32x\38x\28x\32x\38xE\28x\32x\38x\28x\32x\38xZ\28x\32x\38x-\28x\32x\38xC\28x\32x\38x\28x\32x\38xT\28x\32x\38xF\28x\32x\38x{N\28x\32x\38xO\28x\32x\38xW\28x\32x\38x_\28x\32x\38x\28x\32x\38xY\28x\32x\38x\28x\32x\38xO\28x\32x\38xU_\28x\32x\38xS\28x\32x\38x\28x\32x\38x\28x\32x\38x\28x\32x\38xE\28x\32x\38x\28x\32x\38xE\28x\32x\38x_\28x\32x\38xM\28x\32x\38xE\28x\32x\38x\28x\32x\38x_\28x\32x\38xN\28x\32x\38xI\28x\32x\38x\28x\32x\38xC\28x\32x\38xE\28x\32x\38x}\28x\32x\38x\28x\32x\38x\28x\32x\38x\28x\32x\38x\28x\32x\38x\28x\32x\38x"
res = ''.join(char if char.isprintable() else ' ' for char in bxl_str).replace(" 8x", "").replace("x", "").replace(" ", "")
print(res)
