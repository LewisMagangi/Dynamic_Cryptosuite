import sys

def main():
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python fastest-algo.py <elapsed_time>")
        return

    # Get the elapsed time from the command-line argument
    elapsed_time = float(sys.argv[1])

    # Print the elapsed time received
    print("Elapsed time received from ecc-time.py:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
