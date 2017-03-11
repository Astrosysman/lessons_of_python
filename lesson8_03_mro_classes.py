#!/usr/bin/env python3

class Stars:
	pass

class SpectralClassO:
	pass

class SpectralClassB:
	pass

class SpectralClassA:
	pass

class SpectralClassF:
	pass

class SpectralClassG:
	pass

class SpectralClassK:
	pass

class SpectralClassM:
	pass

class SpectralClassL:
	pass

class SpectralClassT:
	pass

class AbsoluteMagnitudeNeg15Neg10:
	pass

class AbsoluteMagnitudeNeg10Neg05:
	pass

class AbsoluteMagnitudeNeg05Zero:
	pass

class AbsoluteMagnitudeZeroPos05:
	pass

class AbsoluteMagnitudePos05Pos10:
	pass

class AbsoluteMagnitudePos10Pos15:
	pass

class AbsoluteMagnitudePos15Pos20:
	pass

class RedStars(Stars):
	pass

class BlueStars(Stars):
	pass

class WhiteStars(Stars):
	pass

class YellowStars(Stars):
	pass

class BrownStars(Stars):
	pass

class Giants(SpectralClassB, SpectralClassA, SpectralClassF, SpectralClassG, SpectralClassK, SpectralClassM, AbsoluteMagnitudeNeg05Zero, BlueStars, WhiteStars, YellowStars, RedStars):
	pass

class HyperGiants(Giants, SpectralClassA, SpectralClassF, SpectralClassG, SpectralClassK, AbsoluteMagnitudeNeg15Neg10):
	pass

class SuperGiants(Giants, SpectralClassA, SpectralClassF, SpectralClassG, SpectralClassK, AbsoluteMagnitudeNeg10Neg05):
	pass

class SubGiants(Giants, SpectralClassA, SpectralClassF, SpectralClassG, SpectralClassK, AbsoluteMagnitudeZeroPos05):
	pass

class Dwarfs(SpectralClassB, SpectralClassA, SpectralClassF, SpectralClassG, SpectralClassK, SpectralClassM, AbsoluteMagnitudeNeg05Zero, AbsoluteMagnitudeZeroPos05, AbsoluteMagnitudePos05Pos10, AbsoluteMagnitudePos10Pos15, AbsoluteMagnitudePos15Pos20, WhiteStars, YellowStars, RedStars, BrownStars):
	pass

class SubDwarfs(Dwarfs, SpectralClassG, SpectralClassK, SpectralClassM, AbsoluteMagnitudePos05Pos10, YellowStars):
	pass

class WhiteDwarfs(Dwarfs, SpectralClassB, SpectralClassA, SpectralClassF, SpectralClassK, AbsoluteMagnitudePos10Pos15, WhiteStars):
	pass

class RedDwarfs(Dwarfs, SpectralClassM, SpectralClassL, SpectralClassT, AbsoluteMagnitudePos10Pos15, RedStars):
	pass

class BrownDwarfs(Dwarfs, SpectralClassM, SpectralClassL, SpectralClassT, AbsoluteMagnitudePos15Pos20, BrownStars):
	pass


def main():

	print(Stars().__class__.__mro__)
	print(SpectralClassO().__class__.__mro__)
	print(SpectralClassB().__class__.__mro__)
	print(SpectralClassA().__class__.__mro__)
	print(SpectralClassF().__class__.__mro__)
	print(SpectralClassG().__class__.__mro__)
	print(SpectralClassK().__class__.__mro__)
	print(SpectralClassM().__class__.__mro__)
	print(SpectralClassL().__class__.__mro__)
	print(SpectralClassT().__class__.__mro__)
	print(AbsoluteMagnitudeNeg15Neg10().__class__.__mro__)
	print(AbsoluteMagnitudeNeg10Neg05().__class__.__mro__)
	print(AbsoluteMagnitudeNeg05Zero().__class__.__mro__)
	print(AbsoluteMagnitudeZeroPos05().__class__.__mro__)
	print(AbsoluteMagnitudePos05Pos10().__class__.__mro__)
	print(AbsoluteMagnitudePos10Pos15().__class__.__mro__)
	print(AbsoluteMagnitudePos15Pos20().__class__.__mro__)
	print(RedStars().__class__.__mro__)
	print(BlueStars().__class__.__mro__)
	print(WhiteStars().__class__.__mro__)
	print(YellowStars().__class__.__mro__)
	print(BrownStars().__class__.__mro__)
	print(Giants().__class__.__mro__)
	print(HyperGiants().__class__.__mro__)
	print(SuperGiants().__class__.__mro__)
	print(SubGiants().__class__.__mro__)
	print(Dwarfs().__class__.__mro__)
	print(SubDwarfs().__class__.__mro__)
	print(WhiteDwarfs().__class__.__mro__)
	print(RedDwarfs().__class__.__mro__)
	print(BrownDwarfs().__class__.__mro__)


main()

