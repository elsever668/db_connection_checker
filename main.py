import pymysql
import socket

def check_port(ip, port):
    """Check if a port is open on a specific IP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)  # Set timeout for the connection
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} on {ip} is open.")
            return True
        else:
            print(f"Port {port} on {ip} is closed.")
            return False

def check_connection(host, port, user, password, database):
    """Check MySQL database connectivity."""
    if not check_port(host, port):
        print("Cannot proceed with database connection. Port check failed.")
        return

    try:
        # Connect to the database
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        print("Successfully connected to the database!")
        connection.close()
    except pymysql.MySQLError as e:
        print(f"Database connection error: {e}")

# Specify connection parameters
host = "192.168.100.1"  # Server IP or hostname
port = 3306            # Database port
user = "user"              # Username
password = "password"          # Password
database = "main_db"  # Database name

# Perform the checks
check_connection(host, port, user, password, database)
