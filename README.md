# Counter-Strike 1.6 - BunnyHop
This is a pretty simple script.

# Warning
Does not work for all versions of cs 1.6.

## Tips for finding addresses
### Jump
1. Open the cheat engine

2. Scan type exact value, value type 4 bytes and value 4

3. Type +jump in console and scan for the value 5
### OnGround
1. Open the cheat engine

2. Scan type exact value, value type 4 bytes and value 1

3. type sv_gravity "3" in console then make your character jump make sure he is not on the ground then look for address 0


## Installation
```console
# Clone the repository
git clone https://github.com/6accOnThe6locc/bhop_cs16.git

# Change the working directory to bhop_cs16
cd bhop_cs16

# Install the requirements
pip install -r requirements.txt
```

## Usage
```console
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
