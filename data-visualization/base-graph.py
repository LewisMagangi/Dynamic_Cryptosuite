import matplotlib.pyplot as plt

# Data from your table
data_sizes = [1, 2, 5, 10, 20, 50]  # in MB
aes_encryption_times = [0.0, 0.00506138801574707, 0.01003265380859375, 0.025650739669799805, 0.06869387626647949, 0.15002202987670898]
aes_decryption_times = [0.005044460296630859, 0.0, 0.010578393936157227, 0.020200490951538086, 0.04541730880737305, 0.13508248329162598]
ecdh_times = [0.034940481185913086, 0.03513956069946289, 0.0697624683380127, 0.11521196365356445, 0.19506525993347168, 0.46010613441467285]
ecc_times = [0.03506326675415039, 0.04428458213806152, 0.0605621337890625, 0.11485123634338379, 0.21000361442565918, 0.5074303150177002]

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(data_sizes, aes_encryption_times, marker='o', label='AES Encryption')
plt.plot(data_sizes, aes_decryption_times, marker='o', label='AES Decryption')
plt.plot(data_sizes, ecdh_times, marker='o', label='ECDH')
plt.plot(data_sizes, ecc_times, marker='o', label='ECC')

# Adding titles and labels
plt.title('Encryption and Decryption Times vs Data Size')
plt.xlabel('Data Size (MB)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
