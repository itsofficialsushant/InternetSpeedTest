import speedtest

test = speedtest.Speedtest()
download = test.download() / 1_000_000  # Convert from bits to Mbps
upload = test.upload() / 1_000_000  # Convert from bits to Mbps

print(f"Download speed: {download:.2f} Mbps")
print(f"Upload speed: {upload:.2f} Mbps")
