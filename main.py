from nicegui import ui

def main():
    ui.label('CineScope - Your movies in seconds')
    ui.input(placeholder='Search for a movie')
    ui.button('Search')
    
    ui.run()

main()
