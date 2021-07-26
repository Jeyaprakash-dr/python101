# Weather project
uv_index = 12
precipitation = 75
temperature = 50
is_cloudy = True

if uv_index > 10:
    print("Bring sunscreen")

if precipitation > 50 and temperature <=32:
    print("Its likely to snow")
elif precipitation > 50 and temperature >=33:
    print("Its likely to rain")
else:
    print ("Its not likely to snow")

print("Finished")