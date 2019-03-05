#http://doc.openalpr.com/sdk.html#language-bindings
import sys
from openalpr import Alpr

alpr = Alpr("us", "C:\Windows\System32\openalpr\windows\build\dist\2.2.0\v140\Release\Win32\config.conf", "C:\Windows\System32\openalpr\windows\build\dist\2.2.0\v140\Release\Win32\runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
print("Loaded ALPR!")

alpr.set_top_n(20)
alpr.set_default_region("az")

results = alpr.recognize_file("test.jpg")

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
alpr.unload()
