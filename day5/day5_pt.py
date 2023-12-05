# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 5   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something
#--------------------------------------------------------------
# Q: What do you give a Christmas tree with bad breath?
# A: OrnaMINTS

locations = []
# Read the input data
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()

    # Working flags and lists
    seeds = []
    reading_stos = False
    stos = []
    reading_stof = False
    stof = []
    reading_ftow = False
    ftow = []
    reading_wtol = False
    wtol = []
    reading_ltot = False
    ltot = []
    reading_ttoh = False
    ttoh = []
    reading_htol = False
    htol = []

    # Read dem datas
    for line in data:
        line = line.strip()
        # Ignore blank lines cause who cares
        if len(line) == 0: continue
        # Fetch the seed types
        if 'seeds' in line:
            seeds = line.split(':')[1].split()
        elif 'seed-to-soil map' in line:
            reading_stos = True
            reading_stof = False
            reading_ftow = False
            reading_wtol = False
            reading_ltot = False
            reading_ttoh = False
            reading_htol = False
            continue
        elif 'soil-to-fertilizer map' in line:
            reading_stof = True
            reading_stos = False
            reading_ftow = False
            reading_wtol = False
            reading_ltot = False
            reading_ttoh = False
            reading_htol = False
            continue
        elif 'fertilizer-to-water map' in line:
            reading_ftow = True
            reading_stos = False
            reading_stof = False
            reading_wtol = False
            reading_ltot = False
            reading_ttoh = False
            reading_htol = False
            continue
        elif 'water-to-light map' in line:
            reading_wtol = True
            reading_stos = False
            reading_stof = False
            reading_ftow = False
            reading_ltot = False
            reading_ttoh = False
            reading_htol = False
            continue
        elif 'light-to-temperature map' in line:
            reading_ltot = True
            reading_stos = False
            reading_stof = False
            reading_ftow = False
            reading_wtol = False
            reading_ttoh = False
            reading_htol = False
            continue
        elif 'temperature-to-humidity map' in line:
            reading_ttoh = True
            reading_stos = False
            reading_stof = False
            reading_ftow = False
            reading_wtol = False
            reading_ltot = False
            reading_htol = False
            continue
        elif 'humidity-to-location map' in line:
            reading_htol = True
            reading_stos = False
            reading_stof = False
            reading_ftow = False
            reading_wtol = False
            reading_ltot = False
            reading_ttoh = False
            continue

        if reading_stos:
            stos.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })
        elif reading_stof:
            stof.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })
        elif reading_ftow:
            ftow.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })
        elif reading_wtol:
            wtol.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })
        elif reading_ltot:
            ltot.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })
        elif reading_ttoh:
            ttoh.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })
        elif reading_htol:
            htol.append({'dest': int(line.split()[0]), 'source': int(line.split()[1]), 'length': int(line.split()[2]) })

    # Map the seed to each destination
    seed_map = {}
    for seed in seeds:
        seed = int(seed)
        print(f'Processing seed {seed}...')

        # Build a range for seed to soil
        soil_val = seed
        soil_found = False
        for record in stos:
            if soil_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            # Check if we're in range and compute deviations
            if soil_val >= record['source'] and soil_val <= record['source'] + record['length']:
                deviations = soil_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                soil_val = record['dest'] + deviations
                soil_found = True
            # We're not in range so we take whatever we came in as
            else:
                soil_val = seed
        # Build a range for soil to fertilizer
        fert_val = soil_val
        fert_found = False
        for record in stof:
            if fert_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            if fert_val >= record['source'] and fert_val <= record['source'] + record['length']:
                deviations = fert_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                fert_val = record['dest'] + deviations
                fert_found = True
            # We're not in range so we take whatever we came in as
            else:
                fert_val = soil_val
        # Build a range for fertilizer to water
        water_val = fert_val
        water_found = False
        for record in ftow:
            if water_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            if water_val >= record['source'] and water_val <= record['source'] + record['length']:
                deviations = water_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                water_val = record['dest'] + deviations
                water_found = True
            # We're not in range so we take whatever we came in as
            else:
                water_val = fert_val
        # Build a range for water to light
        light_val = water_val
        light_found = False
        for record in wtol:
            if light_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            if light_val >= record['source'] and light_val <= record['source'] + record['length']:
                deviations = light_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                light_val = record['dest'] + deviations
                light_found = True
            # We're not in range so we take whatever we came in as
            else:
                light_val = water_val
        # Build a range for light to temperature
        temp_val = light_val
        temp_found = False
        for record in ltot:
            if temp_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            if temp_val >= record['source'] and temp_val <= record['source'] + record['length']:
                deviations = temp_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                temp_val = record['dest'] + deviations
                temp_found = True
            # We're not in range so we take whatever we came in as
            else:
                temp_val = light_val
        # Build a range for temperature to humidity
        humidity_val = temp_val
        humidity_found = False
        for record in ttoh:
            if humidity_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            if humidity_val >= record['source'] and humidity_val <= record['source'] + record['length']:
                deviations = humidity_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                humidity_val = record['dest'] + deviations
                humidity_found = True
            # We're not in range so we take whatever we came in as
            else:
                humidity_val = temp_val
        # Build a range for humidity to location
        location_val = humidity_val
        location_found = False
        for record in htol:
            if location_found:
                break
            # Determine if we're in the source range and how far
            deviations = 0
            in_source = False
            if location_val >= record['source'] and location_val <= record['source'] + record['length']:
                deviations = location_val - record['source']
                in_source = True
            # If we're in range, compute our destination
            if in_source:
                location_val = record['dest'] + deviations
                location_found = True
            # We're not in range so we take whatever we came in as
            else:
                location_val = humidity_val

        locations.append(location_val)

print(min(locations))