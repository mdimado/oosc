import sys
import atheris
import markdown2
from markdown2 import Markdown, LinkProcessor


def TestOneInput(data: bytes):
    fdp = atheris.FuzzedDataProvider(data)
    text = fdp.ConsumeUnicodeNoSurrogates(10000)

    md = Markdown(safe_mode=True)
    link_processor = LinkProcessor(md, None)

    # If test() matches, run it
    if link_processor.test(text):
        link_processor.run(text)

    # Also fuzz the full Markdown path to reach nested states
    md.convert(text)

    
def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
