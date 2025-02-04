# UltraStation

## Overview

UltraStation is a Python-based utility designed to adjust system clock settings on Windows machines. It synchronizes the system time with internet time servers, ensuring accurate and reliable time management. 

## Features

- Synchronizes Windows system clock with internet time servers.
- Ensures your system time is accurate, which is crucial for time-sensitive applications.
- Runs as a background process, synchronizing time every hour.

## Requirements

- **Windows OS**: This script is intended for use on Windows operating systems.
- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **Administrative Privileges**: The script needs admin rights to adjust system time settings.

## Installation

1. Clone the repository or download the `UltraStation.py` file to your local machine.
2. Ensure you have the necessary permissions to run scripts with administrative privileges.

## Usage

1. Open a Command Prompt with administrative privileges.
2. Navigate to the directory containing `UltraStation.py`.
3. Run the script using Python:

   ```bash
   python UltraStation.py
   ```

4. The script will synchronize your system time with internet time servers every hour.

## Important Notes

- Make sure to run the script with administrative privileges, as changing system time requires admin rights.
- The script uses the `w32tm` command, which is built into Windows, to resynchronize the system time. 

## Troubleshooting

- **Permission Errors**: If you encounter permission errors, ensure that you are running the Command Prompt as an administrator.
- **Network Issues**: If synchronization fails, check your internet connection and firewall settings.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any proposed changes or improvements.

## Contact

For support or inquiries, please contact the project maintainer.