#!/usr/bin/env python3
"""
Midi Quest 13 Instrument Catalog Parser
Parses the user-provided 1,046 instrument links, extracts manufacturer and model,
and groups them into organized batches for OmniPatch profile generation.
"""

import re
import json
import os

PROMPT_TEXT_FILE = os.path.join(os.path.dirname(__file__), 'raw_mq_links.txt')
OUTPUT_CATALOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources', 'midiquest_catalog.json')

def parse_catalog(text):
    pattern = r'\[(.*?)\]\((https://squest.com/Products/MidiQuest13/Instruments/(.*?)/index.html)\)'
    matches = re.findall(pattern, text)
    
    catalog = []
    by_mfg = {}
    
    # Known manufacturer prefixes in MidiQuest URLs
    mfg_prefixes = [
        ('1010music', '1010music'),
        ('360Systems', '360 Systems'),
        ('Access', 'Access Music'),
        ('AkaiPro', 'Akai Professional'),
        ('Akai', 'Akai Professional'),
        ('Alesis', 'Alesis'),
        ('AlternateMode', 'Alternate Mode'),
        ('ART', 'ART (Applied Research and Technology)'),
        ('ASM', 'Ashun Sound Machines (ASM)'),
        ('Audiothingies', 'Audiothingies'),
        ('Axxess', 'Axxess Unlimited'),
        ('Behringer', 'Behringer'),
        ('BCM', 'BCM'),
        ('Casio', 'Casio Computer Co.'),
        ('Cheetah', 'Cheetah Marketing'),
        ('Clavia', 'Clavia Nord'),
        ('CreativeLabs', 'Creative Labs'),
        ('Crumar', 'Crumar'),
        ('DaveSmith', 'Sequential / Dave Smith Instruments'),
        ('DigitalMusic', 'Digital Music Corp'),
        ('DigiTech', 'DigiTech'),
        ('Doepfer', 'Doepfer'),
        ('Dreadbox', 'Dreadbox'),
        ('Dynacord', 'Dynacord'),
        ('E-MU', 'E-MU Systems'),
        ('EncoreElectronics', 'Encore Electronics'),
        ('Ensoniq', 'Ensoniq'),
        ('Europa', 'Europa'),
        ('Eventide', 'Eventide'),
        ('Evolution', 'Evolution'),
        ('Fender', 'Fender'),
        ('Futuresonus', 'Futuresonus'),
        ('GliGli', 'GliGli / Sequential'),
        ('Hammond', 'Hammond'),
        ('Hohner', 'Hohner'),
        ('JLCooper', 'JLCooper Electronics'),
        ('JohnsonAmp', 'Johnson Amplification'),
        ('JoMoX', 'JoMoX'),
        ('Kawai', 'Kawai'),
        ('Kenton', 'Kenton Electronics'),
        ('Kiwitechnics', 'KiwiTechnics'),
        ('KMX', 'KMX'),
        ('Korg', 'Korg'),
        ('Kurzweil', 'Kurzweil'),
        ('Lexicon', 'Lexicon'),
        ('Line6', 'Line 6'),
        ('Lintronics', 'Lintronics'),
        ('M-Audio', 'M-Audio'),
        ('MarionSystems', 'Marion Systems'),
        ('Marshall', 'Marshall Amplification'),
        ('Meeblip', 'Meeblip'),
        ('Meris', 'Meris'),
        ('MFB', 'MFB'),
        ('Micron-Tascam', 'Tascam'),
        ('MIDISolutions', 'MIDI Solutions'),
        ('Modal', 'Modal Electronics'),
        ('Moog', 'Moog Music'),
        ('MOTU', 'MOTU'),
        ('Norand', 'Norand'),
        ('Novation', 'Novation'),
        ('Oberheim', 'Oberheim'),
        ('OctavePlateau', 'Octave-Plateau'),
        ('Organix', 'Organix'),
        ('OTOMachines', 'OTO Machines'),
        ('Peavey', 'Peavey'),
        ('Pioneer', 'Pioneer DJ'),
        ('Preenfm', 'PreenFM'),
        ('Quasimidi', 'Quasimidi'),
        ('Rane', 'Rane'),
        ('RedSound', 'Red Sound Systems'),
        ('Rhodes', 'Rhodes'),
        ('RiverCreative', 'River Creative'),
        ('RogerLinnDesign', 'Roger Linn Design'),
        ('RolandBOSS', 'BOSS / Roland'),
        ('RolandEdirol', 'Edirol / Roland'),
        ('Roland', 'Roland Corporation'),
        ('Sequential', 'Sequential Circuits'),
        ('SeriesCircuits', 'Series Circuits'),
        ('Siel', 'Siel'),
        ('Sony', 'Sony'),
        ('Soulsby', 'Soulsby Synthesizers'),
        ('SSL', 'Oxford Synthesiser Company (OSCar)'),
        ('StudioElectronics', 'Studio Electronics'),
        ('Studiologic', 'Studiologic'),
        ('Symetrix', 'Symetrix'),
        ('TastyChips', 'Tasty Chips Electronics'),
        ('TaunTek', 'TaunTek'),
        ('TCElectronic', 'TC Electronic'),
        ('TC-Helicon', 'TC-Helicon'),
        ('TECH21', 'Tech 21'),
        ('Tubbutec', 'Tubbutec'),
        ('TurtleBeach', 'Turtle Beach'),
        ('Untergeek', 'Untergeek'),
        ('Vecoven', 'Vecoven'),
        ('VintageRevolution', 'Vintage Revolution'),
        ('Voce', 'Voce'),
        ('Waldorf', 'Waldorf Music'),
        ('Yamaha', 'Yamaha Corporation'),
        ('ZOOM', 'Zoom Corporation')
    ]
    
    for name, url, path_id in matches:
        mfg = 'Unknown'
        model_part = path_id
        for prefix, mfg_name in mfg_prefixes:
            if path_id.startswith(prefix):
                mfg = mfg_name
                model_part = path_id[len(prefix):]
                break
                
        entry = {
            'display_name': name,
            'url': url,
            'path_id': path_id,
            'manufacturer': mfg,
            'model_id': model_part
        }
        catalog.append(entry)
        by_mfg.setdefault(mfg, []).append(entry)
        
    return catalog, by_mfg

if __name__ == '__main__':
    # Test with sample
    print("Catalog parser ready.")
