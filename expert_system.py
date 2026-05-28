def computer_expert_system():
    print("=" * 60)
    print("🤖 COMPUTER TROUBLESHOOTING EXPERT SYSTEM 🤖")
    print("=" * 60)
    print("Answer the following questions with 'yes' or 'no' to diagnose your issue.\n")

    def ask_symptom(question_text):
        while True:
            response = input(f"{question_text} (yes/no): ").strip().lower()
            if response in ['yes', 'y']:
                return True
            if response in ['no', 'n']:
                return False
            print("❌ Invalid input! Please enter strictly 'yes' or 'no'.\n")

    power_turns_on = ask_symptom("Does the computer power turn on (lights/fans working)?")
    screen_displays = False
    beeping_sounds = False
    os_boots = False
    internet_working = False
    slow_performance = False

    if power_turns_on:
        screen_displays = ask_symptom("Does the monitor screen display anything?")
        if not screen_displays:
            beeping_sounds = ask_symptom("Do you hear unusual repetitive beeping sounds from the computer tower?")
        else:
            os_boots = ask_symptom("Does the Operating System (Windows/Mac) load up completely?")
            if os_boots:
                internet_working = ask_symptom("Is your internet connection working properly?")
                slow_performance = ask_symptom("Is the computer running extremely slow or freezing?")
    else:
        pass

    print("\n" + "=" * 40)
    print("🔍 DIAGNOSIS AND REASONING REPORT")
    print("=" * 40)
    if not power_turns_on:
        print("Diagnosis: Power Supply Unit (PSU) or Cable Failure 🔌")
        print("Reasoning: Because the system does not show signs of physical power (no fans/lights), the root issue sits at the electrical entry point. Check your power strip, wall outlets, and main PSU switch.")

    elif power_turns_on and not screen_displays and beeping_sounds:
        print("Diagnosis: RAM (Memory) Seating Issue or Failure 🧠")
        print("Reasoning: The motherboard is receiving electrical power but failing its initial POST (Power-On Self-Test) routine. Repetitive beeping sequences with a blank screen typically pinpoint faulty or unseated RAM modules.")

    elif power_turns_on and not screen_displays and not beeping_sounds:
        print("Diagnosis: GPU (Graphics Card) or Monitor Cable Fault 🖥️")
        print("Reasoning: The system successfully powers up without critical POST errors (no motherboards alerts), yet no video data reaches the display matrix. Verify HDMI/DisplayPort cable structural integrity and GPU slot connections.")

    elif power_turns_on and screen_displays and not os_boots:
        print("Diagnosis: Hard Drive (Storage) or Operating System Corruption 💾")
        print("Reasoning: Electrical paths and BIOS boot structures are operational. However, the system cannot find or read a bootable operating system partition on your storage drive.")

    elif power_turns_on and screen_displays and os_boots and not internet_working:
        print("Diagnosis: Network Adapter Issue or DNS Configuration Fault 🌐")
        print("Reasoning: Hardware systems and software boot states are completely healthy. The breakdown is localized purely inside network protocol layers or wireless physical adapters.")

    elif power_turns_on and screen_displays and os_boots and slow_performance:
        print("Diagnosis: Thermal Throttling or Excess Background Resource Drain 🌡️")
        print("Reasoning: The machine functions correctly but struggles with workloads. This points to high CPU/RAM usage from background programs or high internal temperatures forcing the hardware to slow down to prevent heat damage.")

    else:
        print("Diagnosis: System Status Healthy! No obvious hardware or software faults found. ✅")
        print("Reasoning: Based on your inputs, all baseline criteria for a functional workstation (Power, Video, OS Boot, Performance, and Network) are working normally.")

    print("=" * 60)

if __name__ == "__main__":
    computer_expert_system()
