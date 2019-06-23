# -*- encoding: utf-8 -*-

from unittest import TestCase, skip

from minim.palindrome import is_strict_palindrome, is_relaxed_palindrome

VALID_STRICT_PALINDROMES = [
    'a',
    'å',
    'AA',
    'ÄÄ',
    'baab',
    'BaB',
    'BäB',
    '123bab321',
    'aB c+-12_3_21-+c Ba',
]

VALID_NON_STRICT_PALINDROMES = [
    'a ',
    'b ab',
    ' Ba a B',
    'B.a..B',
    'B9 B',
    'Bå å. B',
    'Aö   ö A',

    # The following list taken from http://www.palindromelist.net/
    'A car, a man, a maraca.',
    'A dog! A panic in a pagoda!',
    'Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.',
    'Art, name no tub time. Emit but one mantra.',
    'Pull up, Eva, we’re here! Wave! Pull up!',
    'Pot top.',
]

INVALID_PALINDROMES = [
    't7RP9CbuOPq6;qlvH#<&',
    '(|o>`WfB/n..&~ %B{0%',
    'X?Yj tA`>nF)Y}T$<EH1',
    '5A9""Q8oHfo %*um%85T',
    'g%/bl|xå"L;MmuS&6BH?',
    'gO$lf5BNb?lMPkZ,H7 S',
    'U~X+pC)=`$Z$y_I!mOr!',
    'w0HM^x(7r]Q"{BUS+m=#',
    '%?E=viJÖR5|Kp`Y{!? m',
    '%YX&UJgGr0eo,KrM}W74',
    'vqN* e#9Fw[2LY=+vRd(',
    'Jpsb0C+`BRJnN;9q9g~k',
    'pJ$MQ%eqf*-WUg,r}L.C',
    '$h;#V3DHX6=GdC1+*T"j',
    'Ds@^ef+öi3iM98}Uh@mW',
    'b`<:\9K[w2{W9wV&E[fC',
    'WjHhuoT2euV.k{`bkP=)',
    'f4<-]{Fz\lxZbBQ#]S b',
    'O;s2/*kH,d{Mzf1X#]Cq',
    'K>30uänoI#.shiVr@B@1',
    'BkaO%h%I-!4xpM*):z@B',
]


# noinspection PyUnresolvedReferences
class BasePalindrome(object):
    def setUp(self) -> None:
        self.function_under_test = None

    def test_none(self):
        self.assertFalse(self.function_under_test(None))

    def test_empty_string(self):
        self.assertFalse(self.function_under_test(''))

    def test_invalid_palindromes(self):
        for p in INVALID_PALINDROMES:
            with self.subTest(p=p):
                self.assertFalse(self.function_under_test(p))


class StrictPalindromeTestCase(BasePalindrome, TestCase):
    def setUp(self):
        self.function_under_test = is_strict_palindrome

    def test_strict_palindromes(self):
        for p in VALID_STRICT_PALINDROMES:
            with self.subTest(p=p):
                self.assertTrue(is_strict_palindrome(p))

    def test_non_strict_palindromes(self):
        for p in VALID_NON_STRICT_PALINDROMES:
            with self.subTest(p=p):
                self.assertFalse(is_strict_palindrome(p), 'checking if "%s" is a strict palindrome' % p)


class RelaxedPalindromeTestCase(BasePalindrome, TestCase):
    def setUp(self):
        self.function_under_test = is_relaxed_palindrome

    def test_strict_palindromes(self):
        for p in VALID_STRICT_PALINDROMES:
            with self.subTest(p=p):
                self.assertTrue(is_relaxed_palindrome(p))

    def test_non_strict_palindromes(self):
        for p in VALID_NON_STRICT_PALINDROMES:
            with self.subTest(p=p):
                self.assertTrue(is_relaxed_palindrome(p), 'checking if "%s" is a relaxed palindrome' % p)
