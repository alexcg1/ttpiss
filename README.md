# Take-the-piss

This is a simple program that takes a string of text with profanity and returns a string with characters in those words replaced by emoji

## Example

We'll use some words that my great-granny would be offended by to demonstrate:

- **Input:** `Dang it all to heck`
- **Output:** `💀💀💀💀 it all to 🤯🤯🤯🤯`

If we take [George Carlin's "Filthy Words"](https://katherinephelps.com/wp-content/uploads/2013/05/filthy-words-transcript.pdf) as an input text stream we get:

> The original seven words were, ☢️☢️☢️☢️, 💀💀💀💀, 🚫🚫🚫🚫, 💀💀💀💀, 💀💀💀💀sucker, 🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯, and 💀💀💀💀. Those are the ones that will curve your spine, grow hair on your hands and (laughter) maybe, even bring us, God help us, peace without honor (laughter) um, and a bourbon. (laughter) And now the first thing that we noticed was that word 💀💀💀💀 was really repeated in there because the word ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️ is a compound word and it's another form of the word ☢️☢️☢️☢️. (laughter) You want to be a purist it doesn't really -- it can't be on the list of basic words.

## Usage

`ttpiss` will output directly to the terminal, for you to redirect as you wish.

- **From string:** `ttpiss "feck you"`
- **From stdin:** `cat words_not_for_granny.txt | ttpiss`

## Configuration

- TODO: Config is stored in your XDG config directory, generally `$HOME/.config/ttpiss/config.yml`

## Why is it called Take-the-piss?

"Piss" is a bad word. This program takes it out. Hence "take the piss"
