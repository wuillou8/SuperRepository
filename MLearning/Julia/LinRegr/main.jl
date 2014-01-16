data = readcsv("Data/gasoline.csv")

x = data[:, 2:4]
y = data[:, 6]


# Call linreg
coefs = linreg(x, y)

