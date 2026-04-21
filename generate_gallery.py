import os

# Map folder paths to display names and boarding card filenames
sections = [
    {
        'heading': '## 🍁 North America',
        'destinations': [
            {'folder': 'photography/north-america/ontario', 'title': 'Ontario', 'boarding_card': None},
            {'folder': 'photography/north-america/kelowna', 'title': 'Kelowna', 'boarding_card': None},
            {'folder': 'photography/north-america/florida', 'title': 'Florida', 'boarding_card': 'photography/boarding-cards/florida.png'},
            {'folder': 'photography/north-america/dominican-republic', 'title': 'Punta Cana', 'boarding_card': 'photography/boarding-cards/dominican-republic.png'},
        ]
    },
    {
        'heading': '## 🇮🇪 Ireland',
        'destinations': [
            {'folder': 'photography/ireland', 'title': 'Dublin & Ireland', 'boarding_card': 'photography/boarding-cards/dublin.png'},
        ]
    },
    {
        'heading': '## 🌍 Europe',
        'destinations': [
            {'folder': 'photography/europe/netherlands', 'title': 'Amsterdam', 'boarding_card': 'photography/boarding-cards/netherlands.png'},
            {'folder': 'photography/europe/denmark', 'title': 'Copenhagen', 'boarding_card': 'photography/boarding-cards/denmark.png'},
            {'folder': 'photography/europe/sweden', 'title': 'Stockholm', 'boarding_card': 'photography/boarding-cards/sweden.png'},
            {'folder': 'photography/europe/uk', 'title': 'Edinburgh & Glasgow', 'boarding_card': 'photography/boarding-cards/uk.png'},
            {'folder': 'photography/europe/germany', 'title': 'Germany', 'boarding_card': 'photography/boarding-cards/germany.png'},
            {'folder': 'photography/europe/spain', 'title': 'Mallorca & Alicante', 'boarding_card': 'photography/boarding-cards/spain.png'},
            {'folder': 'photography/europe/france', 'title': 'Nice & Paris', 'boarding_card': 'photography/boarding-cards/france.png'},
            {'folder': 'photography/europe/portugal', 'title': 'Faro & Lisbon', 'boarding_card': 'photography/boarding-cards/portugal.png'},
        ]
    },
    {
        'heading': '## 🇮🇹 Italy Road Trip',
        'destinations': [
            {'folder': 'photography/italy', 'title': 'Lake Como · Bormio · Dolomites · Venice · Parma', 'boarding_card': 'photography/boarding-cards/italy.png'},
        ]
    },
    {
        'heading': '## 🇲🇦 Morocco',
        'destinations': [
            {'folder': 'photography/morocco', 'title': 'Marrakesh', 'boarding_card': 'photography/boarding-cards/morocco.png'},
        ]
    },
]

output_lines = []

# Frontmatter
output_lines.append('---')
output_lines.append('title: "Photography"')
output_lines.append('page-layout: full')
output_lines.append('---')
output_lines.append('')

# Intro
output_lines.append('::: {.photography-intro}')
output_lines.append('Living between Dublin and Canada for the past few years meant one thing —')
output_lines.append('a lot of airports, a lot of new places, and always a camera nearby. What')
output_lines.append('started as documenting trips turned into a genuine passion. These are some')
output_lines.append('of my favourite shots from the places I have been lucky enough to explore.')
output_lines.append(':::')
output_lines.append('')
output_lines.append('---')
output_lines.append('')

for section in sections:
    output_lines.append(section['heading'])
    output_lines.append('')

    for dest in section['destinations']:
        # Boarding card
        if dest['boarding_card']:
            output_lines.append('```{=html}')
            output_lines.append('<div class="boarding-card-container">')
            output_lines.append(f'  <img src="{dest["boarding_card"]}" alt="Boarding card for {dest["title"]}">')
            output_lines.append('</div>')
            output_lines.append('```')
            output_lines.append('')

        # Section title
        output_lines.append(f'### {dest["title"]}')
        output_lines.append('')

        # Get image files
        folder = dest['folder']
        if not os.path.exists(folder):
            output_lines.append(f'<!-- Folder not found: {folder} -->')
            output_lines.append('')
            continue

        images = sorted([
            f for f in os.listdir(folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ])

        if not images:
            output_lines.append(f'<!-- No images found in: {folder} -->')
            output_lines.append('')
            continue

        # Generate HTML grid
        output_lines.append('```{=html}')
        output_lines.append('<div class="photo-grid">')
        for img in images:
            output_lines.append(f'  <img src="{folder}/{img}" alt="{dest["title"]} photo">')
        output_lines.append('</div>')
        output_lines.append('```')
        output_lines.append('')

    output_lines.append('---')
    output_lines.append('')

# Write output
with open('photography.qmd', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("photography.qmd generated successfully!")