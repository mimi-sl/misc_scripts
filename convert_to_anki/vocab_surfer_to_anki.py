import csv

def convert_to_anki(infile, outfile):
    vocab_cards = parse_infile(infile)
    write_outfile(outfile, vocab_cards)

def parse_infile(infile):
    with open(infile, 'r') as inf:
        # will end up being a list of dicts in the form {'side_a': 'clue', 'side_b': 'target'}
        vocab_cards = []

        # 0th line is the target word, 1st line is the clue word
        # every 9 lines it restarts
        line_count = 0

        for line in inf:
            if line_count == 0:
                vocab_dict = {'side_a': line.strip(), 'side_b': ''}

            elif line_count == 1:
                vocab_dict['side_b'] = line.strip()
                vocab_cards.append(vocab_dict)

            elif line_count == 8:
                line_count = 0
                target_word = ''
                continue

            line_count += 1

        return vocab_cards

def write_outfile(outfile, vocab_cards):
    with open(outfile, 'w', newline='') as csvfile:
        fieldnames = ['side_a', 'side_b']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for card in vocab_cards:
            writer.writerow(card)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='intakes a csv of vocab surfer data'\
                                                    'and outputs a csv for import into anki')
    parser.add_argument('infile', help='the infile from vocab surfer, is a txt file')
    parser.add_argument('outfile', help='the outfile in anki format, is a csv')
    args = parser.parse_args()

    convert_to_anki(args.infile, args.outfile)
