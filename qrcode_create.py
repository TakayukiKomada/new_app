import qrcode

qr = qrcode.QRCode(
    box_size=4, border=8, version=12, error_correction=qrcode.constants.ERROR_CORRECT_Q
)
