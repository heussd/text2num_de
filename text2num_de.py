# Converts German textual representations of numbers into integer values.
# Inspired by https://github.com/ghewgill/text2num
#
# This code is open source according to the MIT License as follows.
#
# Copyright (c) 2019 Timm Heuss
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


numbers = {
    "hundert": "00 ",
    "elf": "11 ",
    "zwölf": "12 ",
    "dreizehn": "13 ",
    "vierzehn": "14 ",
    "fünfzehn": "14 ",
    "sechszehn": "16 ",
    "siebzehn": "17 ",
    "achtzehn": "18 ",
    "neunzehn": "19 ",
    "eins": 1,
    "zwei": 2,
    "drei": 3,
    "fünf": 5,
    "sechs": 6,
    "sech": 6,
    "sieben": 7,
    "sieb": 7,
    "acht": 8,
    "neun": 9,
    "vier": 4,
    "zig": "0 ",
    "ßig": "0 ",
    "zwan": "2",
    "und": " ",
    "ein": "1"
}


def merge_figures(digits):
    number = None

    for digit in digits:
        if number is None:
            number = digit
        else:
            if int(digit) == 0:
                number = number + digit
            else:
                number = number[:-len(digit)] + digit
    return number


def text2num(giventext):
    inputtext = giventext.lower()
    inputtext = inputtext.replace("milliarden", "000000000 ")
    inputtext = inputtext.replace("millionen", "000000 ")
    inputtext = inputtext.replace("tausend", "000 ")
    inputtext = inputtext.split(" ")

    result = ""
    for text in inputtext:
        if len(text) > 0:
            for word in numbers:
                text = text.replace(word, str(numbers.get(word)))
            # print(text)

            digits = text.strip().split(" ")

            for i in range(len(digits)):
                if i > 0:
                    if len(digits[i]) == 2 and len(digits[i - 1]) == 1:
                        digits[i], digits[i - 1] = digits[i - 1], digits[i]

            number = merge_figures(digits)
            result = merge_figures((result, number))

    # print(giventext, " -> ", result)
    return int(result)


if __name__ == "__main__":
    assert 314000 == text2num("Dreihundertvierzehntausend")
    assert 260000 == text2num("Zweihundertsechzigtausend")
    assert 120000000 == text2num("einhundertzwanzigmillionen")
    assert 22022022 == text2num("zweiundzwanzigmillionenzweiundzwanzigtausendzweiundzwanzig")
    assert 22003 == text2num("zweiundzwanzigtausenddrei")
    assert 49128022003 == text2num("neunundvierzigmilliardeneinhundertachtundzwanzigmillionenzweiundzwanzigtausenddrei")
    assert 51000000000 == text2num("einundfünfzigmilliarden")
    assert 80000001 == text2num("achtzigmillioneneins")
    assert 80000001 == text2num("achtzigmillionenundeins")
    assert 22 == text2num("zweiundzwanzig")
    assert 22000000 == text2num("zweiundzwanzigmillionen")
    assert 30721 == text2num("dreißigtausendsiebenhunderteinundzwanzig")
    assert 721 == text2num("siebenhunderteinundzwanzig")
    assert 575 == text2num("fünfhundertfünfundsiebzig")
    assert 1 == text2num("eins")
    assert 89 == text2num("neunundachtzig")
    assert 12 == text2num("zwölf")
    assert 11 == text2num("elf")
    assert 60 == text2num("sechszig")
    assert 250 == text2num("zweihundertfünfzig")
    assert 307 == text2num("dreihundertsieben")
    assert 20 == text2num("zwanzig")
    assert 30 == text2num("dreißig")
    assert 7000 == text2num("siebentausend")
    assert 4001 == text2num("viertausendeins")
