import time

input = time.time()
print(f"Seconds since January 1, 1970: \
{input:,.4f} or {input:.2e} in scientific notation")
print(time.strftime("%b %d %Y"))
