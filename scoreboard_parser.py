# scoreboard_parser.py
# Simple scoreboard log parser for DV/UVM logs

def parse_log(file_name):
    total = 0
    passed = 0
    failed = 0

    with open(file_name, "r") as f:
        for line in f:
            if "PASS" in line:
                passed += 1
                total += 1
            elif "FAIL" in line:
                failed += 1
                total += 1

    return total, passed, failed


def main():
    log_file = "sample_log.txt"
    total, passed, failed = parse_log(log_file)

    print("----- SCOREBOARD SUMMARY -----")
    print(f"Total Transactions : {total}")
    print(f"PASS               : {passed}")
    print(f"FAIL               : {failed}")

    if failed == 0:
        print("RESULT : TEST PASSED")
    else:
        print("RESULT : TEST FAILED")


if __name__ == "__main__":
    main()
