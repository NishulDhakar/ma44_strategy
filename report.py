def report(results):
    wins = sum(1 for r in results if r > 0)
    losses = sum(1 for r in results if r < 0)

    print("Total Trades:", len(results))
    print("Wins:", wins)
    print("Losses:", losses)
    print("Win Rate:", wins / len(results) * 100)
    print("Total RR:", sum(results))
