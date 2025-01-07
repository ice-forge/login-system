# Login System  

## Overview
A secure and lightweight login system with a modular design for easy customization and expansion.  

## Features  
- **Functional Login System**  
  - User registration, email verification, forgot password, and password reset functionalities.  
- **Homepage**  
  - Accessible post-login with a logout option.  
- **Secure Data Handling**  
  - User data stored locally in a `.json` file.  
  - Environment variables stored in a `.env` file for:  
    - Flask secret key.  
    - Application configurations.  
    - SMTP server details.  
- **Email Integration**  
  - Configured with an SMTP server for email authentication and password resetting.  
- **Modular Design**  
  - Easy to expand and add new features.  

## Technologies Used  
- Flask  
- Python  
- HTML  
- JavaScript  
- CSS  

## Setup

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ice-forge/login-system.git
    ```
2. Create a Virtual Environment:
    ```bash
    python -m venv venv
    ```
    
3. Activate the Virtual Environment:
    ```bash
    venv/scripts/activate

4. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the local configuration in the `.env` file.

## Usage
Run the application:
```bash
python run.py
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
