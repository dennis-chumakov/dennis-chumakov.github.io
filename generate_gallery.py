import os

sections = [
    {
        'heading': '## 🍁 North America',
        'destinations': [
            {'folder': 'photography/north-america/ontario', 'title': 'Ontario', 'subtitle': 'Canada', 'boarding_card': None},
            {'folder': 'photography/north-america/kelowna', 'title': 'Kelowna', 'subtitle': 'British Columbia · Canada', 'boarding_card': None},
            {'folder': 'photography/north-america/florida', 'title': 'Florida', 'subtitle': 'United States', 'boarding_card': 'photography/boarding-cards/florida.png'},
            {'folder': 'photography/north-america/dominican-republic', 'title': 'Punta Cana', 'subtitle': 'Dominican Republic', 'boarding_card': 'photography/boarding-cards/dominican-republic.png'},
        ]
    },
    {
        'heading': '## 🇮🇪 Ireland',
        'destinations': [
            {'folder': 'photography/ireland', 'title': '', 'subtitle': 'Home Base · 2023-2025', 'boarding_card': 'photography/boarding-cards/dublin.png'},
        ]
    },
    {
        'heading': '## 🌍 Europe',
        'destinations': [
            {'folder': 'photography/europe/netherlands', 'title': 'Amsterdam', 'subtitle': 'Netherlands', 'boarding_card': 'photography/boarding-cards/netherlands.png'},
            {'folder': 'photography/europe/denmark', 'title': 'Copenhagen', 'subtitle': 'Denmark', 'boarding_card': 'photography/boarding-cards/denmark.png'},
            {'folder': 'photography/europe/sweden', 'title': 'Stockholm', 'subtitle': 'Sweden', 'boarding_card': 'photography/boarding-cards/sweden.png'},
            {'folder': 'photography/europe/uk', 'title': 'Edinburgh & Glasgow', 'subtitle': 'United Kingdom', 'boarding_card': 'photography/boarding-cards/uk.png'},
            {'folder': 'photography/europe/germany', 'title': 'Germany', 'subtitle': 'Deutschland', 'boarding_card': 'photography/boarding-cards/germany.png'},
            {'folder': 'photography/europe/spain', 'title': 'Mallorca & Alicante', 'subtitle': 'Spain', 'boarding_card': 'photography/boarding-cards/spain.png'},
            {'folder': 'photography/europe/france', 'title': 'Nice & Paris', 'subtitle': 'France', 'boarding_card': 'photography/boarding-cards/france.png'},
            {'folder': 'photography/europe/portugal', 'title': 'Faro & Lisbon', 'subtitle': 'Portugal', 'boarding_card': 'photography/boarding-cards/portugal.png'},
        ]
    },
    {
        'heading': '## 🇮🇹 Italy Road Trip',
        'destinations': [
            {'folder': 'photography/italy', 'title': 'Lake Como · Bormio · Dolomites · Venice · Parma', 'subtitle': 'Italy · Summer 2024', 'boarding_card': 'photography/boarding-cards/italy.png'},
        ]
    },
    {
        'heading': '## 🇲🇦 Morocco',
        'destinations': [
            {'folder': 'photography/morocco', 'title': 'Marrakesh', 'subtitle': 'Morocco', 'boarding_card': 'photography/boarding-cards/morocco.png'},
        ]
    },
]

output_lines = []

output_lines.append('---')
output_lines.append('title: "Photography"')
output_lines.append('page-layout: full')
output_lines.append('---')
output_lines.append('')
output_lines.append('::: {.photography-intro}')
output_lines.append('Living between Dublin and Canada for the past few years meant one thing.')
output_lines.append('A lot of airports, a lot of new places, and always snapping photos. What')
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
        # Destination header div
        output_lines.append('```{=html}')
        output_lines.append('<div class="destination-header">')
        if dest['title']:
            output_lines.append(f'  <h3 class="destination-title">{dest["title"]}</h3>')
        if dest['subtitle']:
            output_lines.append(f'  <p class="destination-subtitle">{dest["subtitle"]}</p>')
        if dest['boarding_card']:
            output_lines.append(f'  <div class="boarding-card-container">')
            output_lines.append(f'    <img src="{dest["boarding_card"]}" alt="Boarding card for {dest["title"]}">')
            output_lines.append(f'  </div>')
        output_lines.append('</div>')
        output_lines.append('```')
        output_lines.append('')

        # Photo grid
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

        output_lines.append('```{=html}')
        output_lines.append('<div class="photo-grid">')
        for img in images:
            output_lines.append(f'  <img src="{folder}/{img}" alt="{dest["title"]} photo">')
        output_lines.append('</div>')
        output_lines.append('```')
        output_lines.append('')

    output_lines.append('---')
    output_lines.append('')

with open('photography.qmd', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("photography.qmd generated successfully!")