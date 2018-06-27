# Generated from OParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00b0\u09a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\4")
        buf.write(u"8\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@")
        buf.write(u"\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\t")
        buf.write(u"I\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R")
        buf.write(u"\tR\4S\tS\4T\tT\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4")
        buf.write(u"[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\t")
        buf.write(u"c\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l")
        buf.write(u"\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4")
        buf.write(u"u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}")
        buf.write(u"\4~\t~\4\177\t\177\4\u0080\t\u0080\4\u0081\t\u0081\4")
        buf.write(u"\u0082\t\u0082\4\u0083\t\u0083\4\u0084\t\u0084\4\u0085")
        buf.write(u"\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087\4\u0088\t\u0088")
        buf.write(u"\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b\t\u008b\4\u008c")
        buf.write(u"\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e\4\u008f\t\u008f")
        buf.write(u"\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092\t\u0092\4\u0093")
        buf.write(u"\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095\4\u0096\t\u0096")
        buf.write(u"\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099\t\u0099\4\u009a")
        buf.write(u"\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c\4\u009d\t\u009d")
        buf.write(u"\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0\t\u00a0\4\u00a1")
        buf.write(u"\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3\4\u00a4\t\u00a4")
        buf.write(u"\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7\t\u00a7\4\u00a8")
        buf.write(u"\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa\4\u00ab\t\u00ab")
        buf.write(u"\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae\t\u00ae\4\u00af")
        buf.write(u"\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1\4\u00b2\t\u00b2")
        buf.write(u"\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5\t\u00b5\4\u00b6")
        buf.write(u"\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8\4\u00b9\t\u00b9")
        buf.write(u"\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc\t\u00bc\4\u00bd")
        buf.write(u"\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf\4\u00c0\t\u00c0")
        buf.write(u"\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3\t\u00c3\4\u00c4")
        buf.write(u"\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6\4\u00c7\t\u00c7")
        buf.write(u"\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca\t\u00ca\4\u00cb")
        buf.write(u"\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd\4\u00ce\t\u00ce")
        buf.write(u"\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1\t\u00d1\4\u00d2")
        buf.write(u"\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4\4\u00d5\t\u00d5")
        buf.write(u"\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8\t\u00d8\4\u00d9")
        buf.write(u"\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db\4\u00dc\t\u00dc")
        buf.write(u"\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df\t\u00df\4\u00e0")
        buf.write(u"\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2\4\u00e3\t\u00e3")
        buf.write(u"\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6\t\u00e6\4\u00e7")
        buf.write(u"\t\u00e7\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u01d6\n\2\3")
        buf.write(u"\2\3\2\5\2\u01da\n\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\6\5\6\u01f5\n\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write(u"\6\u01fc\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0204\n\6\5")
        buf.write(u"\6\u0206\n\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u020e\n\7\3")
        buf.write(u"\7\3\7\3\b\5\b\u0213\n\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write(u"\u021b\n\b\3\b\3\b\5\b\u021f\n\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\5\t\u0229\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\7\n\u0233\n\n\f\n\16\n\u0236\13\n\3\13\3\13\3")
        buf.write(u"\13\5\13\u023b\n\13\3\13\5\13\u023e\n\13\3\f\5\f\u0241")
        buf.write(u"\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u024a\n\f\3\f\3")
        buf.write(u"\f\3\r\3\r\3\r\3\r\5\r\u0252\n\r\3\r\3\r\3\16\5\16\u0257")
        buf.write(u"\n\16\3\16\3\16\3\16\3\16\5\16\u025d\n\16\3\16\3\16\3")
        buf.write(u"\17\3\17\3\17\3\17\5\17\u0265\n\17\3\17\3\17\3\20\5\20")
        buf.write(u"\u026a\n\20\3\20\3\20\3\20\3\20\5\20\u0270\n\20\3\20")
        buf.write(u"\3\20\3\21\5\21\u0275\n\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\5\21\u027e\n\21\3\21\3\21\3\21\5\21\u0283\n")
        buf.write(u"\21\3\21\3\21\3\22\5\22\u0288\n\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\5\22\u0291\n\22\3\22\3\22\3\22\5\22\u0296")
        buf.write(u"\n\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u02a8\n\24\f\24")
        buf.write(u"\16\24\u02ab\13\24\3\25\3\25\5\25\u02af\n\25\3\25\3\25")
        buf.write(u"\3\25\3\25\5\25\u02b5\n\25\3\25\3\25\3\25\3\26\5\26\u02bb")
        buf.write(u"\n\26\3\26\3\26\3\26\3\26\5\26\u02c1\n\26\3\26\3\26\3")
        buf.write(u"\26\5\26\u02c6\n\26\3\26\3\26\3\27\5\27\u02cb\n\27\3")
        buf.write(u"\27\5\27\u02ce\n\27\3\27\3\27\3\27\3\27\5\27\u02d4\n")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\5\30\u02eb\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\5\32\u02f5\n\32\3\32\3\32\3\32\5\32\u02fa\n\32")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\5\33\u0301\n\33\5\33\u0303")
        buf.write(u"\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\5\34\u031a\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3")
        buf.write(u"\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\5\36\u0338\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write(u"\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u034f\n")
        buf.write(u"!\5!\u0351\n!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0359\n\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\5\"\u0360\n\"\5\"\u0362\n\"\3#\3#\3")
        buf.write(u"#\3#\3#\3#\5#\u036a\n#\3#\3#\3#\3#\3#\3$\3$\3$\5$\u0374")
        buf.write(u"\n$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write(u"&\3&\3&\5&\u0389\n&\3&\3&\5&\u038d\n&\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'")
        buf.write(u"\u039f\n\'\f\'\16\'\u03a2\13\'\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(u")\3)\3)\5)\u03ae\n)\3)\3)\5)\u03b2\n)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\5)\u03ba\n)\3)\5)\u03bd\n)\3)\3)\3)\5)\u03c2\n)\3")
        buf.write(u")\5)\u03c5\n)\3*\3*\3*\3*\3*\3*\5*\u03cd\n*\3*\3*\3*")
        buf.write(u"\3*\3*\3*\3*\3*\3*\5*\u03d8\n*\3*\3*\5*\u03dc\n*\3+\3")
        buf.write(u"+\3+\3,\3,\5,\u03e3\n,\3,\3,\3-\3-\3-\5-\u03ea\n-\3-")
        buf.write(u"\3-\3.\3.\3.\3.\3.\5.\u03f3\n.\3/\3/\3/\3/\3/\7/\u03fa")
        buf.write(u"\n/\f/\16/\u03fd\13/\3\60\3\60\3\60\3\60\3\60\3\60\5")
        buf.write(u"\60\u0405\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\5\61\u041f\n\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u0493\n\61\f")
        buf.write(u"\61\16\61\u0496\13\61\3\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\7\64\u04a3\n\64\f\64\16\64\u04a6")
        buf.write(u"\13\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5")
        buf.write(u"\65\u04b1\n\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write(u"\5\67\u04bb\n\67\3\67\3\67\38\38\38\38\38\38\38\38\3")
        buf.write(u"9\39\39\39\39\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3:")
        buf.write(u"\3:\5:\u04da\n:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u04e7")
        buf.write(u"\n:\3:\3:\3:\3:\5:\u04ed\n:\3:\3:\3:\3:\3:\3:\3:\5:\u04f6")
        buf.write(u"\n:\3:\3:\3:\3:\3:\5:\u04fd\n:\3:\3:\3:\3:\3:\3:\5:\u0505")
        buf.write(u"\n:\5:\u0507\n:\3;\3;\5;\u050b\n;\3;\3;\3;\3;\3;\3;\3")
        buf.write(u";\5;\u0514\n;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<")
        buf.write(u"\u0522\n<\3=\3=\3=\3=\3=\5=\u0529\n=\3=\3=\3=\3=\3=\5")
        buf.write(u"=\u0530\n=\3=\3=\5=\u0534\n=\3>\3>\3>\3>\3>\3?\3?\3?")
        buf.write(u"\3?\3?\5?\u0540\n?\3?\3?\3?\7?\u0545\n?\f?\16?\u0548")
        buf.write(u"\13?\3@\3@\3@\3@\5@\u054e\n@\3A\3A\3A\3A\3A\3B\3B\3B")
        buf.write(u"\3B\3B\3B\5B\u055b\nB\3C\3C\3C\3C\3C\3D\3D\3E\5E\u0565")
        buf.write(u"\nE\3E\3E\3E\3F\3F\3F\3F\7F\u056e\nF\fF\16F\u0571\13")
        buf.write(u"F\3G\3G\3G\7G\u0576\nG\fG\16G\u0579\13G\3G\3G\3G\3G\3")
        buf.write(u"G\3G\5G\u0581\nG\3H\3H\3I\3I\5I\u0587\nI\3J\3J\3J\3J")
        buf.write(u"\7J\u058d\nJ\fJ\16J\u0590\13J\3K\3K\3K\3K\7K\u0596\n")
        buf.write(u"K\fK\16K\u0599\13K\3L\3L\3L\7L\u059e\nL\fL\16L\u05a1")
        buf.write(u"\13L\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\5M\u05ad\nM\3N\5N")
        buf.write(u"\u05b0\nN\3N\3N\5N\u05b4\nN\3N\3N\3O\5O\u05b9\nO\3O\3")
        buf.write(u"O\5O\u05bd\nO\3O\3O\3P\3P\3P\7P\u05c4\nP\fP\16P\u05c7")
        buf.write(u"\13P\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R")
        buf.write(u"\3R\3R\5R\u05db\nR\3R\3R\3R\3R\3R\3R\3R\3R\7R\u05e5\n")
        buf.write(u"R\fR\16R\u05e8\13R\3S\3S\5S\u05ec\nS\3T\3T\3T\3T\3T\3")
        buf.write(u"T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\5T\u05fe\nT\3U\3U\3V")
        buf.write(u"\5V\u0603\nV\3V\3V\3W\3W\3X\3X\3X\5X\u060c\nX\3Y\3Y\3")
        buf.write(u"Z\3Z\3Z\7Z\u0613\nZ\fZ\16Z\u0616\13Z\3[\3[\5[\u061a\n")
        buf.write(u"[\3\\\3\\\3\\\5\\\u061f\n\\\3]\3]\3^\3^\3_\3_\3`\3`\3")
        buf.write(u"a\3a\3a\7a\u062c\na\fa\16a\u062f\13a\3b\3b\5b\u0633\n")
        buf.write(u"b\3b\5b\u0636\nb\3c\3c\5c\u063a\nc\3d\3d\3d\5d\u063f")
        buf.write(u"\nd\3e\3e\3e\3f\3f\5f\u0646\nf\3g\3g\3g\3g\3g\3g\3g\3")
        buf.write(u"g\3g\7g\u0651\ng\fg\16g\u0654\13g\3h\3h\3h\3h\7h\u065a")
        buf.write(u"\nh\fh\16h\u065d\13h\3i\3i\3i\3i\3i\5i\u0664\ni\3j\3")
        buf.write(u"j\3j\3j\7j\u066a\nj\fj\16j\u066d\13j\3k\3k\3k\5k\u0672")
        buf.write(u"\nk\3l\3l\3l\3l\3l\3l\3l\3l\3l\3l\5l\u067e\nl\3m\3m\5")
        buf.write(u"m\u0682\nm\3n\3n\3n\3n\3n\3n\7n\u068a\nn\fn\16n\u068d")
        buf.write(u"\13n\3o\3o\5o\u0691\no\3p\3p\3p\3p\5p\u0697\np\3p\3p")
        buf.write(u"\3p\7p\u069c\np\fp\16p\u069f\13p\3p\3p\5p\u06a3\np\3")
        buf.write(u"q\3q\3q\7q\u06a8\nq\fq\16q\u06ab\13q\3r\3r\3r\7r\u06b0")
        buf.write(u"\nr\fr\16r\u06b3\13r\3s\3s\3s\3s\5s\u06b9\ns\3t\3t\3")
        buf.write(u"u\3u\3u\3u\7u\u06c1\nu\fu\16u\u06c4\13u\3v\3v\3v\3v\3")
        buf.write(u"v\3v\3v\3v\3v\3v\5v\u06d0\nv\3w\3w\5w\u06d4\nw\3w\5w")
        buf.write(u"\u06d7\nw\3x\3x\5x\u06db\nx\3x\5x\u06de\nx\3y\3y\3y\3")
        buf.write(u"y\7y\u06e4\ny\fy\16y\u06e7\13y\3z\3z\3z\3z\7z\u06ed\n")
        buf.write(u"z\fz\16z\u06f0\13z\3{\3{\3{\3{\7{\u06f6\n{\f{\16{\u06f9")
        buf.write(u"\13{\3|\3|\3|\3|\7|\u06ff\n|\f|\16|\u0702\13|\3}\3}\3")
        buf.write(u"}\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\5}\u0712\n}\3~\3~")
        buf.write(u"\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\5~\u0723\n~\3")
        buf.write(u"\177\3\177\3\177\7\177\u0728\n\177\f\177\16\177\u072b")
        buf.write(u"\13\177\3\u0080\3\u0080\3\u0080\3\u0080\5\u0080\u0731")
        buf.write(u"\n\u0080\3\u0081\3\u0081\3\u0082\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0083\3\u0083\5\u0083\u073b\n\u0083\3\u0084\3\u0084")
        buf.write(u"\3\u0084\3\u0084\3\u0084\5\u0084\u0742\n\u0084\3\u0085")
        buf.write(u"\5\u0085\u0745\n\u0085\3\u0085\3\u0085\5\u0085\u0749")
        buf.write(u"\n\u0085\3\u0085\3\u0085\3\u0086\5\u0086\u074e\n\u0086")
        buf.write(u"\3\u0086\3\u0086\5\u0086\u0752\n\u0086\3\u0086\3\u0086")
        buf.write(u"\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\7\u0087\u075b")
        buf.write(u"\n\u0087\f\u0087\16\u0087\u075e\13\u0087\5\u0087\u0760")
        buf.write(u"\n\u0087\3\u0088\3\u0088\3\u0088\7\u0088\u0765\n\u0088")
        buf.write(u"\f\u0088\16\u0088\u0768\13\u0088\3\u0089\3\u0089\3\u0089")
        buf.write(u"\3\u0089\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\5\u008a\u0777\n\u008a\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write(u"\3\u008c\7\u008c\u0782\n\u008c\f\u008c\16\u008c\u0785")
        buf.write(u"\13\u008c\3\u008d\3\u008d\3\u008d\3\u008d\5\u008d\u078b")
        buf.write(u"\n\u008d\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e\3\u008f")
        buf.write(u"\3\u008f\3\u008f\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090")
        buf.write(u"\7\u0090\u079a\n\u0090\f\u0090\16\u0090\u079d\13\u0090")
        buf.write(u"\3\u0091\3\u0091\3\u0091\7\u0091\u07a2\n\u0091\f\u0091")
        buf.write(u"\16\u0091\u07a5\13\u0091\3\u0091\5\u0091\u07a8\n\u0091")
        buf.write(u"\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092\5\u0092")
        buf.write(u"\u07b0\n\u0092\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094")
        buf.write(u"\3\u0095\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0097")
        buf.write(u"\3\u0097\3\u0097\3\u0098\3\u0098\3\u0098\3\u0099\3\u0099")
        buf.write(u"\3\u009a\3\u009a\3\u009b\3\u009b\3\u009c\3\u009c\3\u009d")
        buf.write(u"\3\u009d\3\u009e\3\u009e\3\u009f\3\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write(u"\5\u00a1\u07da\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\7\u00a2\u07e1\n\u00a2\f\u00a2\16\u00a2\u07e4")
        buf.write(u"\13\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\5\u00a3\u07ed\n\u00a3\3\u00a4\3\u00a4\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\5\u00a6\u07f9\n\u00a6\3\u00a7\3\u00a7\3\u00a7\5\u00a7")
        buf.write(u"\u07fe\n\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\7\u00a8\u0808\n\u00a8\f\u00a8")
        buf.write(u"\16\u00a8\u080b\13\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ac\3\u00ac\5\u00ac\u081c\n\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u0823")
        buf.write(u"\n\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\7\u00af")
        buf.write(u"\u082a\n\u00af\f\u00af\16\u00af\u082d\13\u00af\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b0\5\u00b0\u0834\n\u00b0")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\5\u00b2\u083e\n\u00b2\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\5\u00b3\u0843\n\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\3\u00b4\5\u00b4\u084d\n\u00b4")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5\7\u00b5")
        buf.write(u"\u0855\n\u00b5\f\u00b5\16\u00b5\u0858\13\u00b5\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u0865\n\u00b6\f\u00b6")
        buf.write(u"\16\u00b6\u0868\13\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b8\3\u00b8\3\u00b8\5\u00b8\u0871\n\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\7\u00b8\u0876\n\u00b8\f\u00b8\16\u00b8")
        buf.write(u"\u0879\13\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write(u"\5\u00b9\u0880\n\u00b9\3\u00ba\3\u00ba\3\u00bb\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\5\u00bb\u088b")
        buf.write(u"\n\u00bb\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc\7\u00bc")
        buf.write(u"\u0892\n\u00bc\f\u00bc\16\u00bc\u0895\13\u00bc\3\u00bd")
        buf.write(u"\3\u00bd\3\u00bd\3\u00bd\3\u00bd\5\u00bd\u089c\n\u00bd")
        buf.write(u"\3\u00be\3\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\5\u00c0\u08a6\n\u00c0\3\u00c1\3\u00c1\3\u00c1")
        buf.write(u"\5\u00c1\u08ab\n\u00c1\3\u00c1\3\u00c1\3\u00c2\3\u00c2")
        buf.write(u"\3\u00c2\3\u00c2\3\u00c2\3\u00c2\7\u00c2\u08b5\n\u00c2")
        buf.write(u"\f\u00c2\16\u00c2\u08b8\13\u00c2\3\u00c3\3\u00c3\3\u00c3")
        buf.write(u"\3\u00c3\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c5\3\u00c5")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c5\7\u00c5\u08c8\n\u00c5")
        buf.write(u"\f\u00c5\16\u00c5\u08cb\13\u00c5\3\u00c6\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\7\u00c6\u08d2\n\u00c6\f\u00c6\16\u00c6")
        buf.write(u"\u08d5\13\u00c6\3\u00c7\3\u00c7\3\u00c7\3\u00c7\3\u00c7")
        buf.write(u"\5\u00c7\u08dc\n\u00c7\3\u00c8\3\u00c8\3\u00c9\3\u00c9")
        buf.write(u"\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\5\u00c9\u08e7")
        buf.write(u"\n\u00c9\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\7\u00ca")
        buf.write(u"\u08ee\n\u00ca\f\u00ca\16\u00ca\u08f1\13\u00ca\3\u00cb")
        buf.write(u"\3\u00cb\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u08f8\n\u00cb")
        buf.write(u"\3\u00cc\3\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00ce\3\u00ce")
        buf.write(u"\3\u00ce\5\u00ce\u0902\n\u00ce\3\u00cf\3\u00cf\3\u00cf")
        buf.write(u"\5\u00cf\u0907\n\u00cf\3\u00cf\3\u00cf\3\u00d0\3\u00d0")
        buf.write(u"\3\u00d0\3\u00d0\3\u00d0\3\u00d0\7\u00d0\u0911\n\u00d0")
        buf.write(u"\f\u00d0\16\u00d0\u0914\13\u00d0\3\u00d1\3\u00d1\3\u00d1")
        buf.write(u"\3\u00d1\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d3\3\u00d3")
        buf.write(u"\3\u00d3\5\u00d3\u0921\n\u00d3\3\u00d3\3\u00d3\3\u00d3")
        buf.write(u"\7\u00d3\u0926\n\u00d3\f\u00d3\16\u00d3\u0929\13\u00d3")
        buf.write(u"\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d4\5\u00d4\u0930")
        buf.write(u"\n\u00d4\3\u00d5\3\u00d5\3\u00d6\3\u00d6\5\u00d6\u0936")
        buf.write(u"\n\u00d6\3\u00d7\3\u00d7\3\u00d7\5\u00d7\u093b\n\u00d7")
        buf.write(u"\3\u00d7\3\u00d7\5\u00d7\u093f\n\u00d7\3\u00d8\3\u00d8")
        buf.write(u"\5\u00d8\u0943\n\u00d8\3\u00d8\3\u00d8\3\u00d9\3\u00d9")
        buf.write(u"\3\u00d9\5\u00d9\u094a\n\u00d9\3\u00da\3\u00da\3\u00da")
        buf.write(u"\3\u00da\3\u00db\3\u00db\3\u00db\7\u00db\u0953\n\u00db")
        buf.write(u"\f\u00db\16\u00db\u0956\13\u00db\3\u00db\3\u00db\3\u00db")
        buf.write(u"\3\u00dc\3\u00dc\3\u00dc\7\u00dc\u095e\n\u00dc\f\u00dc")
        buf.write(u"\16\u00dc\u0961\13\u00dc\3\u00dc\3\u00dc\3\u00dd\3\u00dd")
        buf.write(u"\3\u00dd\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de\7\u00de")
        buf.write(u"\u096d\n\u00de\f\u00de\16\u00de\u0970\13\u00de\3\u00df")
        buf.write(u"\3\u00df\7\u00df\u0974\n\u00df\f\u00df\16\u00df\u0977")
        buf.write(u"\13\u00df\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e1\3\u00e1")
        buf.write(u"\3\u00e1\3\u00e2\3\u00e2\5\u00e2\u0982\n\u00e2\3\u00e3")
        buf.write(u"\3\u00e3\3\u00e3\5\u00e3\u0987\n\u00e3\3\u00e4\3\u00e4")
        buf.write(u"\3\u00e4\3\u00e4\3\u00e4\5\u00e4\u098e\n\u00e4\3\u00e5")
        buf.write(u"\6\u00e5\u0991\n\u00e5\r\u00e5\16\u00e5\u0992\3\u00e6")
        buf.write(u"\3\u00e6\3\u00e6\3\u00e6\5\u00e6\u0999\n\u00e6\3\u00e6")
        buf.write(u"\5\u00e6\u099c\n\u00e6\3\u00e7\6\u00e7\u099f\n\u00e7")
        buf.write(u"\r\u00e7\16\u00e7\u09a0\3\u00e7\2\31\22&L\\`f|\u00a2")
        buf.write(u"\u00cc\u0116\u0142\u014e\u015c\u0168\u016a\u016e\u0176")
        buf.write(u"\u0182\u0188\u018a\u0192\u019e\u01a4\u00e8\2\4\6\b\n")
        buf.write(u"\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:")
        buf.write(u"<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write(u"\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write(u"\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write(u"\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba")
        buf.write(u"\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc")
        buf.write(u"\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de")
        buf.write(u"\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0")
        buf.write(u"\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102")
        buf.write(u"\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112\u0114")
        buf.write(u"\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124\u0126")
        buf.write(u"\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136\u0138")
        buf.write(u"\u013a\u013c\u013e\u0140\u0142\u0144\u0146\u0148\u014a")
        buf.write(u"\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a\u015c")
        buf.write(u"\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c\u016e")
        buf.write(u"\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e\u0180")
        buf.write(u"\u0182\u0184\u0186\u0188\u018a\u018c\u018e\u0190\u0192")
        buf.write(u"\u0194\u0196\u0198\u019a\u019c\u019e\u01a0\u01a2\u01a4")
        buf.write(u"\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\u01b6")
        buf.write(u"\u01b8\u01ba\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8")
        buf.write(u"\u01ca\u01cc\2\r\3\2\36\37\4\2\u008f\u008f\u00a4\u00a4")
        buf.write(u"\4\2\u008b\u008b\u0093\u0093\4\2IIZZ\4\2\7\f\60\u009d")
        buf.write(u"\4\2##uu\r\2\609??BBxx{{\u0085\u0085\u008b\u008b\u0092")
        buf.write(u"\u0092\u009d\u009d\u00a2\u00a4\u00a6\u00a6\13\2\609?")
        buf.write(u"?BBxx{{\u0085\u0085\u0092\u0093\u009d\u009d\u00a2\u00a4")
        buf.write(u"\f\2\609??BBxx{{\u0085\u0085\u008b\u008b\u0092\u0092")
        buf.write(u"\u009d\u009d\u00a2\u00a6\f\2\609??BBxx{{\u0085\u0085")
        buf.write(u"\u008b\u008b\u0092\u0092\u009d\u009d\u00a2\u00a4\5\2")
        buf.write(u"\26\27$$&&\2\u0a2e\2\u01ce\3\2\2\2\4\u01df\3\2\2\2\6")
        buf.write(u"\u01e8\3\2\2\2\b\u01ee\3\2\2\2\n\u01f4\3\2\2\2\f\u0209")
        buf.write(u"\3\2\2\2\16\u0212\3\2\2\2\20\u0222\3\2\2\2\22\u022c\3")
        buf.write(u"\2\2\2\24\u023d\3\2\2\2\26\u0240\3\2\2\2\30\u024d\3\2")
        buf.write(u"\2\2\32\u0256\3\2\2\2\34\u0260\3\2\2\2\36\u0269\3\2\2")
        buf.write(u"\2 \u0274\3\2\2\2\"\u0287\3\2\2\2$\u0299\3\2\2\2&\u029f")
        buf.write(u"\3\2\2\2(\u02ac\3\2\2\2*\u02ba\3\2\2\2,\u02ca\3\2\2\2")
        buf.write(u".\u02da\3\2\2\2\60\u02ec\3\2\2\2\62\u02ef\3\2\2\2\64")
        buf.write(u"\u0302\3\2\2\2\66\u0319\3\2\2\28\u031b\3\2\2\2:\u0337")
        buf.write(u"\3\2\2\2<\u0339\3\2\2\2>\u033f\3\2\2\2@\u0345\3\2\2\2")
        buf.write(u"B\u0361\3\2\2\2D\u0363\3\2\2\2F\u0370\3\2\2\2H\u037c")
        buf.write(u"\3\2\2\2J\u0382\3\2\2\2L\u038e\3\2\2\2N\u03a3\3\2\2\2")
        buf.write(u"P\u03a7\3\2\2\2R\u03db\3\2\2\2T\u03dd\3\2\2\2V\u03e0")
        buf.write(u"\3\2\2\2X\u03e6\3\2\2\2Z\u03f2\3\2\2\2\\\u03f4\3\2\2")
        buf.write(u"\2^\u0404\3\2\2\2`\u041e\3\2\2\2b\u0497\3\2\2\2d\u049b")
        buf.write(u"\3\2\2\2f\u049d\3\2\2\2h\u04b0\3\2\2\2j\u04b2\3\2\2\2")
        buf.write(u"l\u04b7\3\2\2\2n\u04be\3\2\2\2p\u04c6\3\2\2\2r\u0506")
        buf.write(u"\3\2\2\2t\u0508\3\2\2\2v\u0521\3\2\2\2x\u0533\3\2\2\2")
        buf.write(u"z\u0535\3\2\2\2|\u053f\3\2\2\2~\u0549\3\2\2\2\u0080\u054f")
        buf.write(u"\3\2\2\2\u0082\u055a\3\2\2\2\u0084\u055c\3\2\2\2\u0086")
        buf.write(u"\u0561\3\2\2\2\u0088\u0564\3\2\2\2\u008a\u0569\3\2\2")
        buf.write(u"\2\u008c\u0577\3\2\2\2\u008e\u0582\3\2\2\2\u0090\u0586")
        buf.write(u"\3\2\2\2\u0092\u0588\3\2\2\2\u0094\u0591\3\2\2\2\u0096")
        buf.write(u"\u059a\3\2\2\2\u0098\u05ac\3\2\2\2\u009a\u05af\3\2\2")
        buf.write(u"\2\u009c\u05b8\3\2\2\2\u009e\u05c0\3\2\2\2\u00a0\u05c8")
        buf.write(u"\3\2\2\2\u00a2\u05da\3\2\2\2\u00a4\u05eb\3\2\2\2\u00a6")
        buf.write(u"\u05fd\3\2\2\2\u00a8\u05ff\3\2\2\2\u00aa\u0602\3\2\2")
        buf.write(u"\2\u00ac\u0606\3\2\2\2\u00ae\u060b\3\2\2\2\u00b0\u060d")
        buf.write(u"\3\2\2\2\u00b2\u060f\3\2\2\2\u00b4\u0619\3\2\2\2\u00b6")
        buf.write(u"\u061e\3\2\2\2\u00b8\u0620\3\2\2\2\u00ba\u0622\3\2\2")
        buf.write(u"\2\u00bc\u0624\3\2\2\2\u00be\u0626\3\2\2\2\u00c0\u0628")
        buf.write(u"\3\2\2\2\u00c2\u0635\3\2\2\2\u00c4\u0639\3\2\2\2\u00c6")
        buf.write(u"\u063b\3\2\2\2\u00c8\u0640\3\2\2\2\u00ca\u0645\3\2\2")
        buf.write(u"\2\u00cc\u0647\3\2\2\2\u00ce\u0655\3\2\2\2\u00d0\u0663")
        buf.write(u"\3\2\2\2\u00d2\u0665\3\2\2\2\u00d4\u0671\3\2\2\2\u00d6")
        buf.write(u"\u067d\3\2\2\2\u00d8\u067f\3\2\2\2\u00da\u0683\3\2\2")
        buf.write(u"\2\u00dc\u068e\3\2\2\2\u00de\u0692\3\2\2\2\u00e0\u06a4")
        buf.write(u"\3\2\2\2\u00e2\u06ac\3\2\2\2\u00e4\u06b8\3\2\2\2\u00e6")
        buf.write(u"\u06ba\3\2\2\2\u00e8\u06bc\3\2\2\2\u00ea\u06cf\3\2\2")
        buf.write(u"\2\u00ec\u06d1\3\2\2\2\u00ee\u06d8\3\2\2\2\u00f0\u06df")
        buf.write(u"\3\2\2\2\u00f2\u06e8\3\2\2\2\u00f4\u06f1\3\2\2\2\u00f6")
        buf.write(u"\u06fa\3\2\2\2\u00f8\u0711\3\2\2\2\u00fa\u0722\3\2\2")
        buf.write(u"\2\u00fc\u0724\3\2\2\2\u00fe\u0730\3\2\2\2\u0100\u0732")
        buf.write(u"\3\2\2\2\u0102\u0734\3\2\2\2\u0104\u073a\3\2\2\2\u0106")
        buf.write(u"\u0741\3\2\2\2\u0108\u0744\3\2\2\2\u010a\u074d\3\2\2")
        buf.write(u"\2\u010c\u0755\3\2\2\2\u010e\u0761\3\2\2\2\u0110\u0769")
        buf.write(u"\3\2\2\2\u0112\u0776\3\2\2\2\u0114\u0778\3\2\2\2\u0116")
        buf.write(u"\u077c\3\2\2\2\u0118\u078a\3\2\2\2\u011a\u078c\3\2\2")
        buf.write(u"\2\u011c\u0791\3\2\2\2\u011e\u0796\3\2\2\2\u0120\u079e")
        buf.write(u"\3\2\2\2\u0122\u07af\3\2\2\2\u0124\u07b1\3\2\2\2\u0126")
        buf.write(u"\u07b3\3\2\2\2\u0128\u07b6\3\2\2\2\u012a\u07b9\3\2\2")
        buf.write(u"\2\u012c\u07bc\3\2\2\2\u012e\u07bf\3\2\2\2\u0130\u07c2")
        buf.write(u"\3\2\2\2\u0132\u07c4\3\2\2\2\u0134\u07c6\3\2\2\2\u0136")
        buf.write(u"\u07c8\3\2\2\2\u0138\u07ca\3\2\2\2\u013a\u07cc\3\2\2")
        buf.write(u"\2\u013c\u07ce\3\2\2\2\u013e\u07d0\3\2\2\2\u0140\u07d9")
        buf.write(u"\3\2\2\2\u0142\u07db\3\2\2\2\u0144\u07ec\3\2\2\2\u0146")
        buf.write(u"\u07ee\3\2\2\2\u0148\u07f0\3\2\2\2\u014a\u07f8\3\2\2")
        buf.write(u"\2\u014c\u07fa\3\2\2\2\u014e\u0801\3\2\2\2\u0150\u080c")
        buf.write(u"\3\2\2\2\u0152\u0810\3\2\2\2\u0154\u0814\3\2\2\2\u0156")
        buf.write(u"\u081b\3\2\2\2\u0158\u081d\3\2\2\2\u015a\u0822\3\2\2")
        buf.write(u"\2\u015c\u0824\3\2\2\2\u015e\u0833\3\2\2\2\u0160\u0835")
        buf.write(u"\3\2\2\2\u0162\u083d\3\2\2\2\u0164\u083f\3\2\2\2\u0166")
        buf.write(u"\u084c\3\2\2\2\u0168\u084e\3\2\2\2\u016a\u0859\3\2\2")
        buf.write(u"\2\u016c\u0869\3\2\2\2\u016e\u0870\3\2\2\2\u0170\u087f")
        buf.write(u"\3\2\2\2\u0172\u0881\3\2\2\2\u0174\u088a\3\2\2\2\u0176")
        buf.write(u"\u088c\3\2\2\2\u0178\u089b\3\2\2\2\u017a\u089d\3\2\2")
        buf.write(u"\2\u017c\u089f\3\2\2\2\u017e\u08a5\3\2\2\2\u0180\u08a7")
        buf.write(u"\3\2\2\2\u0182\u08ae\3\2\2\2\u0184\u08b9\3\2\2\2\u0186")
        buf.write(u"\u08bd\3\2\2\2\u0188\u08c1\3\2\2\2\u018a\u08cc\3\2\2")
        buf.write(u"\2\u018c\u08db\3\2\2\2\u018e\u08dd\3\2\2\2\u0190\u08e6")
        buf.write(u"\3\2\2\2\u0192\u08e8\3\2\2\2\u0194\u08f7\3\2\2\2\u0196")
        buf.write(u"\u08f9\3\2\2\2\u0198\u08fb\3\2\2\2\u019a\u0901\3\2\2")
        buf.write(u"\2\u019c\u0903\3\2\2\2\u019e\u090a\3\2\2\2\u01a0\u0915")
        buf.write(u"\3\2\2\2\u01a2\u0919\3\2\2\2\u01a4\u0920\3\2\2\2\u01a6")
        buf.write(u"\u092f\3\2\2\2\u01a8\u0931\3\2\2\2\u01aa\u0935\3\2\2")
        buf.write(u"\2\u01ac\u093e\3\2\2\2\u01ae\u0940\3\2\2\2\u01b0\u0949")
        buf.write(u"\3\2\2\2\u01b2\u094b\3\2\2\2\u01b4\u094f\3\2\2\2\u01b6")
        buf.write(u"\u095a\3\2\2\2\u01b8\u0964\3\2\2\2\u01ba\u0969\3\2\2")
        buf.write(u"\2\u01bc\u0971\3\2\2\2\u01be\u0978\3\2\2\2\u01c0\u097c")
        buf.write(u"\3\2\2\2\u01c2\u0981\3\2\2\2\u01c4\u0983\3\2\2\2\u01c6")
        buf.write(u"\u098d\3\2\2\2\u01c8\u0990\3\2\2\2\u01ca\u099b\3\2\2")
        buf.write(u"\2\u01cc\u099e\3\2\2\2\u01ce\u01cf\7`\2\2\u01cf\u01d0")
        buf.write(u"\7R\2\2\u01d0\u01d5\5\u00bc_\2\u01d1\u01d2\7\22\2\2\u01d2")
        buf.write(u"\u01d3\5\u00e2r\2\u01d3\u01d4\7\23\2\2\u01d4\u01d6\3")
        buf.write(u"\2\2\2\u01d5\u01d1\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write(u"\u01d9\3\2\2\2\u01d7\u01d8\7d\2\2\u01d8\u01da\5\u00bc")
        buf.write(u"_\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db")
        buf.write(u"\3\2\2\2\u01db\u01dc\7\26\2\2\u01dc\u01dd\5\u0094K\2")
        buf.write(u"\u01dd\u01de\7\27\2\2\u01de\3\3\2\2\2\u01df\u01e0\7`")
        buf.write(u"\2\2\u01e0\u01e1\5\u00bc_\2\u01e1\u01e2\7\22\2\2\u01e2")
        buf.write(u"\u01e3\5\u00a6T\2\u01e3\u01e4\7\23\2\2\u01e4\u01e5\7")
        buf.write(u"\26\2\2\u01e5\u01e6\5\u0092J\2\u01e6\u01e7\7\27\2\2\u01e7")
        buf.write(u"\5\3\2\2\2\u01e8\u01e9\5\u00be`\2\u01e9\u01ea\7\22\2")
        buf.write(u"\2\u01ea\u01eb\5|?\2\u01eb\u01ec\7\23\2\2\u01ec\u01ed")
        buf.write(u"\7\16\2\2\u01ed\7\3\2\2\2\u01ee\u01ef\5\u00be`\2\u01ef")
        buf.write(u"\u01f0\7)\2\2\u01f0\u01f1\5`\61\2\u01f1\u01f2\7\16\2")
        buf.write(u"\2\u01f2\t\3\2\2\2\u01f3\u01f5\7\u008f\2\2\u01f4\u01f3")
        buf.write(u"\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write(u"\u01f7\7K\2\2\u01f7\u01f8\5\u00ba^\2\u01f8\u01f9\7\r")
        buf.write(u"\2\2\u01f9\u01fb\5\u00a2R\2\u01fa\u01fc\5\u0098M\2\u01fb")
        buf.write(u"\u01fa\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u0205\3\2\2")
        buf.write(u"\2\u01fd\u01fe\7\u0099\2\2\u01fe\u0203\7o\2\2\u01ff\u0200")
        buf.write(u"\7\22\2\2\u0200\u0201\5\u00e0q\2\u0201\u0202\7\23\2\2")
        buf.write(u"\u0202\u0204\3\2\2\2\u0203\u01ff\3\2\2\2\u0203\u0204")
        buf.write(u"\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u01fd\3\2\2\2\u0205")
        buf.write(u"\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\7\16\2")
        buf.write(u"\2\u0208\13\3\2\2\2\u0209\u020a\7\u0098\2\2\u020a\u020d")
        buf.write(u"\5\u00bc_\2\u020b\u020c\7d\2\2\u020c\u020e\5\u00bc_\2")
        buf.write(u"\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f")
        buf.write(u"\3\2\2\2\u020f\u0210\5\24\13\2\u0210\r\3\2\2\2\u0211")
        buf.write(u"\u0213\7\u008f\2\2\u0212\u0211\3\2\2\2\u0212\u0213\3")
        buf.write(u"\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\7R\2\2\u0215\u021a")
        buf.write(u"\5\u00bc_\2\u0216\u0217\7\22\2\2\u0217\u0218\5\u00e2")
        buf.write(u"r\2\u0218\u0219\7\23\2\2\u0219\u021b\3\2\2\2\u021a\u0216")
        buf.write(u"\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021e\3\2\2\2\u021c")
        buf.write(u"\u021d\7d\2\2\u021d\u021f\5\22\n\2\u021e\u021c\3\2\2")
        buf.write(u"\2\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221")
        buf.write(u"\5\24\13\2\u0221\17\3\2\2\2\u0222\u0223\7\u008d\2\2\u0223")
        buf.write(u"\u0228\5\u00bc_\2\u0224\u0225\7\22\2\2\u0225\u0226\5")
        buf.write(u"\u00e2r\2\u0226\u0227\7\23\2\2\u0227\u0229\3\2\2\2\u0228")
        buf.write(u"\u0224\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022a\3\2\2")
        buf.write(u"\2\u022a\u022b\5\24\13\2\u022b\21\3\2\2\2\u022c\u022d")
        buf.write(u"\b\n\1\2\u022d\u022e\5\u00bc_\2\u022e\u0234\3\2\2\2\u022f")
        buf.write(u"\u0230\f\3\2\2\u0230\u0231\7\17\2\2\u0231\u0233\5\u00bc")
        buf.write(u"_\2\u0232\u022f\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232")
        buf.write(u"\3\2\2\2\u0234\u0235\3\2\2\2\u0235\23\3\2\2\2\u0236\u0234")
        buf.write(u"\3\2\2\2\u0237\u023e\7\16\2\2\u0238\u023a\7\26\2\2\u0239")
        buf.write(u"\u023b\5\u00ceh\2\u023a\u0239\3\2\2\2\u023a\u023b\3\2")
        buf.write(u"\2\2\u023b\u023c\3\2\2\2\u023c\u023e\7\27\2\2\u023d\u0237")
        buf.write(u"\3\2\2\2\u023d\u0238\3\2\2\2\u023e\25\3\2\2\2\u023f\u0241")
        buf.write(u"\5\u00a2R\2\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write(u"\u0242\3\2\2\2\u0242\u0243\7\177\2\2\u0243\u0244\5\u0122")
        buf.write(u"\u0092\2\u0244\u0245\7\22\2\2\u0245\u0246\5\u00c4c\2")
        buf.write(u"\u0246\u0247\7\23\2\2\u0247\u0249\7\26\2\2\u0248\u024a")
        buf.write(u"\5\u00f0y\2\u0249\u0248\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write(u"\u024b\3\2\2\2\u024b\u024c\7\27\2\2\u024c\27\3\2\2\2")
        buf.write(u"\u024d\u024e\7\u008c\2\2\u024e\u024f\5\u00b8]\2\u024f")
        buf.write(u"\u0251\7\26\2\2\u0250\u0252\5\u00f0y\2\u0251\u0250\3")
        buf.write(u"\2\2\2\u0251\u0252\3\2\2\2\u0252\u0253\3\2\2\2\u0253")
        buf.write(u"\u0254\7\27\2\2\u0254\31\3\2\2\2\u0255\u0257\7w\2\2\u0256")
        buf.write(u"\u0255\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\3\2\2")
        buf.write(u"\2\u0258\u0259\7\u008c\2\2\u0259\u025a\5\u00b8]\2\u025a")
        buf.write(u"\u025c\7\26\2\2\u025b\u025d\5\u00e8u\2\u025c\u025b\3")
        buf.write(u"\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write(u"\u025f\7\27\2\2\u025f\33\3\2\2\2\u0260\u0261\7k\2\2\u0261")
        buf.write(u"\u0262\5\u00b8]\2\u0262\u0264\7\26\2\2\u0263\u0265\5")
        buf.write(u"\u00f0y\2\u0264\u0263\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write(u"\u0266\3\2\2\2\u0266\u0267\7\27\2\2\u0267\35\3\2\2\2")
        buf.write(u"\u0268\u026a\7w\2\2\u0269\u0268\3\2\2\2\u0269\u026a\3")
        buf.write(u"\2\2\2\u026a\u026b\3\2\2\2\u026b\u026c\7k\2\2\u026c\u026d")
        buf.write(u"\5\u00b8]\2\u026d\u026f\7\26\2\2\u026e\u0270\5\u00e8")
        buf.write(u"u\2\u026f\u026e\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0271")
        buf.write(u"\3\2\2\2\u0271\u0272\7\27\2\2\u0272\37\3\2\2\2\u0273")
        buf.write(u"\u0275\7\u008f\2\2\u0274\u0273\3\2\2\2\u0274\u0275\3")
        buf.write(u"\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\7w\2\2\u0277\u0278")
        buf.write(u"\7\u0087\2\2\u0278\u027d\5\u00bc_\2\u0279\u027a\7\22")
        buf.write(u"\2\2\u027a\u027b\5\u00e2r\2\u027b\u027c\7\23\2\2\u027c")
        buf.write(u"\u027e\3\2\2\2\u027d\u0279\3\2\2\2\u027d\u027e\3\2\2")
        buf.write(u"\2\u027e\u027f\3\2\2\2\u027f\u0280\7\26\2\2\u0280\u0282")
        buf.write(u"\5$\23\2\u0281\u0283\5\u00d2j\2\u0282\u0281\3\2\2\2\u0282")
        buf.write(u"\u0283\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0285\7\27\2")
        buf.write(u"\2\u0285!\3\2\2\2\u0286\u0288\7\u008f\2\2\u0287\u0286")
        buf.write(u"\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u0289\3\2\2\2\u0289")
        buf.write(u"\u028a\7w\2\2\u028a\u028b\7R\2\2\u028b\u0290\5\u00bc")
        buf.write(u"_\2\u028c\u028d\7\22\2\2\u028d\u028e\5\u00e2r\2\u028e")
        buf.write(u"\u028f\7\23\2\2\u028f\u0291\3\2\2\2\u0290\u028c\3\2\2")
        buf.write(u"\2\u0290\u0291\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0293")
        buf.write(u"\7\26\2\2\u0293\u0295\5$\23\2\u0294\u0296\5\u00d2j\2")
        buf.write(u"\u0295\u0294\3\2\2\2\u0295\u0296\3\2\2\2\u0296\u0297")
        buf.write(u"\3\2\2\2\u0297\u0298\7\27\2\2\u0298#\3\2\2\2\u0299\u029a")
        buf.write(u"\7R\2\2\u029a\u029b\7M\2\2\u029b\u029c\7\26\2\2\u029c")
        buf.write(u"\u029d\5&\24\2\u029d\u029e\7\27\2\2\u029e%\3\2\2\2\u029f")
        buf.write(u"\u02a0\b\24\1\2\u02a0\u02a1\5\u00d6l\2\u02a1\u02a2\7")
        buf.write(u"\16\2\2\u02a2\u02a9\3\2\2\2\u02a3\u02a4\f\3\2\2\u02a4")
        buf.write(u"\u02a5\5\u00d6l\2\u02a5\u02a6\7\16\2\2\u02a6\u02a8\3")
        buf.write(u"\2\2\2\u02a7\u02a3\3\2\2\2\u02a8\u02ab\3\2\2\2\u02a9")
        buf.write(u"\u02a7\3\2\2\2\u02a9\u02aa\3\2\2\2\u02aa\'\3\2\2\2\u02ab")
        buf.write(u"\u02a9\3\2\2\2\u02ac\u02ae\7C\2\2\u02ad\u02af\5\u00a2")
        buf.write(u"R\2\u02ae\u02ad\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b0")
        buf.write(u"\3\2\2\2\u02b0\u02b1\7s\2\2\u02b1\u02b2\5\u00b4[\2\u02b2")
        buf.write(u"\u02b4\7\22\2\2\u02b3\u02b5\5\u00c0a\2\u02b4\u02b3\3")
        buf.write(u"\2\2\2\u02b4\u02b5\3\2\2\2\u02b5\u02b6\3\2\2\2\u02b6")
        buf.write(u"\u02b7\7\23\2\2\u02b7\u02b8\7\16\2\2\u02b8)\3\2\2\2\u02b9")
        buf.write(u"\u02bb\5\u00a2R\2\u02ba\u02b9\3\2\2\2\u02ba\u02bb\3\2")
        buf.write(u"\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd\7s\2\2\u02bd\u02be")
        buf.write(u"\5\u00b4[\2\u02be\u02c0\7\22\2\2\u02bf\u02c1\5\u00c0")
        buf.write(u"a\2\u02c0\u02bf\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2")
        buf.write(u"\3\2\2\2\u02c2\u02c3\7\23\2\2\u02c3\u02c5\7\26\2\2\u02c4")
        buf.write(u"\u02c6\5\u00f0y\2\u02c5\u02c4\3\2\2\2\u02c5\u02c6\3\2")
        buf.write(u"\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02c8\7\27\2\2\u02c8+")
        buf.write(u"\3\2\2\2\u02c9\u02cb\5\u00caf\2\u02ca\u02c9\3\2\2\2\u02ca")
        buf.write(u"\u02cb\3\2\2\2\u02cb\u02cd\3\2\2\2\u02cc\u02ce\7w\2\2")
        buf.write(u"\u02cd\u02cc\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02cf")
        buf.write(u"\3\2\2\2\u02cf\u02d0\7s\2\2\u02d0\u02d1\5\u00b4[\2\u02d1")
        buf.write(u"\u02d3\7\22\2\2\u02d2\u02d4\5\u00c0a\2\u02d3\u02d2\3")
        buf.write(u"\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5")
        buf.write(u"\u02d6\7\23\2\2\u02d6\u02d7\7\26\2\2\u02d7\u02d8\5\u00e8")
        buf.write(u"u\2\u02d8\u02d9\7\27\2\2\u02d9-\3\2\2\2\u02da\u02db\7")
        buf.write(u"\u0092\2\2\u02db\u02dc\7s\2\2\u02dc\u02dd\7\u00a7\2\2")
        buf.write(u"\u02dd\u02de\7\22\2\2\u02de\u02df\7\23\2\2\u02df\u02e0")
        buf.write(u"\7\26\2\2\u02e0\u02e1\5\u00f0y\2\u02e1\u02e2\7\27\2\2")
        buf.write(u"\u02e2\u02ea\7\u0097\2\2\u02e3\u02e4\7\26\2\2\u02e4\u02e5")
        buf.write(u"\5\u00f2z\2\u02e5\u02e6\7\27\2\2\u02e6\u02eb\3\2\2\2")
        buf.write(u"\u02e7\u02e8\5\u00be`\2\u02e8\u02e9\7\16\2\2\u02e9\u02eb")
        buf.write(u"\3\2\2\2\u02ea\u02e3\3\2\2\2\u02ea\u02e7\3\2\2\2\u02eb")
        buf.write(u"/\3\2\2\2\u02ec\u02ed\5`\61\2\u02ed\u02ee\7\16\2\2\u02ee")
        buf.write(u"\61\3\2\2\2\u02ef\u02f4\5\u00caf\2\u02f0\u02f1\7\22\2")
        buf.write(u"\2\u02f1\u02f2\5\u00e2r\2\u02f2\u02f3\7\23\2\2\u02f3")
        buf.write(u"\u02f5\3\2\2\2\u02f4\u02f0\3\2\2\2\u02f4\u02f5\3\2\2")
        buf.write(u"\2\u02f5\u02f6\3\2\2\2\u02f6\u02f9\5\u00b8]\2\u02f7\u02f8")
        buf.write(u"\7)\2\2\u02f8\u02fa\5\u0104\u0083\2\u02f9\u02f7\3\2\2")
        buf.write(u"\2\u02f9\u02fa\3\2\2\2\u02fa\63\3\2\2\2\u02fb\u0303\5")
        buf.write(u"\66\34\2\u02fc\u0300\7\26\2\2\u02fd\u02fe\5\u00f0y\2")
        buf.write(u"\u02fe\u02ff\7\27\2\2\u02ff\u0301\3\2\2\2\u0300\u02fd")
        buf.write(u"\3\2\2\2\u0300\u0301\3\2\2\2\u0301\u0303\3\2\2\2\u0302")
        buf.write(u"\u02fb\3\2\2\2\u0302\u02fc\3\2\2\2\u0303\65\3\2\2\2\u0304")
        buf.write(u"\u0305\5X-\2\u0305\u0306\7\16\2\2\u0306\u031a\3\2\2\2")
        buf.write(u"\u0307\u031a\5\u0080A\2\u0308\u031a\5\u0084C\2\u0309")
        buf.write(u"\u031a\5:\36\2\u030a\u031a\58\35\2\u030b\u031a\5T+\2")
        buf.write(u"\u030c\u031a\5V,\2\u030d\u031a\5J&\2\u030e\u031a\5@!")
        buf.write(u"\2\u030f\u031a\5D#\2\u0310\u031a\5H%\2\u0311\u031a\5")
        buf.write(u"F$\2\u0312\u031a\5P)\2\u0313\u031a\5N(\2\u0314\u031a")
        buf.write(u"\5n8\2\u0315\u031a\5<\37\2\u0316\u031a\5> \2\u0317\u031a")
        buf.write(u"\5*\26\2\u0318\u031a\5\u00e6t\2\u0319\u0304\3\2\2\2\u0319")
        buf.write(u"\u0307\3\2\2\2\u0319\u0308\3\2\2\2\u0319\u0309\3\2\2")
        buf.write(u"\2\u0319\u030a\3\2\2\2\u0319\u030b\3\2\2\2\u0319\u030c")
        buf.write(u"\3\2\2\2\u0319\u030d\3\2\2\2\u0319\u030e\3\2\2\2\u0319")
        buf.write(u"\u030f\3\2\2\2\u0319\u0310\3\2\2\2\u0319\u0311\3\2\2")
        buf.write(u"\2\u0319\u0312\3\2\2\2\u0319\u0313\3\2\2\2\u0319\u0314")
        buf.write(u"\3\2\2\2\u0319\u0315\3\2\2\2\u0319\u0316\3\2\2\2\u0319")
        buf.write(u"\u0317\3\2\2\2\u0319\u0318\3\2\2\2\u031a\67\3\2\2\2\u031b")
        buf.write(u"\u031c\7h\2\2\u031c\u031d\7\22\2\2\u031d\u031e\7\23\2")
        buf.write(u"\2\u031e\u031f\7\16\2\2\u031f9\3\2\2\2\u0320\u0321\7")
        buf.write(u"Y\2\2\u0321\u0322\7\22\2\2\u0322\u0323\5\u009eP\2\u0323")
        buf.write(u"\u0324\7\23\2\2\u0324\u0325\7\16\2\2\u0325\u0338\3\2")
        buf.write(u"\2\2\u0326\u0327\7\u0090\2\2\u0327\u0328\7\22\2\2\u0328")
        buf.write(u"\u0329\5\u009eP\2\u0329\u032a\7\23\2\2\u032a\u032b\7")
        buf.write(u"\16\2\2\u032b\u0338\3\2\2\2\u032c\u032d\7Y\2\2\u032d")
        buf.write(u"\u032e\7\22\2\2\u032e\u032f\5\u009eP\2\u032f\u0330\7")
        buf.write(u"\23\2\2\u0330\u0331\7F\2\2\u0331\u0332\7\u0090\2\2\u0332")
        buf.write(u"\u0333\7\22\2\2\u0333\u0334\5\u009eP\2\u0334\u0335\7")
        buf.write(u"\23\2\2\u0335\u0336\7\16\2\2\u0336\u0338\3\2\2\2\u0337")
        buf.write(u"\u0320\3\2\2\2\u0337\u0326\3\2\2\2\u0337\u032c\3\2\2")
        buf.write(u"\2\u0338;\3\2\2\2\u0339\u033a\7\u0099\2\2\u033a\u033b")
        buf.write(u"\7\22\2\2\u033b\u033c\5\u0114\u008b\2\u033c\u033d\7\23")
        buf.write(u"\2\2\u033d\u033e\5\64\33\2\u033e=\3\2\2\2\u033f\u0340")
        buf.write(u"\7\u0099\2\2\u0340\u0341\7\22\2\2\u0341\u0342\5\u00bc")
        buf.write(u"_\2\u0342\u0343\7\23\2\2\u0343\u0344\5\64\33\2\u0344")
        buf.write(u"?\3\2\2\2\u0345\u0346\7\u0091\2\2\u0346\u0347\7\22\2")
        buf.write(u"\2\u0347\u0348\5`\61\2\u0348\u0349\7\23\2\2\u0349\u034a")
        buf.write(u"\7\26\2\2\u034a\u0350\5\u00f4{\2\u034b\u034c\7W\2\2\u034c")
        buf.write(u"\u034e\7\r\2\2\u034d\u034f\5\u00f0y\2\u034e\u034d\3\2")
        buf.write(u"\2\2\u034e\u034f\3\2\2\2\u034f\u0351\3\2\2\2\u0350\u034b")
        buf.write(u"\3\2\2\2\u0350\u0351\3\2\2\2\u0351\u0352\3\2\2\2\u0352")
        buf.write(u"\u0353\7\27\2\2\u0353A\3\2\2\2\u0354\u0355\7P\2\2\u0355")
        buf.write(u"\u0356\5\u00fa~\2\u0356\u0358\7\r\2\2\u0357\u0359\5\u00f0")
        buf.write(u"y\2\u0358\u0357\3\2\2\2\u0358\u0359\3\2\2\2\u0359\u0362")
        buf.write(u"\3\2\2\2\u035a\u035b\7P\2\2\u035b\u035c\7n\2\2\u035c")
        buf.write(u"\u035d\5\u00f8}\2\u035d\u035f\7\r\2\2\u035e\u0360\5\u00f0")
        buf.write(u"y\2\u035f\u035e\3\2\2\2\u035f\u0360\3\2\2\2\u0360\u0362")
        buf.write(u"\3\2\2\2\u0361\u0354\3\2\2\2\u0361\u035a\3\2\2\2\u0362")
        buf.write(u"C\3\2\2\2\u0363\u0364\7i\2\2\u0364\u0365\7]\2\2\u0365")
        buf.write(u"\u0366\7\22\2\2\u0366\u0369\5\u00b8]\2\u0367\u0368\7")
        buf.write(u"\17\2\2\u0368\u036a\5\u00b8]\2\u0369\u0367\3\2\2\2\u0369")
        buf.write(u"\u036a\3\2\2\2\u036a\u036b\3\2\2\2\u036b\u036c\7n\2\2")
        buf.write(u"\u036c\u036d\5`\61\2\u036d\u036e\7\23\2\2\u036e\u036f")
        buf.write(u"\5\64\33\2\u036fE\3\2\2\2\u0370\u0371\7[\2\2\u0371\u0373")
        buf.write(u"\7\26\2\2\u0372\u0374\5\u00f0y\2\u0373\u0372\3\2\2\2")
        buf.write(u"\u0373\u0374\3\2\2\2\u0374\u0375\3\2\2\2\u0375\u0376")
        buf.write(u"\7\27\2\2\u0376\u0377\7\u009c\2\2\u0377\u0378\7\22\2")
        buf.write(u"\2\u0378\u0379\5`\61\2\u0379\u037a\7\23\2\2\u037a\u037b")
        buf.write(u"\7\16\2\2\u037bG\3\2\2\2\u037c\u037d\7\u009c\2\2\u037d")
        buf.write(u"\u037e\7\22\2\2\u037e\u037f\5`\61\2\u037f\u0380\7\23")
        buf.write(u"\2\2\u0380\u0381\5\64\33\2\u0381I\3\2\2\2\u0382\u0383")
        buf.write(u"\7m\2\2\u0383\u0384\7\22\2\2\u0384\u0385\5`\61\2\u0385")
        buf.write(u"\u0386\7\23\2\2\u0386\u0388\5\64\33\2\u0387\u0389\5L")
        buf.write(u"\'\2\u0388\u0387\3\2\2\2\u0388\u0389\3\2\2\2\u0389\u038c")
        buf.write(u"\3\2\2\2\u038a\u038b\7^\2\2\u038b\u038d\5\64\33\2\u038c")
        buf.write(u"\u038a\3\2\2\2\u038c\u038d\3\2\2\2\u038dK\3\2\2\2\u038e")
        buf.write(u"\u038f\b\'\1\2\u038f\u0390\7^\2\2\u0390\u0391\7m\2\2")
        buf.write(u"\u0391\u0392\7\22\2\2\u0392\u0393\5`\61\2\u0393\u0394")
        buf.write(u"\7\23\2\2\u0394\u0395\5\64\33\2\u0395\u03a0\3\2\2\2\u0396")
        buf.write(u"\u0397\f\3\2\2\u0397\u0398\7^\2\2\u0398\u0399\7m\2\2")
        buf.write(u"\u0399\u039a\7\22\2\2\u039a\u039b\5`\61\2\u039b\u039c")
        buf.write(u"\7\23\2\2\u039c\u039d\5\64\33\2\u039d\u039f\3\2\2\2\u039e")
        buf.write(u"\u0396\3\2\2\2\u039f\u03a2\3\2\2\2\u03a0\u039e\3\2\2")
        buf.write(u"\2\u03a0\u03a1\3\2\2\2\u03a1M\3\2\2\2\u03a2\u03a0\3\2")
        buf.write(u"\2\2\u03a3\u03a4\7\u0094\2\2\u03a4\u03a5\5`\61\2\u03a5")
        buf.write(u"\u03a6\7\16\2\2\u03a6O\3\2\2\2\u03a7\u03a8\7\u0096\2")
        buf.write(u"\2\u03a8\u03a9\7\22\2\2\u03a9\u03aa\5\u00b8]\2\u03aa")
        buf.write(u"\u03ab\7\23\2\2\u03ab\u03ad\7\26\2\2\u03ac\u03ae\5\u00f0")
        buf.write(u"y\2\u03ad\u03ac\3\2\2\2\u03ad\u03ae\3\2\2\2\u03ae\u03af")
        buf.write(u"\3\2\2\2\u03af\u03b1\7\27\2\2\u03b0\u03b2\5\u00f6|\2")
        buf.write(u"\u03b1\u03b0\3\2\2\2\u03b1\u03b2\3\2\2\2\u03b2\u03bc")
        buf.write(u"\3\2\2\2\u03b3\u03b4\7Q\2\2\u03b4\u03b5\7\22\2\2\u03b5")
        buf.write(u"\u03b6\7G\2\2\u03b6\u03b7\7\23\2\2\u03b7\u03b9\7\26\2")
        buf.write(u"\2\u03b8\u03ba\5\u00f0y\2\u03b9\u03b8\3\2\2\2\u03b9\u03ba")
        buf.write(u"\3\2\2\2\u03ba\u03bb\3\2\2\2\u03bb\u03bd\7\27\2\2\u03bc")
        buf.write(u"\u03b3\3\2\2\2\u03bc\u03bd\3\2\2\2\u03bd\u03c4\3\2\2")
        buf.write(u"\2\u03be\u03bf\7g\2\2\u03bf\u03c1\7\26\2\2\u03c0\u03c2")
        buf.write(u"\5\u00f0y\2\u03c1\u03c0\3\2\2\2\u03c1\u03c2\3\2\2\2\u03c2")
        buf.write(u"\u03c3\3\2\2\2\u03c3\u03c5\7\27\2\2\u03c4\u03be\3\2\2")
        buf.write(u"\2\u03c4\u03c5\3\2\2\2\u03c5Q\3\2\2\2\u03c6\u03c7\7Q")
        buf.write(u"\2\2\u03c7\u03c8\7\22\2\2\u03c8\u03c9\5\u00be`\2\u03c9")
        buf.write(u"\u03ca\7\23\2\2\u03ca\u03cc\7\26\2\2\u03cb\u03cd\5\u00f0")
        buf.write(u"y\2\u03cc\u03cb\3\2\2\2\u03cc\u03cd\3\2\2\2\u03cd\u03ce")
        buf.write(u"\3\2\2\2\u03ce\u03cf\7\27\2\2\u03cf\u03dc\3\2\2\2\u03d0")
        buf.write(u"\u03d1\7Q\2\2\u03d1\u03d2\7n\2\2\u03d2\u03d3\7\22\2\2")
        buf.write(u"\u03d3\u03d4\5\u0096L\2\u03d4\u03d5\7\23\2\2\u03d5\u03d7")
        buf.write(u"\7\26\2\2\u03d6\u03d8\5\u00f0y\2\u03d7\u03d6\3\2\2\2")
        buf.write(u"\u03d7\u03d8\3\2\2\2\u03d8\u03d9\3\2\2\2\u03d9\u03da")
        buf.write(u"\7\27\2\2\u03da\u03dc\3\2\2\2\u03db\u03c6\3\2\2\2\u03db")
        buf.write(u"\u03d0\3\2\2\2\u03dcS\3\2\2\2\u03dd\u03de\7N\2\2\u03de")
        buf.write(u"\u03df\7\16\2\2\u03dfU\3\2\2\2\u03e0\u03e2\7\u0088\2")
        buf.write(u"\2\u03e1\u03e3\5`\61\2\u03e2\u03e1\3\2\2\2\u03e2\u03e3")
        buf.write(u"\3\2\2\2\u03e3\u03e4\3\2\2\2\u03e4\u03e5\7\16\2\2\u03e5")
        buf.write(u"W\3\2\2\2\u03e6\u03e7\5Z.\2\u03e7\u03e9\7\22\2\2\u03e8")
        buf.write(u"\u03ea\5|?\2\u03e9\u03e8\3\2\2\2\u03e9\u03ea\3\2\2\2")
        buf.write(u"\u03ea\u03eb\3\2\2\2\u03eb\u03ec\7\23\2\2\u03ecY\3\2")
        buf.write(u"\2\2\u03ed\u03f3\5\u00b4[\2\u03ee\u03ef\5\\/\2\u03ef")
        buf.write(u"\u03f0\7\21\2\2\u03f0\u03f1\5\u00b4[\2\u03f1\u03f3\3")
        buf.write(u"\2\2\2\u03f2\u03ed\3\2\2\2\u03f2\u03ee\3\2\2\2\u03f3")
        buf.write(u"[\3\2\2\2\u03f4\u03f5\b/\1\2\u03f5\u03f6\5\u00b6\\\2")
        buf.write(u"\u03f6\u03fb\3\2\2\2\u03f7\u03f8\f\3\2\2\u03f8\u03fa")
        buf.write(u"\5^\60\2\u03f9\u03f7\3\2\2\2\u03fa\u03fd\3\2\2\2\u03fb")
        buf.write(u"\u03f9\3\2\2\2\u03fb\u03fc\3\2\2\2\u03fc]\3\2\2\2\u03fd")
        buf.write(u"\u03fb\3\2\2\2\u03fe\u03ff\7\21\2\2\u03ff\u0405\5\u00b8")
        buf.write(u"]\2\u0400\u0401\7\24\2\2\u0401\u0402\5`\61\2\u0402\u0403")
        buf.write(u"\7\25\2\2\u0403\u0405\3\2\2\2\u0404\u03fe\3\2\2\2\u0404")
        buf.write(u"\u0400\3\2\2\2\u0405_\3\2\2\2\u0406\u0407\b\61\1\2\u0407")
        buf.write(u"\u041f\5\u01aa\u00d6\2\u0408\u041f\5f\64\2\u0409\u041f")
        buf.write(u"\5h\65\2\u040a\u040b\7\37\2\2\u040b\u041f\5`\61&\u040c")
        buf.write(u"\u040d\7\31\2\2\u040d\u041f\5`\61%\u040e\u040f\7\22\2")
        buf.write(u"\2\u040f\u0410\5\u00caf\2\u0410\u0411\7\23\2\2\u0411")
        buf.write(u"\u0412\5`\61\37\u0412\u041f\3\2\2\2\u0413\u0414\7;\2")
        buf.write(u"\2\u0414\u0415\7\22\2\2\u0415\u0416\5`\61\2\u0416\u0417")
        buf.write(u"\7\23\2\2\u0417\u041f\3\2\2\2\u0418\u0419\7b\2\2\u0419")
        buf.write(u"\u041a\7\22\2\2\u041a\u041b\5\u00b8]\2\u041b\u041c\7")
        buf.write(u"\23\2\2\u041c\u041f\3\2\2\2\u041d\u041f\5d\63\2\u041e")
        buf.write(u"\u0406\3\2\2\2\u041e\u0408\3\2\2\2\u041e\u0409\3\2\2")
        buf.write(u"\2\u041e\u040a\3\2\2\2\u041e\u040c\3\2\2\2\u041e\u040e")
        buf.write(u"\3\2\2\2\u041e\u0413\3\2\2\2\u041e\u0418\3\2\2\2\u041e")
        buf.write(u"\u041d\3\2\2\2\u041f\u0494\3\2\2\2\u0420\u0421\f$\2\2")
        buf.write(u"\u0421\u0422\5\u0132\u009a\2\u0422\u0423\5`\61%\u0423")
        buf.write(u"\u0493\3\2\2\2\u0424\u0425\f#\2\2\u0425\u0426\5\u0134")
        buf.write(u"\u009b\2\u0426\u0427\5`\61$\u0427\u0493\3\2\2\2\u0428")
        buf.write(u"\u0429\f\"\2\2\u0429\u042a\5\u0138\u009d\2\u042a\u042b")
        buf.write(u"\5`\61#\u042b\u0493\3\2\2\2\u042c\u042d\f!\2\2\u042d")
        buf.write(u"\u042e\5\u0136\u009c\2\u042e\u042f\5`\61\"\u042f\u0493")
        buf.write(u"\3\2\2\2\u0430\u0431\f \2\2\u0431\u0432\t\2\2\2\u0432")
        buf.write(u"\u0493\5`\61!\u0433\u0434\f\36\2\2\u0434\u0435\7&\2\2")
        buf.write(u"\u0435\u0493\5`\61\37\u0436\u0437\f\35\2\2\u0437\u0438")
        buf.write(u"\7\'\2\2\u0438\u0493\5`\61\36\u0439\u043a\f\34\2\2\u043a")
        buf.write(u"\u043b\7$\2\2\u043b\u0493\5`\61\35\u043c\u043d\f\33\2")
        buf.write(u"\2\u043d\u043e\7%\2\2\u043e\u0493\5`\61\34\u043f\u0440")
        buf.write(u"\f\30\2\2\u0440\u0441\7q\2\2\u0441\u0442\7y\2\2\u0442")
        buf.write(u"\u0493\5`\61\31\u0443\u0444\f\27\2\2\u0444\u0445\7q\2")
        buf.write(u"\2\u0445\u0493\5`\61\30\u0446\u0447\f\26\2\2\u0447\u0448")
        buf.write(u"\7+\2\2\u0448\u0493\5`\61\27\u0449\u044a\f\25\2\2\u044a")
        buf.write(u"\u044b\7*\2\2\u044b\u0493\5`\61\26\u044c\u044d\f\24\2")
        buf.write(u"\2\u044d\u044e\7,\2\2\u044e\u0493\5`\61\25\u044f\u0450")
        buf.write(u"\f\23\2\2\u0450\u0451\7U\2\2\u0451\u0493\5`\61\24\u0452")
        buf.write(u"\u0453\f\22\2\2\u0453\u0454\7n\2\2\u0454\u0493\5`\61")
        buf.write(u"\23\u0455\u0456\f\21\2\2\u0456\u0457\7l\2\2\u0457\u0493")
        buf.write(u"\5`\61\22\u0458\u0459\f\20\2\2\u0459\u045a\7l\2\2\u045a")
        buf.write(u"\u045b\7D\2\2\u045b\u0493\5`\61\21\u045c\u045d\f\17\2")
        buf.write(u"\2\u045d\u045e\7l\2\2\u045e\u045f\7G\2\2\u045f\u0493")
        buf.write(u"\5`\61\20\u0460\u0461\f\16\2\2\u0461\u0462\7y\2\2\u0462")
        buf.write(u"\u0463\7U\2\2\u0463\u0493\5`\61\17\u0464\u0465\f\r\2")
        buf.write(u"\2\u0465\u0466\7y\2\2\u0466\u0467\7n\2\2\u0467\u0493")
        buf.write(u"\5`\61\16\u0468\u0469\f\f\2\2\u0469\u046a\7y\2\2\u046a")
        buf.write(u"\u046b\7l\2\2\u046b\u0493\5`\61\r\u046c\u046d\f\13\2")
        buf.write(u"\2\u046d\u046e\7y\2\2\u046e\u046f\7l\2\2\u046f\u0470")
        buf.write(u"\7D\2\2\u0470\u0493\5`\61\f\u0471\u0472\f\n\2\2\u0472")
        buf.write(u"\u0473\7y\2\2\u0473\u0474\7l\2\2\u0474\u0475\7G\2\2\u0475")
        buf.write(u"\u0493\5`\61\13\u0476\u0477\f\t\2\2\u0477\u0478\7\35")
        buf.write(u"\2\2\u0478\u0493\5`\61\n\u0479\u047a\f\b\2\2\u047a\u047b")
        buf.write(u"\7\33\2\2\u047b\u0493\5`\61\t\u047c\u047d\f\7\2\2\u047d")
        buf.write(u"\u047e\7\30\2\2\u047e\u047f\5`\61\2\u047f\u0480\7\r\2")
        buf.write(u"\2\u0480\u0481\5`\61\b\u0481\u0493\3\2\2\2\u0482\u0483")
        buf.write(u"\f\32\2\2\u0483\u0484\7q\2\2\u0484\u0485\7y\2\2\u0485")
        buf.write(u"\u0493\5b\62\2\u0486\u0487\f\31\2\2\u0487\u0488\7q\2")
        buf.write(u"\2\u0488\u0493\5b\62\2\u0489\u048a\f\3\2\2\u048a\u048b")
        buf.write(u"\7i\2\2\u048b\u048c\7]\2\2\u048c\u048d\7\22\2\2\u048d")
        buf.write(u"\u048e\5\u00b8]\2\u048e\u048f\7n\2\2\u048f\u0490\5`\61")
        buf.write(u"\2\u0490\u0491\7\23\2\2\u0491\u0493\3\2\2\2\u0492\u0420")
        buf.write(u"\3\2\2\2\u0492\u0424\3\2\2\2\u0492\u0428\3\2\2\2\u0492")
        buf.write(u"\u042c\3\2\2\2\u0492\u0430\3\2\2\2\u0492\u0433\3\2\2")
        buf.write(u"\2\u0492\u0436\3\2\2\2\u0492\u0439\3\2\2\2\u0492\u043c")
        buf.write(u"\3\2\2\2\u0492\u043f\3\2\2\2\u0492\u0443\3\2\2\2\u0492")
        buf.write(u"\u0446\3\2\2\2\u0492\u0449\3\2\2\2\u0492\u044c\3\2\2")
        buf.write(u"\2\u0492\u044f\3\2\2\2\u0492\u0452\3\2\2\2\u0492\u0455")
        buf.write(u"\3\2\2\2\u0492\u0458\3\2\2\2\u0492\u045c\3\2\2\2\u0492")
        buf.write(u"\u0460\3\2\2\2\u0492\u0464\3\2\2\2\u0492\u0468\3\2\2")
        buf.write(u"\2\u0492\u046c\3\2\2\2\u0492\u0471\3\2\2\2\u0492\u0476")
        buf.write(u"\3\2\2\2\u0492\u0479\3\2\2\2\u0492\u047c\3\2\2\2\u0492")
        buf.write(u"\u0482\3\2\2\2\u0492\u0486\3\2\2\2\u0492\u0489\3\2\2")
        buf.write(u"\2\u0493\u0496\3\2\2\2\u0494\u0492\3\2\2\2\u0494\u0495")
        buf.write(u"\3\2\2\2\u0495a\3\2\2\2\u0496\u0494\3\2\2\2\u0497\u0498")
        buf.write(u"\6\62$\3\u0498\u0499\7\u00a4\2\2\u0499\u049a\5\u00ca")
        buf.write(u"f\2\u049ac\3\2\2\2\u049b\u049c\5\u00bc_\2\u049ce\3\2")
        buf.write(u"\2\2\u049d\u049e\b\64\1\2\u049e\u049f\5\u00fe\u0080\2")
        buf.write(u"\u049f\u04a4\3\2\2\2\u04a0\u04a1\f\3\2\2\u04a1\u04a3")
        buf.write(u"\5v<\2\u04a2\u04a0\3\2\2\2\u04a3\u04a6\3\2\2\2\u04a4")
        buf.write(u"\u04a2\3\2\2\2\u04a4\u04a5\3\2\2\2\u04a5g\3\2\2\2\u04a6")
        buf.write(u"\u04a4\3\2\2\2\u04a7\u04b1\5j\66\2\u04a8\u04b1\5l\67")
        buf.write(u"\2\u04a9\u04b1\5p9\2\u04aa\u04b1\5r:\2\u04ab\u04b1\5")
        buf.write(u"\u011a\u008e\2\u04ac\u04b1\5\u011c\u008f\2\u04ad\u04b1")
        buf.write(u"\5t;\2\u04ae\u04b1\5X-\2\u04af\u04b1\5x=\2\u04b0\u04a7")
        buf.write(u"\3\2\2\2\u04b0\u04a8\3\2\2\2\u04b0\u04a9\3\2\2\2\u04b0")
        buf.write(u"\u04aa\3\2\2\2\u04b0\u04ab\3\2\2\2\u04b0\u04ac\3\2\2")
        buf.write(u"\2\u04b0\u04ad\3\2\2\2\u04b0\u04ae\3\2\2\2\u04b0\u04af")
        buf.write(u"\3\2\2\2\u04b1i\3\2\2\2\u04b2\u04b3\7=\2\2\u04b3\u04b4")
        buf.write(u"\7\22\2\2\u04b4\u04b5\5`\61\2\u04b5\u04b6\7\23\2\2\u04b6")
        buf.write(u"k\3\2\2\2\u04b7\u04b8\7<\2\2\u04b8\u04ba\7\22\2\2\u04b9")
        buf.write(u"\u04bb\5`\61\2\u04ba\u04b9\3\2\2\2\u04ba\u04bb\3\2\2")
        buf.write(u"\2\u04bb\u04bc\3\2\2\2\u04bc\u04bd\7\23\2\2\u04bdm\3")
        buf.write(u"\2\2\2\u04be\u04bf\7\u009d\2\2\u04bf\u04c0\7\22\2\2\u04c0")
        buf.write(u"\u04c1\5`\61\2\u04c1\u04c2\7\23\2\2\u04c2\u04c3\7\u0095")
        buf.write(u"\2\2\u04c3\u04c4\5`\61\2\u04c4\u04c5\7\16\2\2\u04c5o")
        buf.write(u"\3\2\2\2\u04c6\u04c7\7f\2\2\u04c7\u04c8\7\22\2\2\u04c8")
        buf.write(u"\u04c9\5`\61\2\u04c9\u04ca\7\23\2\2\u04ca\u04cb\7\u0099")
        buf.write(u"\2\2\u04cb\u04cc\7\22\2\2\u04cc\u04cd\5\u00b8]\2\u04cd")
        buf.write(u"\u04ce\7\23\2\2\u04ce\u04cf\7\u009b\2\2\u04cf\u04d0\7")
        buf.write(u"\22\2\2\u04d0\u04d1\5`\61\2\u04d1\u04d2\7\23\2\2\u04d2")
        buf.write(u"q\3\2\2\2\u04d3\u04d4\7e\2\2\u04d4\u04d9\7}\2\2\u04d5")
        buf.write(u"\u04d6\7\22\2\2\u04d6\u04d7\5\u00aaV\2\u04d7\u04d8\7")
        buf.write(u"\23\2\2\u04d8\u04da\3\2\2\2\u04d9\u04d5\3\2\2\2\u04d9")
        buf.write(u"\u04da\3\2\2\2\u04da\u04db\3\2\2\2\u04db\u04dc\7\u009b")
        buf.write(u"\2\2\u04dc\u04dd\7\22\2\2\u04dd\u04de\5`\61\2\u04de\u04df")
        buf.write(u"\7\23\2\2\u04df\u0507\3\2\2\2\u04e0\u04f5\7e\2\2\u04e1")
        buf.write(u"\u04e6\7D\2\2\u04e2\u04e3\7\22\2\2\u04e3\u04e4\5\u00aa")
        buf.write(u"V\2\u04e4\u04e5\7\23\2\2\u04e5\u04e7\3\2\2\2\u04e6\u04e2")
        buf.write(u"\3\2\2\2\u04e6\u04e7\3\2\2\2\u04e7\u04f6\3\2\2\2\u04e8")
        buf.write(u"\u04e9\7\22\2\2\u04e9\u04ea\5\u00aaV\2\u04ea\u04eb\7")
        buf.write(u"\23\2\2\u04eb\u04ed\3\2\2\2\u04ec\u04e8\3\2\2\2\u04ec")
        buf.write(u"\u04ed\3\2\2\2\u04ed\u04ee\3\2\2\2\u04ee\u04ef\7\u008a")
        buf.write(u"\2\2\u04ef\u04f0\7\22\2\2\u04f0\u04f1\5`\61\2\u04f1\u04f2")
        buf.write(u"\7\u0095\2\2\u04f2\u04f3\5`\61\2\u04f3\u04f4\7\23\2\2")
        buf.write(u"\u04f4\u04f6\3\2\2\2\u04f5\u04e1\3\2\2\2\u04f5\u04ec")
        buf.write(u"\3\2\2\2\u04f6\u04fc\3\2\2\2\u04f7\u04f8\7\u009b\2\2")
        buf.write(u"\u04f8\u04f9\7\22\2\2\u04f9\u04fa\5`\61\2\u04fa\u04fb")
        buf.write(u"\7\23\2\2\u04fb\u04fd\3\2\2\2\u04fc\u04f7\3\2\2\2\u04fc")
        buf.write(u"\u04fd\3\2\2\2\u04fd\u0504\3\2\2\2\u04fe\u04ff\7\u0081")
        buf.write(u"\2\2\u04ff\u0500\7O\2\2\u0500\u0501\7\22\2\2\u0501\u0502")
        buf.write(u"\5\u011e\u0090\2\u0502\u0503\7\23\2\2\u0503\u0505\3\2")
        buf.write(u"\2\2\u0504\u04fe\3\2\2\2\u0504\u0505\3\2\2\2\u0505\u0507")
        buf.write(u"\3\2\2\2\u0506\u04d3\3\2\2\2\u0506\u04e0\3\2\2\2\u0507")
        buf.write(u"s\3\2\2\2\u0508\u050a\7\u008e\2\2\u0509\u050b\7Z\2\2")
        buf.write(u"\u050a\u0509\3\2\2\2\u050a\u050b\3\2\2\2\u050b\u050c")
        buf.write(u"\3\2\2\2\u050c\u050d\7\22\2\2\u050d\u0513\5f\64\2\u050e")
        buf.write(u"\u050f\7\17\2\2\u050f\u0510\5\u0128\u0095\2\u0510\u0511")
        buf.write(u"\7)\2\2\u0511\u0512\5f\64\2\u0512\u0514\3\2\2\2\u0513")
        buf.write(u"\u050e\3\2\2\2\u0513\u0514\3\2\2\2\u0514\u0515\3\2\2")
        buf.write(u"\2\u0515\u0516\7\23\2\2\u0516u\3\2\2\2\u0517\u0518\7")
        buf.write(u"\21\2\2\u0518\u0522\5\u00b8]\2\u0519\u051a\7\24\2\2\u051a")
        buf.write(u"\u051b\5`\61\2\u051b\u051c\7\25\2\2\u051c\u0522\3\2\2")
        buf.write(u"\2\u051d\u051e\7\24\2\2\u051e\u051f\5\u0112\u008a\2\u051f")
        buf.write(u"\u0520\7\25\2\2\u0520\u0522\3\2\2\2\u0521\u0517\3\2\2")
        buf.write(u"\2\u0521\u0519\3\2\2\2\u0521\u051d\3\2\2\2\u0522w\3\2")
        buf.write(u"\2\2\u0523\u0524\5\u00aaV\2\u0524\u0525\7\22\2\2\u0525")
        buf.write(u"\u0528\5z>\2\u0526\u0527\7\17\2\2\u0527\u0529\5|?\2\u0528")
        buf.write(u"\u0526\3\2\2\2\u0528\u0529\3\2\2\2\u0529\u052a\3\2\2")
        buf.write(u"\2\u052a\u052b\7\23\2\2\u052b\u0534\3\2\2\2\u052c\u052d")
        buf.write(u"\5\u00aaV\2\u052d\u052f\7\22\2\2\u052e\u0530\5|?\2\u052f")
        buf.write(u"\u052e\3\2\2\2\u052f\u0530\3\2\2\2\u0530\u0531\3\2\2")
        buf.write(u"\2\u0531\u0532\7\23\2\2\u0532\u0534\3\2\2\2\u0533\u0523")
        buf.write(u"\3\2\2\2\u0533\u052c\3\2\2\2\u0534y\3\2\2\2\u0535\u0536")
        buf.write(u"\7j\2\2\u0536\u0537\5\u0130\u0099\2\u0537\u0538\5`\61")
        buf.write(u"\2\u0538\u0539\6>&\3\u0539{\3\2\2\2\u053a\u053b\b?\1")
        buf.write(u"\2\u053b\u053c\5`\61\2\u053c\u053d\6?\'\3\u053d\u0540")
        buf.write(u"\3\2\2\2\u053e\u0540\5~@\2\u053f\u053a\3\2\2\2\u053f")
        buf.write(u"\u053e\3\2\2\2\u0540\u0546\3\2\2\2\u0541\u0542\f\3\2")
        buf.write(u"\2\u0542\u0543\7\17\2\2\u0543\u0545\5~@\2\u0544\u0541")
        buf.write(u"\3\2\2\2\u0545\u0548\3\2\2\2\u0546\u0544\3\2\2\2\u0546")
        buf.write(u"\u0547\3\2\2\2\u0547}\3\2\2\2\u0548\u0546\3\2\2\2\u0549")
        buf.write(u"\u054d\5\u00b8]\2\u054a\u054b\5\u0130\u0099\2\u054b\u054c")
        buf.write(u"\5`\61\2\u054c\u054e\3\2\2\2\u054d\u054a\3\2\2\2\u054d")
        buf.write(u"\u054e\3\2\2\2\u054e\177\3\2\2\2\u054f\u0550\5\u0116")
        buf.write(u"\u008c\2\u0550\u0551\5\u0130\u0099\2\u0551\u0552\5`\61")
        buf.write(u"\2\u0552\u0553\7\16\2\2\u0553\u0081\3\2\2\2\u0554\u0555")
        buf.write(u"\7\21\2\2\u0555\u055b\5\u00b8]\2\u0556\u0557\7\24\2\2")
        buf.write(u"\u0557\u0558\5`\61\2\u0558\u0559\7\25\2\2\u0559\u055b")
        buf.write(u"\3\2\2\2\u055a\u0554\3\2\2\2\u055a\u0556\3\2\2\2\u055b")
        buf.write(u"\u0083\3\2\2\2\u055c\u055d\5\u00e0q\2\u055d\u055e\5\u0130")
        buf.write(u"\u0099\2\u055e\u055f\5`\61\2\u055f\u0560\7\16\2\2\u0560")
        buf.write(u"\u0085\3\2\2\2\u0561\u0562\7{\2\2\u0562\u0087\3\2\2\2")
        buf.write(u"\u0563\u0565\5\u008aF\2\u0564\u0563\3\2\2\2\u0564\u0565")
        buf.write(u"\3\2\2\2\u0565\u0566\3\2\2\2\u0566\u0567\5\u013a\u009e")
        buf.write(u"\2\u0567\u0568\7\2\2\3\u0568\u0089\3\2\2\2\u0569\u056f")
        buf.write(u"\5\u008cG\2\u056a\u056b\5\u013c\u009f\2\u056b\u056c\5")
        buf.write(u"\u008cG\2\u056c\u056e\3\2\2\2\u056d\u056a\3\2\2\2\u056e")
        buf.write(u"\u0571\3\2\2\2\u056f\u056d\3\2\2\2\u056f\u0570\3\2\2")
        buf.write(u"\2\u0570\u008b\3\2\2\2\u0571\u056f\3\2\2\2\u0572\u0573")
        buf.write(u"\5\u00e6t\2\u0573\u0574\5\u013c\u009f\2\u0574\u0576\3")
        buf.write(u"\2\2\2\u0575\u0572\3\2\2\2\u0576\u0579\3\2\2\2\u0577")
        buf.write(u"\u0575\3\2\2\2\u0577\u0578\3\2\2\2\u0578\u0580\3\2\2")
        buf.write(u"\2\u0579\u0577\3\2\2\2\u057a\u0581\5\n\6\2\u057b\u0581")
        buf.write(u"\5\u00aeX\2\u057c\u0581\5\u008eH\2\u057d\u0581\5\u0090")
        buf.write(u"I\2\u057e\u0581\5\u00b0Y\2\u057f\u0581\5\u00e4s\2\u0580")
        buf.write(u"\u057a\3\2\2\2\u0580\u057b\3\2\2\2\u0580\u057c\3\2\2")
        buf.write(u"\2\u0580\u057d\3\2\2\2\u0580\u057e\3\2\2\2\u0580\u057f")
        buf.write(u"\3\2\2\2\u0581\u008d\3\2\2\2\u0582\u0583\5 \21\2\u0583")
        buf.write(u"\u008f\3\2\2\2\u0584\u0587\5\2\2\2\u0585\u0587\5\4\3")
        buf.write(u"\2\u0586\u0584\3\2\2\2\u0586\u0585\3\2\2\2\u0587\u0091")
        buf.write(u"\3\2\2\2\u0588\u058e\5\b\5\2\u0589\u058a\5\u013c\u009f")
        buf.write(u"\2\u058a\u058b\5\b\5\2\u058b\u058d\3\2\2\2\u058c\u0589")
        buf.write(u"\3\2\2\2\u058d\u0590\3\2\2\2\u058e\u058c\3\2\2\2\u058e")
        buf.write(u"\u058f\3\2\2\2\u058f\u0093\3\2\2\2\u0590\u058e\3\2\2")
        buf.write(u"\2\u0591\u0597\5\6\4\2\u0592\u0593\5\u013c\u009f\2\u0593")
        buf.write(u"\u0594\5\6\4\2\u0594\u0596\3\2\2\2\u0595\u0592\3\2\2")
        buf.write(u"\2\u0596\u0599\3\2\2\2\u0597\u0595\3\2\2\2\u0597\u0598")
        buf.write(u"\3\2\2\2\u0598\u0095\3\2\2\2\u0599\u0597\3\2\2\2\u059a")
        buf.write(u"\u059f\5\u00be`\2\u059b\u059c\7\17\2\2\u059c\u059e\5")
        buf.write(u"\u00be`\2\u059d\u059b\3\2\2\2\u059e\u05a1\3\2\2\2\u059f")
        buf.write(u"\u059d\3\2\2\2\u059f\u05a0\3\2\2\2\u05a0\u0097\3\2\2")
        buf.write(u"\2\u05a1\u059f\3\2\2\2\u05a2\u05a3\7n\2\2\u05a3\u05ad")
        buf.write(u"\5\u009aN\2\u05a4\u05a5\7n\2\2\u05a5\u05ad\5\u009cO\2")
        buf.write(u"\u05a6\u05a7\7n\2\2\u05a7\u05ad\5\u00a0Q\2\u05a8\u05a9")
        buf.write(u"\7r\2\2\u05a9\u05ad\7\u00a7\2\2\u05aa\u05ab\7r\2\2\u05ab")
        buf.write(u"\u05ad\5`\61\2\u05ac\u05a2\3\2\2\2\u05ac\u05a4\3\2\2")
        buf.write(u"\2\u05ac\u05a6\3\2\2\2\u05ac\u05a8\3\2\2\2\u05ac\u05aa")
        buf.write(u"\3\2\2\2\u05ad\u0099\3\2\2\2\u05ae\u05b0\7v\2\2\u05af")
        buf.write(u"\u05ae\3\2\2\2\u05af\u05b0\3\2\2\2\u05b0\u05b1\3\2\2")
        buf.write(u"\2\u05b1\u05b3\7\24\2\2\u05b2\u05b4\5\u009eP\2\u05b3")
        buf.write(u"\u05b2\3\2\2\2\u05b3\u05b4\3\2\2\2\u05b4\u05b5\3\2\2")
        buf.write(u"\2\u05b5\u05b6\7\25\2\2\u05b6\u009b\3\2\2\2\u05b7\u05b9")
        buf.write(u"\7v\2\2\u05b8\u05b7\3\2\2\2\u05b8\u05b9\3\2\2\2\u05b9")
        buf.write(u"\u05ba\3\2\2\2\u05ba\u05bc\7&\2\2\u05bb\u05bd\5\u009e")
        buf.write(u"P\2\u05bc\u05bb\3\2\2\2\u05bc\u05bd\3\2\2\2\u05bd\u05be")
        buf.write(u"\3\2\2\2\u05be\u05bf\7$\2\2\u05bf\u009d\3\2\2\2\u05c0")
        buf.write(u"\u05c5\5`\61\2\u05c1\u05c2\7\17\2\2\u05c2\u05c4\5`\61")
        buf.write(u"\2\u05c3\u05c1\3\2\2\2\u05c4\u05c7\3\2\2\2\u05c5\u05c3")
        buf.write(u"\3\2\2\2\u05c5\u05c6\3\2\2\2\u05c6\u009f\3\2\2\2\u05c7")
        buf.write(u"\u05c5\3\2\2\2\u05c8\u05c9\7\24\2\2\u05c9\u05ca\5`\61")
        buf.write(u"\2\u05ca\u05cb\7\20\2\2\u05cb\u05cc\5`\61\2\u05cc\u05cd")
        buf.write(u"\7\25\2\2\u05cd\u00a1\3\2\2\2\u05ce\u05cf\bR\1\2\u05cf")
        buf.write(u"\u05db\5\u00a4S\2\u05d0\u05d1\7A\2\2\u05d1\u05d2\7&\2")
        buf.write(u"\2\u05d2\u05d3\5\u00a2R\2\u05d3\u05d4\7$\2\2\u05d4\u05db")
        buf.write(u"\3\2\2\2\u05d5\u05d6\7@\2\2\u05d6\u05d7\7&\2\2\u05d7")
        buf.write(u"\u05d8\5\u00a2R\2\u05d8\u05d9\7$\2\2\u05d9\u05db\3\2")
        buf.write(u"\2\2\u05da\u05ce\3\2\2\2\u05da\u05d0\3\2\2\2\u05da\u05d5")
        buf.write(u"\3\2\2\2\u05db\u05e6\3\2\2\2\u05dc\u05dd\f\7\2\2\u05dd")
        buf.write(u"\u05e5\7(\2\2\u05de\u05df\f\6\2\2\u05df\u05e0\7\24\2")
        buf.write(u"\2\u05e0\u05e5\7\25\2\2\u05e1\u05e2\f\5\2\2\u05e2\u05e3")
        buf.write(u"\7\26\2\2\u05e3\u05e5\7\27\2\2\u05e4\u05dc\3\2\2\2\u05e4")
        buf.write(u"\u05de\3\2\2\2\u05e4\u05e1\3\2\2\2\u05e5\u05e8\3\2\2")
        buf.write(u"\2\u05e6\u05e4\3\2\2\2\u05e6\u05e7\3\2\2\2\u05e7\u00a3")
        buf.write(u"\3\2\2\2\u05e8\u05e6\3\2\2\2\u05e9\u05ec\5\u00a6T\2\u05ea")
        buf.write(u"\u05ec\5\u00a8U\2\u05eb\u05e9\3\2\2\2\u05eb\u05ea\3\2")
        buf.write(u"\2\2\u05ec\u00a5\3\2\2\2\u05ed\u05fe\7\60\2\2\u05ee\u05fe")
        buf.write(u"\7\61\2\2\u05ef\u05fe\7\62\2\2\u05f0\u05fe\7>\2\2\u05f1")
        buf.write(u"\u05fe\7\63\2\2\u05f2\u05fe\7\64\2\2\u05f3\u05fe\7<\2")
        buf.write(u"\2\u05f4\u05fe\7\65\2\2\u05f5\u05fe\7\67\2\2\u05f6\u05fe")
        buf.write(u"\7\66\2\2\u05f7\u05fe\78\2\2\u05f8\u05fe\79\2\2\u05f9")
        buf.write(u"\u05fe\7;\2\2\u05fa\u05fe\7=\2\2\u05fb\u05fe\7?\2\2\u05fc")
        buf.write(u"\u05fe\7B\2\2\u05fd\u05ed\3\2\2\2\u05fd\u05ee\3\2\2\2")
        buf.write(u"\u05fd\u05ef\3\2\2\2\u05fd\u05f0\3\2\2\2\u05fd\u05f1")
        buf.write(u"\3\2\2\2\u05fd\u05f2\3\2\2\2\u05fd\u05f3\3\2\2\2\u05fd")
        buf.write(u"\u05f4\3\2\2\2\u05fd\u05f5\3\2\2\2\u05fd\u05f6\3\2\2")
        buf.write(u"\2\u05fd\u05f7\3\2\2\2\u05fd\u05f8\3\2\2\2\u05fd\u05f9")
        buf.write(u"\3\2\2\2\u05fd\u05fa\3\2\2\2\u05fd\u05fb\3\2\2\2\u05fd")
        buf.write(u"\u05fc\3\2\2\2\u05fe\u00a7\3\2\2\2\u05ff\u0600\7\u00a3")
        buf.write(u"\2\2\u0600\u00a9\3\2\2\2\u0601\u0603\7v\2\2\u0602\u0601")
        buf.write(u"\3\2\2\2\u0602\u0603\3\2\2\2\u0603\u0604\3\2\2\2\u0604")
        buf.write(u"\u0605\5\u00a8U\2\u0605\u00ab\3\2\2\2\u0606\u0607\7;")
        buf.write(u"\2\2\u0607\u00ad\3\2\2\2\u0608\u060c\5\16\b\2\u0609\u060c")
        buf.write(u"\5\"\22\2\u060a\u060c\5\20\t\2\u060b\u0608\3\2\2\2\u060b")
        buf.write(u"\u0609\3\2\2\2\u060b\u060a\3\2\2\2\u060c\u00af\3\2\2")
        buf.write(u"\2\u060d\u060e\5\f\7\2\u060e\u00b1\3\2\2\2\u060f\u0614")
        buf.write(u"\5\u00bc_\2\u0610\u0611\7\17\2\2\u0611\u0613\5\u00bc")
        buf.write(u"_\2\u0612\u0610\3\2\2\2\u0613\u0616\3\2\2\2\u0614\u0612")
        buf.write(u"\3\2\2\2\u0614\u0615\3\2\2\2\u0615\u00b3\3\2\2\2\u0616")
        buf.write(u"\u0614\3\2\2\2\u0617\u061a\5\u00b8]\2\u0618\u061a\5\u00bc")
        buf.write(u"_\2\u0619\u0617\3\2\2\2\u0619\u0618\3\2\2\2\u061a\u00b5")
        buf.write(u"\3\2\2\2\u061b\u061f\5\u00b8]\2\u061c\u061f\5\u00bc_")
        buf.write(u"\2\u061d\u061f\5\u00be`\2\u061e\u061b\3\2\2\2\u061e\u061c")
        buf.write(u"\3\2\2\2\u061e\u061d\3\2\2\2\u061f\u00b7\3\2\2\2\u0620")
        buf.write(u"\u0621\7\u00a4\2\2\u0621\u00b9\3\2\2\2\u0622\u0623\t")
        buf.write(u"\3\2\2\u0623\u00bb\3\2\2\2\u0624\u0625\7\u00a3\2\2\u0625")
        buf.write(u"\u00bd\3\2\2\2\u0626\u0627\7\u00a2\2\2\u0627\u00bf\3")
        buf.write(u"\2\2\2\u0628\u062d\5\u00c2b\2\u0629\u062a\7\17\2\2\u062a")
        buf.write(u"\u062c\5\u00c2b\2\u062b\u0629\3\2\2\2\u062c\u062f\3\2")
        buf.write(u"\2\2\u062d\u062b\3\2\2\2\u062d\u062e\3\2\2\2\u062e\u00c1")
        buf.write(u"\3\2\2\2\u062f\u062d\3\2\2\2\u0630\u0636\5\u00c8e\2\u0631")
        buf.write(u"\u0633\7v\2\2\u0632\u0631\3\2\2\2\u0632\u0633\3\2\2\2")
        buf.write(u"\u0633\u0634\3\2\2\2\u0634\u0636\5\u00c4c\2\u0635\u0630")
        buf.write(u"\3\2\2\2\u0635\u0632\3\2\2\2\u0636\u00c3\3\2\2\2\u0637")
        buf.write(u"\u063a\5\u00c6d\2\u0638\u063a\5\62\32\2\u0639\u0637\3")
        buf.write(u"\2\2\2\u0639\u0638\3\2\2\2\u063a\u00c5\3\2\2\2\u063b")
        buf.write(u"\u063e\5\u00b8]\2\u063c\u063d\7)\2\2\u063d\u063f\5\u0104")
        buf.write(u"\u0083\2\u063e\u063c\3\2\2\2\u063e\u063f\3\2\2\2\u063f")
        buf.write(u"\u00c7\3\2\2\2\u0640\u0641\5\u00acW\2\u0641\u0642\5\u00b8")
        buf.write(u"]\2\u0642\u00c9\3\2\2\2\u0643\u0646\5\u00a2R\2\u0644")
        buf.write(u"\u0646\5\u00ccg\2\u0645\u0643\3\2\2\2\u0645\u0644\3\2")
        buf.write(u"\2\2\u0646\u00cb\3\2\2\2\u0647\u0648\bg\1\2\u0648\u0649")
        buf.write(u"\7G\2\2\u0649\u0652\3\2\2\2\u064a\u064b\f\4\2\2\u064b")
        buf.write(u"\u064c\7\24\2\2\u064c\u0651\7\25\2\2\u064d\u064e\f\3")
        buf.write(u"\2\2\u064e\u064f\7\26\2\2\u064f\u0651\7\27\2\2\u0650")
        buf.write(u"\u064a\3\2\2\2\u0650\u064d\3\2\2\2\u0651\u0654\3\2\2")
        buf.write(u"\2\u0652\u0650\3\2\2\2\u0652\u0653\3\2\2\2\u0653\u00cd")
        buf.write(u"\3\2\2\2\u0654\u0652\3\2\2\2\u0655\u065b\5\u00d0i\2\u0656")
        buf.write(u"\u0657\5\u013c\u009f\2\u0657\u0658\5\u00d0i\2\u0658\u065a")
        buf.write(u"\3\2\2\2\u0659\u0656\3\2\2\2\u065a\u065d\3\2\2\2\u065b")
        buf.write(u"\u0659\3\2\2\2\u065b\u065c\3\2\2\2\u065c\u00cf\3\2\2")
        buf.write(u"\2\u065d\u065b\3\2\2\2\u065e\u0664\5\30\r\2\u065f\u0664")
        buf.write(u"\5\34\17\2\u0660\u0664\5*\26\2\u0661\u0664\5(\25\2\u0662")
        buf.write(u"\u0664\5\26\f\2\u0663\u065e\3\2\2\2\u0663\u065f\3\2\2")
        buf.write(u"\2\u0663\u0660\3\2\2\2\u0663\u0661\3\2\2\2\u0663\u0662")
        buf.write(u"\3\2\2\2\u0664\u00d1\3\2\2\2\u0665\u066b\5\u00d4k\2\u0666")
        buf.write(u"\u0667\5\u013c\u009f\2\u0667\u0668\5\u00d4k\2\u0668\u066a")
        buf.write(u"\3\2\2\2\u0669\u0666\3\2\2\2\u066a\u066d\3\2\2\2\u066b")
        buf.write(u"\u0669\3\2\2\2\u066b\u066c\3\2\2\2\u066c\u00d3\3\2\2")
        buf.write(u"\2\u066d\u066b\3\2\2\2\u066e\u0672\5\36\20\2\u066f\u0672")
        buf.write(u"\5\32\16\2\u0670\u0672\5,\27\2\u0671\u066e\3\2\2\2\u0671")
        buf.write(u"\u066f\3\2\2\2\u0671\u0670\3\2\2\2\u0672\u00d5\3\2\2")
        buf.write(u"\2\u0673\u0674\7\7\2\2\u0674\u067e\5\u018a\u00c6\2\u0675")
        buf.write(u"\u0676\7\b\2\2\u0676\u067e\5\u01a4\u00d3\2\u0677\u0678")
        buf.write(u"\7\t\2\2\u0678\u067e\5\u00d8m\2\u0679\u067a\7\n\2\2\u067a")
        buf.write(u"\u067e\5\u00d8m\2\u067b\u067c\7\13\2\2\u067c\u067e\5")
        buf.write(u"\u00dco\2\u067d\u0673\3\2\2\2\u067d\u0675\3\2\2\2\u067d")
        buf.write(u"\u0677\3\2\2\2\u067d\u0679\3\2\2\2\u067d\u067b\3\2\2")
        buf.write(u"\2\u067e\u00d7\3\2\2\2\u067f\u0681\5\u00b6\\\2\u0680")
        buf.write(u"\u0682\5\u00dan\2\u0681\u0680\3\2\2\2\u0681\u0682\3\2")
        buf.write(u"\2\2\u0682\u00d9\3\2\2\2\u0683\u0684\7j\2\2\u0684\u0685")
        buf.write(u"\5\u012a\u0096\2\u0685\u0686\7\r\2\2\u0686\u068b\5\u00b6")
        buf.write(u"\\\2\u0687\u0688\7\21\2\2\u0688\u068a\5\u00b6\\\2\u0689")
        buf.write(u"\u0687\3\2\2\2\u068a\u068d\3\2\2\2\u068b\u0689\3\2\2")
        buf.write(u"\2\u068b\u068c\3\2\2\2\u068c\u00db\3\2\2\2\u068d\u068b")
        buf.write(u"\3\2\2\2\u068e\u0690\5\u00b6\\\2\u068f\u0691\5\u00de")
        buf.write(u"p\2\u0690\u068f\3\2\2\2\u0690\u0691\3\2\2\2\u0691\u00dd")
        buf.write(u"\3\2\2\2\u0692\u0693\7j\2\2\u0693\u0694\5\u012a\u0096")
        buf.write(u"\2\u0694\u0696\7\r\2\2\u0695\u0697\7!\2\2\u0696\u0695")
        buf.write(u"\3\2\2\2\u0696\u0697\3\2\2\2\u0697\u0698\3\2\2\2\u0698")
        buf.write(u"\u069d\5\u0158\u00ad\2\u0699\u069a\7!\2\2\u069a\u069c")
        buf.write(u"\5\u0158\u00ad\2\u069b\u0699\3\2\2\2\u069c\u069f\3\2")
        buf.write(u"\2\2\u069d\u069b\3\2\2\2\u069d\u069e\3\2\2\2\u069e\u06a2")
        buf.write(u"\3\2\2\2\u069f\u069d\3\2\2\2\u06a0\u06a1\7\21\2\2\u06a1")
        buf.write(u"\u06a3\5\u0158\u00ad\2\u06a2\u06a0\3\2\2\2\u06a2\u06a3")
        buf.write(u"\3\2\2\2\u06a3\u00df\3\2\2\2\u06a4\u06a9\5\u00b8]\2\u06a5")
        buf.write(u"\u06a6\7\17\2\2\u06a6\u06a8\5\u00b8]\2\u06a7\u06a5\3")
        buf.write(u"\2\2\2\u06a8\u06ab\3\2\2\2\u06a9\u06a7\3\2\2\2\u06a9")
        buf.write(u"\u06aa\3\2\2\2\u06aa\u00e1\3\2\2\2\u06ab\u06a9\3\2\2")
        buf.write(u"\2\u06ac\u06b1\5\u00ba^\2\u06ad\u06ae\7\17\2\2\u06ae")
        buf.write(u"\u06b0\5\u00ba^\2\u06af\u06ad\3\2\2\2\u06b0\u06b3\3\2")
        buf.write(u"\2\2\u06b1\u06af\3\2\2\2\u06b1\u06b2\3\2\2\2\u06b2\u00e3")
        buf.write(u"\3\2\2\2\u06b3\u06b1\3\2\2\2\u06b4\u06b9\5(\25\2\u06b5")
        buf.write(u"\u06b9\5*\26\2\u06b6\u06b9\5,\27\2\u06b7\u06b9\5.\30")
        buf.write(u"\2\u06b8\u06b4\3\2\2\2\u06b8\u06b5\3\2\2\2\u06b8\u06b6")
        buf.write(u"\3\2\2\2\u06b8\u06b7\3\2\2\2\u06b9\u00e5\3\2\2\2\u06ba")
        buf.write(u"\u06bb\7\6\2\2\u06bb\u00e7\3\2\2\2\u06bc\u06c2\5\u00ea")
        buf.write(u"v\2\u06bd\u06be\5\u013c\u009f\2\u06be\u06bf\5\u00eav")
        buf.write(u"\2\u06bf\u06c1\3\2\2\2\u06c0\u06bd\3\2\2\2\u06c1\u06c4")
        buf.write(u"\3\2\2\2\u06c2\u06c0\3\2\2\2\u06c2\u06c3\3\2\2\2\u06c3")
        buf.write(u"\u00e9\3\2\2\2\u06c4\u06c2\3\2\2\2\u06c5\u06c6\7\7\2")
        buf.write(u"\2\u06c6\u06d0\5\u0174\u00bb\2\u06c7\u06c8\7\b\2\2\u06c8")
        buf.write(u"\u06d0\5\u0190\u00c9\2\u06c9\u06ca\7\t\2\2\u06ca\u06d0")
        buf.write(u"\5\u00ecw\2\u06cb\u06cc\7\n\2\2\u06cc\u06d0\5\u00ecw")
        buf.write(u"\2\u06cd\u06ce\7\13\2\2\u06ce\u06d0\5\u00eex\2\u06cf")
        buf.write(u"\u06c5\3\2\2\2\u06cf\u06c7\3\2\2\2\u06cf\u06c9\3\2\2")
        buf.write(u"\2\u06cf\u06cb\3\2\2\2\u06cf\u06cd\3\2\2\2\u06d0\u00eb")
        buf.write(u"\3\2\2\2\u06d1\u06d3\5\u015a\u00ae\2\u06d2\u06d4\7\16")
        buf.write(u"\2\2\u06d3\u06d2\3\2\2\2\u06d3\u06d4\3\2\2\2\u06d4\u06d6")
        buf.write(u"\3\2\2\2\u06d5\u06d7\5\u00dan\2\u06d6\u06d5\3\2\2\2\u06d6")
        buf.write(u"\u06d7\3\2\2\2\u06d7\u00ed\3\2\2\2\u06d8\u06da\5\u0140")
        buf.write(u"\u00a1\2\u06d9\u06db\7\16\2\2\u06da\u06d9\3\2\2\2\u06da")
        buf.write(u"\u06db\3\2\2\2\u06db\u06dd\3\2\2\2\u06dc\u06de\5\u00de")
        buf.write(u"p\2\u06dd\u06dc\3\2\2\2\u06dd\u06de\3\2\2\2\u06de\u00ef")
        buf.write(u"\3\2\2\2\u06df\u06e5\5\66\34\2\u06e0\u06e1\5\u013c\u009f")
        buf.write(u"\2\u06e1\u06e2\5\66\34\2\u06e2\u06e4\3\2\2\2\u06e3\u06e0")
        buf.write(u"\3\2\2\2\u06e4\u06e7\3\2\2\2\u06e5\u06e3\3\2\2\2\u06e5")
        buf.write(u"\u06e6\3\2\2\2\u06e6\u00f1\3\2\2\2\u06e7\u06e5\3\2\2")
        buf.write(u"\2\u06e8\u06ee\5\60\31\2\u06e9\u06ea\5\u013c\u009f\2")
        buf.write(u"\u06ea\u06eb\5\60\31\2\u06eb\u06ed\3\2\2\2\u06ec\u06e9")
        buf.write(u"\3\2\2\2\u06ed\u06f0\3\2\2\2\u06ee\u06ec\3\2\2\2\u06ee")
        buf.write(u"\u06ef\3\2\2\2\u06ef\u00f3\3\2\2\2\u06f0\u06ee\3\2\2")
        buf.write(u"\2\u06f1\u06f7\5B\"\2\u06f2\u06f3\5\u013c\u009f\2\u06f3")
        buf.write(u"\u06f4\5B\"\2\u06f4\u06f6\3\2\2\2\u06f5\u06f2\3\2\2\2")
        buf.write(u"\u06f6\u06f9\3\2\2\2\u06f7\u06f5\3\2\2\2\u06f7\u06f8")
        buf.write(u"\3\2\2\2\u06f8\u00f5\3\2\2\2\u06f9\u06f7\3\2\2\2\u06fa")
        buf.write(u"\u0700\5R*\2\u06fb\u06fc\5\u013c\u009f\2\u06fc\u06fd")
        buf.write(u"\5R*\2\u06fd\u06ff\3\2\2\2\u06fe\u06fb\3\2\2\2\u06ff")
        buf.write(u"\u0702\3\2\2\2\u0700\u06fe\3\2\2\2\u0700\u0701\3\2\2")
        buf.write(u"\2\u0701\u00f7\3\2\2\2\u0702\u0700\3\2\2\2\u0703\u0704")
        buf.write(u"\7\24\2\2\u0704\u0705\5\u00fa~\2\u0705\u0706\7\20\2\2")
        buf.write(u"\u0706\u0707\5\u00fa~\2\u0707\u0708\7\25\2\2\u0708\u0712")
        buf.write(u"\3\2\2\2\u0709\u070a\7\24\2\2\u070a\u070b\5\u00fc\177")
        buf.write(u"\2\u070b\u070c\7\25\2\2\u070c\u0712\3\2\2\2\u070d\u070e")
        buf.write(u"\7&\2\2\u070e\u070f\5\u00fc\177\2\u070f\u0710\7$\2\2")
        buf.write(u"\u0710\u0712\3\2\2\2\u0711\u0703\3\2\2\2\u0711\u0709")
        buf.write(u"\3\2\2\2\u0711\u070d\3\2\2\2\u0712\u00f9\3\2\2\2\u0713")
        buf.write(u"\u0723\7\u00a0\2\2\u0714\u0723\7\u00a1\2\2\u0715\u0723")
        buf.write(u"\7\u00a9\2\2\u0716\u0723\7\u00aa\2\2\u0717\u0723\7\u009f")
        buf.write(u"\2\2\u0718\u0723\7\u00ae\2\2\u0719\u0723\7\u00ad\2\2")
        buf.write(u"\u071a\u0723\7\u00a7\2\2\u071b\u0723\7\u00ab\2\2\u071c")
        buf.write(u"\u0723\7\u00ac\2\2\u071d\u0723\7\u009e\2\2\u071e\u0723")
        buf.write(u"\7\u00af\2\2\u071f\u0723\7\u00b0\2\2\u0720\u0723\7\u00a8")
        buf.write(u"\2\2\u0721\u0723\5\u0086D\2\u0722\u0713\3\2\2\2\u0722")
        buf.write(u"\u0714\3\2\2\2\u0722\u0715\3\2\2\2\u0722\u0716\3\2\2")
        buf.write(u"\2\u0722\u0717\3\2\2\2\u0722\u0718\3\2\2\2\u0722\u0719")
        buf.write(u"\3\2\2\2\u0722\u071a\3\2\2\2\u0722\u071b\3\2\2\2\u0722")
        buf.write(u"\u071c\3\2\2\2\u0722\u071d\3\2\2\2\u0722\u071e\3\2\2")
        buf.write(u"\2\u0722\u071f\3\2\2\2\u0722\u0720\3\2\2\2\u0722\u0721")
        buf.write(u"\3\2\2\2\u0723\u00fb\3\2\2\2\u0724\u0729\5\u00fa~\2\u0725")
        buf.write(u"\u0726\7\17\2\2\u0726\u0728\5\u00fa~\2\u0727\u0725\3")
        buf.write(u"\2\2\2\u0728\u072b\3\2\2\2\u0729\u0727\3\2\2\2\u0729")
        buf.write(u"\u072a\3\2\2\2\u072a\u00fd\3\2\2\2\u072b\u0729\3\2\2")
        buf.write(u"\2\u072c\u0731\5\u0102\u0082\2\u072d\u0731\5\u0104\u0083")
        buf.write(u"\2\u072e\u0731\5\u00b6\\\2\u072f\u0731\5\u0100\u0081")
        buf.write(u"\2\u0730\u072c\3\2\2\2\u0730\u072d\3\2\2\2\u0730\u072e")
        buf.write(u"\3\2\2\2\u0730\u072f\3\2\2\2\u0731\u00ff\3\2\2\2\u0732")
        buf.write(u"\u0733\t\4\2\2\u0733\u0101\3\2\2\2\u0734\u0735\7\22\2")
        buf.write(u"\2\u0735\u0736\5`\61\2\u0736\u0737\7\23\2\2\u0737\u0103")
        buf.write(u"\3\2\2\2\u0738\u073b\5\u00fa~\2\u0739\u073b\5\u0106\u0084")
        buf.write(u"\2\u073a\u0738\3\2\2\2\u073a\u0739\3\2\2\2\u073b\u0105")
        buf.write(u"\3\2\2\2\u073c\u0742\5\u00a0Q\2\u073d\u0742\5\u009aN")
        buf.write(u"\2\u073e\u0742\5\u009cO\2\u073f\u0742\5\u010a\u0086\2")
        buf.write(u"\u0740\u0742\5\u0108\u0085\2\u0741\u073c\3\2\2\2\u0741")
        buf.write(u"\u073d\3\2\2\2\u0741\u073e\3\2\2\2\u0741\u073f\3\2\2")
        buf.write(u"\2\u0741\u0740\3\2\2\2\u0742\u0107\3\2\2\2\u0743\u0745")
        buf.write(u"\7v\2\2\u0744\u0743\3\2\2\2\u0744\u0745\3\2\2\2\u0745")
        buf.write(u"\u0746\3\2\2\2\u0746\u0748\7\22\2\2\u0747\u0749\5\u010c")
        buf.write(u"\u0087\2\u0748\u0747\3\2\2\2\u0748\u0749\3\2\2\2\u0749")
        buf.write(u"\u074a\3\2\2\2\u074a\u074b\7\23\2\2\u074b\u0109\3\2\2")
        buf.write(u"\2\u074c\u074e\7v\2\2\u074d\u074c\3\2\2\2\u074d\u074e")
        buf.write(u"\3\2\2\2\u074e\u074f\3\2\2\2\u074f\u0751\7\26\2\2\u0750")
        buf.write(u"\u0752\5\u010e\u0088\2\u0751\u0750\3\2\2\2\u0751\u0752")
        buf.write(u"\3\2\2\2\u0752\u0753\3\2\2\2\u0753\u0754\7\27\2\2\u0754")
        buf.write(u"\u010b\3\2\2\2\u0755\u0756\5`\61\2\u0756\u075f\7\17\2")
        buf.write(u"\2\u0757\u075c\5`\61\2\u0758\u0759\7\17\2\2\u0759\u075b")
        buf.write(u"\5`\61\2\u075a\u0758\3\2\2\2\u075b\u075e\3\2\2\2\u075c")
        buf.write(u"\u075a\3\2\2\2\u075c\u075d\3\2\2\2\u075d\u0760\3\2\2")
        buf.write(u"\2\u075e\u075c\3\2\2\2\u075f\u0757\3\2\2\2\u075f\u0760")
        buf.write(u"\3\2\2\2\u0760\u010d\3\2\2\2\u0761\u0766\5\u0110\u0089")
        buf.write(u"\2\u0762\u0763\7\17\2\2\u0763\u0765\5\u0110\u0089\2\u0764")
        buf.write(u"\u0762\3\2\2\2\u0765\u0768\3\2\2\2\u0766\u0764\3\2\2")
        buf.write(u"\2\u0766\u0767\3\2\2\2\u0767\u010f\3\2\2\2\u0768\u0766")
        buf.write(u"\3\2\2\2\u0769\u076a\5`\61\2\u076a\u076b\7\r\2\2\u076b")
        buf.write(u"\u076c\5`\61\2\u076c\u0111\3\2\2\2\u076d\u076e\5`\61")
        buf.write(u"\2\u076e\u076f\7\r\2\2\u076f\u0770\5`\61\2\u0770\u0777")
        buf.write(u"\3\2\2\2\u0771\u0772\5`\61\2\u0772\u0773\7\r\2\2\u0773")
        buf.write(u"\u0777\3\2\2\2\u0774\u0775\7\r\2\2\u0775\u0777\5`\61")
        buf.write(u"\2\u0776\u076d\3\2\2\2\u0776\u0771\3\2\2\2\u0776\u0774")
        buf.write(u"\3\2\2\2\u0777\u0113\3\2\2\2\u0778\u0779\5\u00b8]\2\u0779")
        buf.write(u"\u077a\5\u0130\u0099\2\u077a\u077b\5`\61\2\u077b\u0115")
        buf.write(u"\3\2\2\2\u077c\u077d\b\u008c\1\2\u077d\u077e\5\u00b8")
        buf.write(u"]\2\u077e\u0783\3\2\2\2\u077f\u0780\f\3\2\2\u0780\u0782")
        buf.write(u"\5\u0082B\2\u0781\u077f\3\2\2\2\u0782\u0785\3\2\2\2\u0783")
        buf.write(u"\u0781\3\2\2\2\u0783\u0784\3\2\2\2\u0784\u0117\3\2\2")
        buf.write(u"\2\u0785\u0783\3\2\2\2\u0786\u0787\6\u008d/\3\u0787\u0788")
        buf.write(u"\7\u00a4\2\2\u0788\u078b\5\u00caf\2\u0789\u078b\5`\61")
        buf.write(u"\2\u078a\u0786\3\2\2\2\u078a\u0789\3\2\2\2\u078b\u0119")
        buf.write(u"\3\2\2\2\u078c\u078d\7\u0085\2\2\u078d\u078e\7D\2\2\u078e")
        buf.write(u"\u078f\7j\2\2\u078f\u0790\5`\61\2\u0790\u011b\3\2\2\2")
        buf.write(u"\u0791\u0792\7\u0085\2\2\u0792\u0793\7}\2\2\u0793\u0794")
        buf.write(u"\7j\2\2\u0794\u0795\5`\61\2\u0795\u011d\3\2\2\2\u0796")
        buf.write(u"\u079b\5\u0120\u0091\2\u0797\u0798\7\17\2\2\u0798\u079a")
        buf.write(u"\5\u0120\u0091\2\u0799\u0797\3\2\2\2\u079a\u079d\3\2")
        buf.write(u"\2\2\u079b\u0799\3\2\2\2\u079b\u079c\3\2\2\2\u079c\u011f")
        buf.write(u"\3\2\2\2\u079d\u079b\3\2\2\2\u079e\u07a3\5\u00b8]\2\u079f")
        buf.write(u"\u07a0\7\21\2\2\u07a0\u07a2\5\u00b8]\2\u07a1\u079f\3")
        buf.write(u"\2\2\2\u07a2\u07a5\3\2\2\2\u07a3\u07a1\3\2\2\2\u07a3")
        buf.write(u"\u07a4\3\2\2\2\u07a4\u07a7\3\2\2\2\u07a5\u07a3\3\2\2")
        buf.write(u"\2\u07a6\u07a8\t\5\2\2\u07a7\u07a6\3\2\2\2\u07a7\u07a8")
        buf.write(u"\3\2\2\2\u07a8\u0121\3\2\2\2\u07a9\u07b0\7\36\2\2\u07aa")
        buf.write(u"\u07b0\7\37\2\2\u07ab\u07b0\5\u0132\u009a\2\u07ac\u07b0")
        buf.write(u"\5\u0134\u009b\2\u07ad\u07b0\5\u0136\u009c\2\u07ae\u07b0")
        buf.write(u"\5\u0138\u009d\2\u07af\u07a9\3\2\2\2\u07af\u07aa\3\2")
        buf.write(u"\2\2\u07af\u07ab\3\2\2\2\u07af\u07ac\3\2\2\2\u07af\u07ad")
        buf.write(u"\3\2\2\2\u07af\u07ae\3\2\2\2\u07b0\u0123\3\2\2\2\u07b1")
        buf.write(u"\u07b2\t\6\2\2\u07b2\u0125\3\2\2\2\u07b3\u07b4\7\u00a4")
        buf.write(u"\2\2\u07b4\u07b5\6\u0094\60\3\u07b5\u0127\3\2\2\2\u07b6")
        buf.write(u"\u07b7\7\u00a4\2\2\u07b7\u07b8\6\u0095\61\3\u07b8\u0129")
        buf.write(u"\3\2\2\2\u07b9\u07ba\7\u00a4\2\2\u07ba\u07bb\6\u0096")
        buf.write(u"\62\3\u07bb\u012b\3\2\2\2\u07bc\u07bd\7\u00a4\2\2\u07bd")
        buf.write(u"\u07be\6\u0097\63\3\u07be\u012d\3\2\2\2\u07bf\u07c0\7")
        buf.write(u"\u00a4\2\2\u07c0\u07c1\6\u0098\64\3\u07c1\u012f\3\2\2")
        buf.write(u"\2\u07c2\u07c3\7)\2\2\u07c3\u0131\3\2\2\2\u07c4\u07c5")
        buf.write(u"\7 \2\2\u07c5\u0133\3\2\2\2\u07c6\u07c7\7!\2\2\u07c7")
        buf.write(u"\u0135\3\2\2\2\u07c8\u07c9\7\"\2\2\u07c9\u0137\3\2\2")
        buf.write(u"\2\u07ca\u07cb\t\7\2\2\u07cb\u0139\3\2\2\2\u07cc\u07cd")
        buf.write(u"\3\2\2\2\u07cd\u013b\3\2\2\2\u07ce\u07cf\3\2\2\2\u07cf")
        buf.write(u"\u013d\3\2\2\2\u07d0\u07d1\3\2\2\2\u07d1\u013f\3\2\2")
        buf.write(u"\2\u07d2\u07d3\7\u0088\2\2\u07d3\u07d4\5\u0142\u00a2")
        buf.write(u"\2\u07d4\u07d5\7\16\2\2\u07d5\u07da\3\2\2\2\u07d6\u07d7")
        buf.write(u"\5\u0142\u00a2\2\u07d7\u07d8\7\16\2\2\u07d8\u07da\3\2")
        buf.write(u"\2\2\u07d9\u07d2\3\2\2\2\u07d9\u07d6\3\2\2\2\u07da\u0141")
        buf.write(u"\3\2\2\2\u07db\u07dc\b\u00a2\1\2\u07dc\u07dd\5\u0144")
        buf.write(u"\u00a3\2\u07dd\u07e2\3\2\2\2\u07de\u07df\f\3\2\2\u07df")
        buf.write(u"\u07e1\5\u014a\u00a6\2\u07e0\u07de\3\2\2\2\u07e1\u07e4")
        buf.write(u"\3\2\2\2\u07e2\u07e0\3\2\2\2\u07e2\u07e3\3\2\2\2\u07e3")
        buf.write(u"\u0143\3\2\2\2\u07e4\u07e2\3\2\2\2\u07e5\u07ed\5\u0146")
        buf.write(u"\u00a4\2\u07e6\u07ed\5\u0148\u00a5\2\u07e7\u07ed\5\u0152")
        buf.write(u"\u00aa\2\u07e8\u07ed\5\u0154\u00ab\2\u07e9\u07ed\5\u0156")
        buf.write(u"\u00ac\2\u07ea\u07ed\5\u014c\u00a7\2\u07eb\u07ed\5\u0150")
        buf.write(u"\u00a9\2\u07ec\u07e5\3\2\2\2\u07ec\u07e6\3\2\2\2\u07ec")
        buf.write(u"\u07e7\3\2\2\2\u07ec\u07e8\3\2\2\2\u07ec\u07e9\3\2\2")
        buf.write(u"\2\u07ec\u07ea\3\2\2\2\u07ec\u07eb\3\2\2\2\u07ed\u0145")
        buf.write(u"\3\2\2\2\u07ee\u07ef\5\u0100\u0081\2\u07ef\u0147\3\2")
        buf.write(u"\2\2\u07f0\u07f1\5\u0126\u0094\2\u07f1\u07f2\5\u014c")
        buf.write(u"\u00a7\2\u07f2\u0149\3\2\2\2\u07f3\u07f4\7\21\2\2\u07f4")
        buf.write(u"\u07f9\5\u014c\u00a7\2\u07f5\u07f6\7\21\2\2\u07f6\u07f9")
        buf.write(u"\5\u0158\u00ad\2\u07f7\u07f9\5\u0150\u00a9\2\u07f8\u07f3")
        buf.write(u"\3\2\2\2\u07f8\u07f5\3\2\2\2\u07f8\u07f7\3\2\2\2\u07f9")
        buf.write(u"\u014b\3\2\2\2\u07fa\u07fb\5\u0158\u00ad\2\u07fb\u07fd")
        buf.write(u"\7\22\2\2\u07fc\u07fe\5\u014e\u00a8\2\u07fd\u07fc\3\2")
        buf.write(u"\2\2\u07fd\u07fe\3\2\2\2\u07fe\u07ff\3\2\2\2\u07ff\u0800")
        buf.write(u"\7\23\2\2\u0800\u014d\3\2\2\2\u0801\u0802\b\u00a8\1\2")
        buf.write(u"\u0802\u0803\5\u0142\u00a2\2\u0803\u0809\3\2\2\2\u0804")
        buf.write(u"\u0805\f\3\2\2\u0805\u0806\7\17\2\2\u0806\u0808\5\u0142")
        buf.write(u"\u00a2\2\u0807\u0804\3\2\2\2\u0808\u080b\3\2\2\2\u0809")
        buf.write(u"\u0807\3\2\2\2\u0809\u080a\3\2\2\2\u080a\u014f\3\2\2")
        buf.write(u"\2\u080b\u0809\3\2\2\2\u080c\u080d\7\24\2\2\u080d\u080e")
        buf.write(u"\5\u0142\u00a2\2\u080e\u080f\7\25\2\2\u080f\u0151\3\2")
        buf.write(u"\2\2\u0810\u0811\7\22\2\2\u0811\u0812\5\u0142\u00a2\2")
        buf.write(u"\u0812\u0813\7\23\2\2\u0813\u0153\3\2\2\2\u0814\u0815")
        buf.write(u"\5\u0158\u00ad\2\u0815\u0155\3\2\2\2\u0816\u081c\7\u00a9")
        buf.write(u"\2\2\u0817\u081c\7\u00ab\2\2\u0818\u081c\7\u00a7\2\2")
        buf.write(u"\u0819\u081c\7\u009e\2\2\u081a\u081c\7\u009f\2\2\u081b")
        buf.write(u"\u0816\3\2\2\2\u081b\u0817\3\2\2\2\u081b\u0818\3\2\2")
        buf.write(u"\2\u081b\u0819\3\2\2\2\u081b\u081a\3\2\2\2\u081c\u0157")
        buf.write(u"\3\2\2\2\u081d\u081e\t\b\2\2\u081e\u0159\3\2\2\2\u081f")
        buf.write(u"\u0820\7\u0088\2\2\u0820\u0823\5\u015c\u00af\2\u0821")
        buf.write(u"\u0823\5\u015c\u00af\2\u0822\u081f\3\2\2\2\u0822\u0821")
        buf.write(u"\3\2\2\2\u0823\u015b\3\2\2\2\u0824\u0825\b\u00af\1\2")
        buf.write(u"\u0825\u0826\5\u015e\u00b0\2\u0826\u082b\3\2\2\2\u0827")
        buf.write(u"\u0828\f\3\2\2\u0828\u082a\5\u0162\u00b2\2\u0829\u0827")
        buf.write(u"\3\2\2\2\u082a\u082d\3\2\2\2\u082b\u0829\3\2\2\2\u082b")
        buf.write(u"\u082c\3\2\2\2\u082c\u015d\3\2\2\2\u082d\u082b\3\2\2")
        buf.write(u"\2\u082e\u0834\5\u0160\u00b1\2\u082f\u0834\5\u016c\u00b7")
        buf.write(u"\2\u0830\u0834\5\u016e\u00b8\2\u0831\u0834\5\u0170\u00b9")
        buf.write(u"\2\u0832\u0834\5\u0164\u00b3\2\u0833\u082e\3\2\2\2\u0833")
        buf.write(u"\u082f\3\2\2\2\u0833\u0830\3\2\2\2\u0833\u0831\3\2\2")
        buf.write(u"\2\u0833\u0832\3\2\2\2\u0834\u015f\3\2\2\2\u0835\u0836")
        buf.write(u"\5\u0100\u0081\2\u0836\u0161\3\2\2\2\u0837\u0838\7\21")
        buf.write(u"\2\2\u0838\u083e\5\u0164\u00b3\2\u0839\u083a\7\24\2\2")
        buf.write(u"\u083a\u083b\5\u015c\u00af\2\u083b\u083c\7\25\2\2\u083c")
        buf.write(u"\u083e\3\2\2\2\u083d\u0837\3\2\2\2\u083d\u0839\3\2\2")
        buf.write(u"\2\u083e\u0163\3\2\2\2\u083f\u0840\5\u0172\u00ba\2\u0840")
        buf.write(u"\u0842\7\22\2\2\u0841\u0843\5\u0166\u00b4\2\u0842\u0841")
        buf.write(u"\3\2\2\2\u0842\u0843\3\2\2\2\u0843\u0844\3\2\2\2\u0844")
        buf.write(u"\u0845\7\23\2\2\u0845\u0165\3\2\2\2\u0846\u084d\5\u0168")
        buf.write(u"\u00b5\2\u0847\u084d\5\u016a\u00b6\2\u0848\u0849\5\u0168")
        buf.write(u"\u00b5\2\u0849\u084a\7\17\2\2\u084a\u084b\5\u016a\u00b6")
        buf.write(u"\2\u084b\u084d\3\2\2\2\u084c\u0846\3\2\2\2\u084c\u0847")
        buf.write(u"\3\2\2\2\u084c\u0848\3\2\2\2\u084d\u0167\3\2\2\2\u084e")
        buf.write(u"\u084f\b\u00b5\1\2\u084f\u0850\5\u015c\u00af\2\u0850")
        buf.write(u"\u0856\3\2\2\2\u0851\u0852\f\3\2\2\u0852\u0853\7\17\2")
        buf.write(u"\2\u0853\u0855\5\u015c\u00af\2\u0854\u0851\3\2\2\2\u0855")
        buf.write(u"\u0858\3\2\2\2\u0856\u0854\3\2\2\2\u0856\u0857\3\2\2")
        buf.write(u"\2\u0857\u0169\3\2\2\2\u0858\u0856\3\2\2\2\u0859\u085a")
        buf.write(u"\b\u00b6\1\2\u085a\u085b\5\u0172\u00ba\2\u085b\u085c")
        buf.write(u"\7)\2\2\u085c\u085d\5\u015c\u00af\2\u085d\u0866\3\2\2")
        buf.write(u"\2\u085e\u085f\f\3\2\2\u085f\u0860\7\17\2\2\u0860\u0861")
        buf.write(u"\5\u0172\u00ba\2\u0861\u0862\7)\2\2\u0862\u0863\5\u015c")
        buf.write(u"\u00af\2\u0863\u0865\3\2\2\2\u0864\u085e\3\2\2\2\u0865")
        buf.write(u"\u0868\3\2\2\2\u0866\u0864\3\2\2\2\u0866\u0867\3\2\2")
        buf.write(u"\2\u0867\u016b\3\2\2\2\u0868\u0866\3\2\2\2\u0869\u086a")
        buf.write(u"\7\22\2\2\u086a\u086b\5\u015c\u00af\2\u086b\u086c\7\23")
        buf.write(u"\2\2\u086c\u016d\3\2\2\2\u086d\u086e\b\u00b8\1\2\u086e")
        buf.write(u"\u0871\7\u00a6\2\2\u086f\u0871\5\u0172\u00ba\2\u0870")
        buf.write(u"\u086d\3\2\2\2\u0870\u086f\3\2\2\2\u0871\u0877\3\2\2")
        buf.write(u"\2\u0872\u0873\f\3\2\2\u0873\u0874\7\21\2\2\u0874\u0876")
        buf.write(u"\5\u0172\u00ba\2\u0875\u0872\3\2\2\2\u0876\u0879\3\2")
        buf.write(u"\2\2\u0877\u0875\3\2\2\2\u0877\u0878\3\2\2\2\u0878\u016f")
        buf.write(u"\3\2\2\2\u0879\u0877\3\2\2\2\u087a\u0880\7\u00a9\2\2")
        buf.write(u"\u087b\u0880\7\u00ab\2\2\u087c\u0880\7\u00a7\2\2\u087d")
        buf.write(u"\u0880\7\u009e\2\2\u087e\u0880\7\u009f\2\2\u087f\u087a")
        buf.write(u"\3\2\2\2\u087f\u087b\3\2\2\2\u087f\u087c\3\2\2\2\u087f")
        buf.write(u"\u087d\3\2\2\2\u087f\u087e\3\2\2\2\u0880\u0171\3\2\2")
        buf.write(u"\2\u0881\u0882\t\t\2\2\u0882\u0173\3\2\2\2\u0883\u0884")
        buf.write(u"\7\u0088\2\2\u0884\u0885\5\u0176\u00bc\2\u0885\u0886")
        buf.write(u"\7\16\2\2\u0886\u088b\3\2\2\2\u0887\u0888\5\u0176\u00bc")
        buf.write(u"\2\u0888\u0889\7\16\2\2\u0889\u088b\3\2\2\2\u088a\u0883")
        buf.write(u"\3\2\2\2\u088a\u0887\3\2\2\2\u088b\u0175\3\2\2\2\u088c")
        buf.write(u"\u088d\b\u00bc\1\2\u088d\u088e\5\u0178\u00bd\2\u088e")
        buf.write(u"\u0893\3\2\2\2\u088f\u0890\f\3\2\2\u0890\u0892\5\u017e")
        buf.write(u"\u00c0\2\u0891\u088f\3\2\2\2\u0892\u0895\3\2\2\2\u0893")
        buf.write(u"\u0891\3\2\2\2\u0893\u0894\3\2\2\2\u0894\u0177\3\2\2")
        buf.write(u"\2\u0895\u0893\3\2\2\2\u0896\u089c\5\u017a\u00be\2\u0897")
        buf.write(u"\u089c\5\u017c\u00bf\2\u0898\u089c\5\u0186\u00c4\2\u0899")
        buf.write(u"\u089c\5\u0188\u00c5\2\u089a\u089c\5\u018c\u00c7\2\u089b")
        buf.write(u"\u0896\3\2\2\2\u089b\u0897\3\2\2\2\u089b\u0898\3\2\2")
        buf.write(u"\2\u089b\u0899\3\2\2\2\u089b\u089a\3\2\2\2\u089c\u0179")
        buf.write(u"\3\2\2\2\u089d\u089e\5\u0100\u0081\2\u089e\u017b\3\2")
        buf.write(u"\2\2\u089f\u08a0\5\u0126\u0094\2\u08a0\u08a1\5\u0180")
        buf.write(u"\u00c1\2\u08a1\u017d\3\2\2\2\u08a2\u08a3\7\21\2\2\u08a3")
        buf.write(u"\u08a6\5\u0180\u00c1\2\u08a4\u08a6\5\u0184\u00c3\2\u08a5")
        buf.write(u"\u08a2\3\2\2\2\u08a5\u08a4\3\2\2\2\u08a6\u017f\3\2\2")
        buf.write(u"\2\u08a7\u08a8\5\u018e\u00c8\2\u08a8\u08aa\7\22\2\2\u08a9")
        buf.write(u"\u08ab\5\u0182\u00c2\2\u08aa\u08a9\3\2\2\2\u08aa\u08ab")
        buf.write(u"\3\2\2\2\u08ab\u08ac\3\2\2\2\u08ac\u08ad\7\23\2\2\u08ad")
        buf.write(u"\u0181\3\2\2\2\u08ae\u08af\b\u00c2\1\2\u08af\u08b0\5")
        buf.write(u"\u0176\u00bc\2\u08b0\u08b6\3\2\2\2\u08b1\u08b2\f\3\2")
        buf.write(u"\2\u08b2\u08b3\7\17\2\2\u08b3\u08b5\5\u0176\u00bc\2\u08b4")
        buf.write(u"\u08b1\3\2\2\2\u08b5\u08b8\3\2\2\2\u08b6\u08b4\3\2\2")
        buf.write(u"\2\u08b6\u08b7\3\2\2\2\u08b7\u0183\3\2\2\2\u08b8\u08b6")
        buf.write(u"\3\2\2\2\u08b9\u08ba\7\24\2\2\u08ba\u08bb\5\u0176\u00bc")
        buf.write(u"\2\u08bb\u08bc\7\25\2\2\u08bc\u0185\3\2\2\2\u08bd\u08be")
        buf.write(u"\7\22\2\2\u08be\u08bf\5\u0176\u00bc\2\u08bf\u08c0\7\23")
        buf.write(u"\2\2\u08c0\u0187\3\2\2\2\u08c1\u08c2\b\u00c5\1\2\u08c2")
        buf.write(u"\u08c3\5\u018e\u00c8\2\u08c3\u08c9\3\2\2\2\u08c4\u08c5")
        buf.write(u"\f\3\2\2\u08c5\u08c6\7\21\2\2\u08c6\u08c8\5\u018e\u00c8")
        buf.write(u"\2\u08c7\u08c4\3\2\2\2\u08c8\u08cb\3\2\2\2\u08c9\u08c7")
        buf.write(u"\3\2\2\2\u08c9\u08ca\3\2\2\2\u08ca\u0189\3\2\2\2\u08cb")
        buf.write(u"\u08c9\3\2\2\2\u08cc\u08cd\b\u00c6\1\2\u08cd\u08ce\5")
        buf.write(u"\u0188\u00c5\2\u08ce\u08d3\3\2\2\2\u08cf\u08d0\f\3\2")
        buf.write(u"\2\u08d0\u08d2\7\u00a6\2\2\u08d1\u08cf\3\2\2\2\u08d2")
        buf.write(u"\u08d5\3\2\2\2\u08d3\u08d1\3\2\2\2\u08d3\u08d4\3\2\2")
        buf.write(u"\2\u08d4\u018b\3\2\2\2\u08d5\u08d3\3\2\2\2\u08d6\u08dc")
        buf.write(u"\7\u00a9\2\2\u08d7\u08dc\7\u00ab\2\2\u08d8\u08dc\7\u00a7")
        buf.write(u"\2\2\u08d9\u08dc\7\u009e\2\2\u08da\u08dc\7\u009f\2\2")
        buf.write(u"\u08db\u08d6\3\2\2\2\u08db\u08d7\3\2\2\2\u08db\u08d8")
        buf.write(u"\3\2\2\2\u08db\u08d9\3\2\2\2\u08db\u08da\3\2\2\2\u08dc")
        buf.write(u"\u018d\3\2\2\2\u08dd\u08de\t\n\2\2\u08de\u018f\3\2\2")
        buf.write(u"\2\u08df\u08e0\7\u0088\2\2\u08e0\u08e1\5\u0192\u00ca")
        buf.write(u"\2\u08e1\u08e2\7\16\2\2\u08e2\u08e7\3\2\2\2\u08e3\u08e4")
        buf.write(u"\5\u0192\u00ca\2\u08e4\u08e5\7\16\2\2\u08e5\u08e7\3\2")
        buf.write(u"\2\2\u08e6\u08df\3\2\2\2\u08e6\u08e3\3\2\2\2\u08e7\u0191")
        buf.write(u"\3\2\2\2\u08e8\u08e9\b\u00ca\1\2\u08e9\u08ea\5\u0194")
        buf.write(u"\u00cb\2\u08ea\u08ef\3\2\2\2\u08eb\u08ec\f\3\2\2\u08ec")
        buf.write(u"\u08ee\5\u019a\u00ce\2\u08ed\u08eb\3\2\2\2\u08ee\u08f1")
        buf.write(u"\3\2\2\2\u08ef\u08ed\3\2\2\2\u08ef\u08f0\3\2\2\2\u08f0")
        buf.write(u"\u0193\3\2\2\2\u08f1\u08ef\3\2\2\2\u08f2\u08f8\5\u0196")
        buf.write(u"\u00cc\2\u08f3\u08f8\5\u0198\u00cd\2\u08f4\u08f8\5\u01a2")
        buf.write(u"\u00d2\2\u08f5\u08f8\5\u01a4\u00d3\2\u08f6\u08f8\5\u01a6")
        buf.write(u"\u00d4\2\u08f7\u08f2\3\2\2\2\u08f7\u08f3\3\2\2\2\u08f7")
        buf.write(u"\u08f4\3\2\2\2\u08f7\u08f5\3\2\2\2\u08f7\u08f6\3\2\2")
        buf.write(u"\2\u08f8\u0195\3\2\2\2\u08f9\u08fa\5\u0100\u0081\2\u08fa")
        buf.write(u"\u0197\3\2\2\2\u08fb\u08fc\5\u0126\u0094\2\u08fc\u08fd")
        buf.write(u"\5\u019c\u00cf\2\u08fd\u0199\3\2\2\2\u08fe\u08ff\7\21")
        buf.write(u"\2\2\u08ff\u0902\5\u019c\u00cf\2\u0900\u0902\5\u01a0")
        buf.write(u"\u00d1\2\u0901\u08fe\3\2\2\2\u0901\u0900\3\2\2\2\u0902")
        buf.write(u"\u019b\3\2\2\2\u0903\u0904\5\u01a8\u00d5\2\u0904\u0906")
        buf.write(u"\7\22\2\2\u0905\u0907\5\u019e\u00d0\2\u0906\u0905\3\2")
        buf.write(u"\2\2\u0906\u0907\3\2\2\2\u0907\u0908\3\2\2\2\u0908\u0909")
        buf.write(u"\7\23\2\2\u0909\u019d\3\2\2\2\u090a\u090b\b\u00d0\1\2")
        buf.write(u"\u090b\u090c\5\u0192\u00ca\2\u090c\u0912\3\2\2\2\u090d")
        buf.write(u"\u090e\f\3\2\2\u090e\u090f\7\17\2\2\u090f\u0911\5\u0192")
        buf.write(u"\u00ca\2\u0910\u090d\3\2\2\2\u0911\u0914\3\2\2\2\u0912")
        buf.write(u"\u0910\3\2\2\2\u0912\u0913\3\2\2\2\u0913\u019f\3\2\2")
        buf.write(u"\2\u0914\u0912\3\2\2\2\u0915\u0916\7\24\2\2\u0916\u0917")
        buf.write(u"\5\u0192\u00ca\2\u0917\u0918\7\25\2\2\u0918\u01a1\3\2")
        buf.write(u"\2\2\u0919\u091a\7\22\2\2\u091a\u091b\5\u0192\u00ca\2")
        buf.write(u"\u091b\u091c\7\23\2\2\u091c\u01a3\3\2\2\2\u091d\u091e")
        buf.write(u"\b\u00d3\1\2\u091e\u0921\7\u00a6\2\2\u091f\u0921\5\u01a8")
        buf.write(u"\u00d5\2\u0920\u091d\3\2\2\2\u0920\u091f\3\2\2\2\u0921")
        buf.write(u"\u0927\3\2\2\2\u0922\u0923\f\3\2\2\u0923\u0924\7\21\2")
        buf.write(u"\2\u0924\u0926\5\u01a8\u00d5\2\u0925\u0922\3\2\2\2\u0926")
        buf.write(u"\u0929\3\2\2\2\u0927\u0925\3\2\2\2\u0927\u0928\3\2\2")
        buf.write(u"\2\u0928\u01a5\3\2\2\2\u0929\u0927\3\2\2\2\u092a\u0930")
        buf.write(u"\7\u00a9\2\2\u092b\u0930\7\u00ab\2\2\u092c\u0930\7\u00a7")
        buf.write(u"\2\2\u092d\u0930\7\u009e\2\2\u092e\u0930\7\u009f\2\2")
        buf.write(u"\u092f\u092a\3\2\2\2\u092f\u092b\3\2\2\2\u092f\u092c")
        buf.write(u"\3\2\2\2\u092f\u092d\3\2\2\2\u092f\u092e\3\2\2\2\u0930")
        buf.write(u"\u01a7\3\2\2\2\u0931\u0932\t\13\2\2\u0932\u01a9\3\2\2")
        buf.write(u"\2\u0933\u0936\5\u01ac\u00d7\2\u0934\u0936\5\u01ae\u00d8")
        buf.write(u"\2\u0935\u0933\3\2\2\2\u0935\u0934\3\2\2\2\u0936\u01ab")
        buf.write(u"\3\2\2\2\u0937\u093f\5\u01b4\u00db\2\u0938\u093a\5\u01b6")
        buf.write(u"\u00dc\2\u0939\u093b\5\u01c8\u00e5\2\u093a\u0939\3\2")
        buf.write(u"\2\2\u093a\u093b\3\2\2\2\u093b\u093c\3\2\2\2\u093c\u093d")
        buf.write(u"\5\u01b8\u00dd\2\u093d\u093f\3\2\2\2\u093e\u0937\3\2")
        buf.write(u"\2\2\u093e\u0938\3\2\2\2\u093f\u01ad\3\2\2\2\u0940\u0942")
        buf.write(u"\5\u01b0\u00d9\2\u0941\u0943\5\u01c8\u00e5\2\u0942\u0941")
        buf.write(u"\3\2\2\2\u0942\u0943\3\2\2\2\u0943\u0944\3\2\2\2\u0944")
        buf.write(u"\u0945\5\u01b2\u00da\2\u0945\u01af\3\2\2\2\u0946\u0947")
        buf.write(u"\7&\2\2\u0947\u094a\7$\2\2\u0948\u094a\7(\2\2\u0949\u0946")
        buf.write(u"\3\2\2\2\u0949\u0948\3\2\2\2\u094a\u01b1\3\2\2\2\u094b")
        buf.write(u"\u094c\7&\2\2\u094c\u094d\7!\2\2\u094d\u094e\7$\2\2\u094e")
        buf.write(u"\u01b3\3\2\2\2\u094f\u0950\7&\2\2\u0950\u0954\5\u01ba")
        buf.write(u"\u00de\2\u0951\u0953\5\u01c4\u00e3\2\u0952\u0951\3\2")
        buf.write(u"\2\2\u0953\u0956\3\2\2\2\u0954\u0952\3\2\2\2\u0954\u0955")
        buf.write(u"\3\2\2\2\u0955\u0957\3\2\2\2\u0956\u0954\3\2\2\2\u0957")
        buf.write(u"\u0958\7!\2\2\u0958\u0959\7$\2\2\u0959\u01b5\3\2\2\2")
        buf.write(u"\u095a\u095b\7&\2\2\u095b\u095f\5\u01ba\u00de\2\u095c")
        buf.write(u"\u095e\5\u01c4\u00e3\2\u095d\u095c\3\2\2\2\u095e\u0961")
        buf.write(u"\3\2\2\2\u095f\u095d\3\2\2\2\u095f\u0960\3\2\2\2\u0960")
        buf.write(u"\u0962\3\2\2\2\u0961\u095f\3\2\2\2\u0962\u0963\7$\2\2")
        buf.write(u"\u0963\u01b7\3\2\2\2\u0964\u0965\7&\2\2\u0965\u0966\7")
        buf.write(u"!\2\2\u0966\u0967\5\u01ba\u00de\2\u0967\u0968\7$\2\2")
        buf.write(u"\u0968\u01b9\3\2\2\2\u0969\u096e\5\u01bc\u00df\2\u096a")
        buf.write(u"\u096b\7\21\2\2\u096b\u096d\5\u01bc\u00df\2\u096c\u096a")
        buf.write(u"\3\2\2\2\u096d\u0970\3\2\2\2\u096e\u096c\3\2\2\2\u096e")
        buf.write(u"\u096f\3\2\2\2\u096f\u01bb\3\2\2\2\u0970\u096e\3\2\2")
        buf.write(u"\2\u0971\u0975\5\u01c2\u00e2\2\u0972\u0974\5\u01be\u00e0")
        buf.write(u"\2\u0973\u0972\3\2\2\2\u0974\u0977\3\2\2\2\u0975\u0973")
        buf.write(u"\3\2\2\2\u0975\u0976\3\2\2\2\u0976\u01bd\3\2\2\2\u0977")
        buf.write(u"\u0975\3\2\2\2\u0978\u0979\6\u00e0B\3\u0979\u097a\7\37")
        buf.write(u"\2\2\u097a\u097b\5\u01c0\u00e1\2\u097b\u01bf\3\2\2\2")
        buf.write(u"\u097c\u097d\6\u00e1C\3\u097d\u097e\5\u01c2\u00e2\2\u097e")
        buf.write(u"\u01c1\3\2\2\2\u097f\u0982\5\u00b6\\\2\u0980\u0982\5")
        buf.write(u"\u0124\u0093\2\u0981\u097f\3\2\2\2\u0981\u0980\3\2\2")
        buf.write(u"\2\u0982\u01c3\3\2\2\2\u0983\u0986\5\u01bc\u00df\2\u0984")
        buf.write(u"\u0985\7)\2\2\u0985\u0987\5\u01c6\u00e4\2\u0986\u0984")
        buf.write(u"\3\2\2\2\u0986\u0987\3\2\2\2\u0987\u01c5\3\2\2\2\u0988")
        buf.write(u"\u098e\7\u00a7\2\2\u0989\u098a\7\26\2\2\u098a\u098b\5")
        buf.write(u"`\61\2\u098b\u098c\7\27\2\2\u098c\u098e\3\2\2\2\u098d")
        buf.write(u"\u0988\3\2\2\2\u098d\u0989\3\2\2\2\u098e\u01c7\3\2\2")
        buf.write(u"\2\u098f\u0991\5\u01ca\u00e6\2\u0990\u098f\3\2\2\2\u0991")
        buf.write(u"\u0992\3\2\2\2\u0992\u0990\3\2\2\2\u0992\u0993\3\2\2")
        buf.write(u"\2\u0993\u01c9\3\2\2\2\u0994\u099c\5\u01cc\u00e7\2\u0995")
        buf.write(u"\u099c\5\u01ac\u00d7\2\u0996\u0998\7\26\2\2\u0997\u0999")
        buf.write(u"\5`\61\2\u0998\u0997\3\2\2\2\u0998\u0999\3\2\2\2\u0999")
        buf.write(u"\u099a\3\2\2\2\u099a\u099c\7\27\2\2\u099b\u0994\3\2\2")
        buf.write(u"\2\u099b\u0995\3\2\2\2\u099b\u0996\3\2\2\2\u099c\u01cb")
        buf.write(u"\3\2\2\2\u099d\u099f\n\f\2\2\u099e\u099d\3\2\2\2\u099f")
        buf.write(u"\u09a0\3\2\2\2\u09a0\u099e\3\2\2\2\u09a0\u09a1\3\2\2")
        buf.write(u"\2\u09a1\u01cd\3\2\2\2\u00dd\u01d5\u01d9\u01f4\u01fb")
        buf.write(u"\u0203\u0205\u020d\u0212\u021a\u021e\u0228\u0234\u023a")
        buf.write(u"\u023d\u0240\u0249\u0251\u0256\u025c\u0264\u0269\u026f")
        buf.write(u"\u0274\u027d\u0282\u0287\u0290\u0295\u02a9\u02ae\u02b4")
        buf.write(u"\u02ba\u02c0\u02c5\u02ca\u02cd\u02d3\u02ea\u02f4\u02f9")
        buf.write(u"\u0300\u0302\u0319\u0337\u034e\u0350\u0358\u035f\u0361")
        buf.write(u"\u0369\u0373\u0388\u038c\u03a0\u03ad\u03b1\u03b9\u03bc")
        buf.write(u"\u03c1\u03c4\u03cc\u03d7\u03db\u03e2\u03e9\u03f2\u03fb")
        buf.write(u"\u0404\u041e\u0492\u0494\u04a4\u04b0\u04ba\u04d9\u04e6")
        buf.write(u"\u04ec\u04f5\u04fc\u0504\u0506\u050a\u0513\u0521\u0528")
        buf.write(u"\u052f\u0533\u053f\u0546\u054d\u055a\u0564\u056f\u0577")
        buf.write(u"\u0580\u0586\u058e\u0597\u059f\u05ac\u05af\u05b3\u05b8")
        buf.write(u"\u05bc\u05c5\u05da\u05e4\u05e6\u05eb\u05fd\u0602\u060b")
        buf.write(u"\u0614\u0619\u061e\u062d\u0632\u0635\u0639\u063e\u0645")
        buf.write(u"\u0650\u0652\u065b\u0663\u066b\u0671\u067d\u0681\u068b")
        buf.write(u"\u0690\u0696\u069d\u06a2\u06a9\u06b1\u06b8\u06c2\u06cf")
        buf.write(u"\u06d3\u06d6\u06da\u06dd\u06e5\u06ee\u06f7\u0700\u0711")
        buf.write(u"\u0722\u0729\u0730\u073a\u0741\u0744\u0748\u074d\u0751")
        buf.write(u"\u075c\u075f\u0766\u0776\u0783\u078a\u079b\u07a3\u07a7")
        buf.write(u"\u07af\u07d9\u07e2\u07ec\u07f8\u07fd\u0809\u081b\u0822")
        buf.write(u"\u082b\u0833\u083d\u0842\u084c\u0856\u0866\u0870\u0877")
        buf.write(u"\u087f\u088a\u0893\u089b\u08a5\u08aa\u08b6\u08c9\u08d3")
        buf.write(u"\u08db\u08e6\u08ef\u08f7\u0901\u0906\u0912\u0920\u0927")
        buf.write(u"\u092f\u0935\u093a\u093e\u0942\u0949\u0954\u095f\u096e")
        buf.write(u"\u0975\u0981\u0986\u098d\u0992\u0998\u099b\u09a0")
        return buf.getvalue()


class OParser ( AbstractParser ):

    grammarFileName = "OParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"' '", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'Java:'", u"'C#:'", u"'Python2:'", u"'Python3:'", 
                     u"'JavaScript:'", u"'Swift:'", u"':'", u"';'", u"<INVALID>", 
                     u"'..'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", 
                     u"<INVALID>", u"'-'", u"'*'", u"'/'", u"'\\'", u"'%'", 
                     u"'>'", u"'>='", u"'<'", u"'<='", u"'<>'", u"'='", 
                     u"'!='", u"'=='", u"'~='", u"'~'", u"'<-'", u"'->'", 
                     u"'Boolean'", u"'Character'", u"'Text'", u"'Integer'", 
                     u"'Decimal'", u"'Date'", u"'Time'", u"'DateTime'", 
                     u"'Period'", u"'Version'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'Blob'", u"'Image'", u"'Uuid'", u"'Iterator'", 
                     u"'Cursor'", u"'Html'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"<INVALID>", u"'attr'", 
                     u"'attribute'", u"'attributes'", u"'bindings'", u"'break'", 
                     u"'by'", u"'case'", u"'catch'", u"'category'", u"'class'", 
                     u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'filtered'", u"'finally'", u"'flush'", u"'for'", 
                     u"'from'", u"'getter'", u"'has'", u"'if'", u"'in'", 
                     u"'index'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
                     u"'methods'", u"'modulo'", u"'mutable'", u"'native'", 
                     u"'None'", u"'not'", u"<INVALID>", u"'null'", u"'on'", 
                     u"'one'", u"'open'", u"'operator'", u"'or'", u"'order'", 
                     u"'otherwise'", u"'pass'", u"'raise'", u"'read'", u"'receiving'", 
                     u"'resource'", u"'return'", u"'returning'", u"'rows'", 
                     u"'self'", u"'setter'", u"'singleton'", u"'sorted'", 
                     u"'storable'", u"'store'", u"'switch'", u"'test'", 
                     u"'this'", u"'throw'", u"'to'", u"'try'", u"'verifying'", 
                     u"'widget'", u"'with'", u"'when'", u"'where'", u"'while'", 
                     u"'write'", u"<INVALID>", u"<INVALID>", u"'MIN_INTEGER'", 
                     u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"SPACE", u"WS", u"LF", u"COMMENT", 
                      u"JAVA", u"CSHARP", u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", 
                      u"SWIFT", u"COLON", u"SEMI", u"COMMA", u"RANGE", u"DOT", 
                      u"LPAR", u"RPAR", u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", 
                      u"QMARK", u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", 
                      u"PLUS", u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"VERSION", u"METHOD_T", 
                      u"CODE", u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", 
                      u"ITERATOR", u"CURSOR", u"HTML", u"ABSTRACT", u"ALL", 
                      u"ALWAYS", u"AND", u"ANY", u"AS", u"ASC", u"ATTR", 
                      u"ATTRIBUTE", u"ATTRIBUTES", u"BINDINGS", u"BREAK", 
                      u"BY", u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DELETE", 
                      u"DESC", u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", 
                      u"ENUMERATED", u"EXCEPT", u"EXECUTE", u"EXPECTING", 
                      u"EXTENDS", u"FETCH", u"FILTERED", u"FINALLY", u"FLUSH", 
                      u"FOR", u"FROM", u"GETTER", u"HAS", u"IF", u"IN", 
                      u"INDEX", u"INVOKE", u"IS", u"MATCHING", u"METHOD", 
                      u"METHODS", u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", 
                      u"NOT", u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", 
                      u"OPERATOR", u"OR", u"ORDER", u"OTHERWISE", u"PASS", 
                      u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", u"RETURN", 
                      u"RETURNING", u"ROWS", u"SELF", u"SETTER", u"SINGLETON", 
                      u"SORTED", u"STORABLE", u"STORE", u"SWITCH", u"TEST", 
                      u"THIS", u"THROW", u"TO", u"TRY", u"VERIFYING", u"WIDGET", 
                      u"WITH", u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"UUID_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL", u"VERSION_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_category_symbol = 2
    RULE_native_symbol = 3
    RULE_attribute_declaration = 4
    RULE_concrete_widget_declaration = 5
    RULE_concrete_category_declaration = 6
    RULE_singleton_category_declaration = 7
    RULE_derived_list = 8
    RULE_category_method_list = 9
    RULE_operator_method_declaration = 10
    RULE_setter_method_declaration = 11
    RULE_native_setter_declaration = 12
    RULE_getter_method_declaration = 13
    RULE_native_getter_declaration = 14
    RULE_native_resource_declaration = 15
    RULE_native_category_declaration = 16
    RULE_native_category_bindings = 17
    RULE_native_category_binding_list = 18
    RULE_abstract_method_declaration = 19
    RULE_concrete_method_declaration = 20
    RULE_native_method_declaration = 21
    RULE_test_method_declaration = 22
    RULE_assertion = 23
    RULE_typed_argument = 24
    RULE_statement_or_list = 25
    RULE_statement = 26
    RULE_flush_statement = 27
    RULE_store_statement = 28
    RULE_with_resource_statement = 29
    RULE_with_singleton_statement = 30
    RULE_switch_statement = 31
    RULE_switch_case_statement = 32
    RULE_for_each_statement = 33
    RULE_do_while_statement = 34
    RULE_while_statement = 35
    RULE_if_statement = 36
    RULE_else_if_statement_list = 37
    RULE_raise_statement = 38
    RULE_try_statement = 39
    RULE_catch_statement = 40
    RULE_break_statement = 41
    RULE_return_statement = 42
    RULE_method_call = 43
    RULE_method_selector = 44
    RULE_callable_parent = 45
    RULE_callable_selector = 46
    RULE_expression = 47
    RULE_an_expression = 48
    RULE_closure_expression = 49
    RULE_instance_expression = 50
    RULE_method_expression = 51
    RULE_blob_expression = 52
    RULE_document_expression = 53
    RULE_write_statement = 54
    RULE_filtered_list_expression = 55
    RULE_fetch_store_expression = 56
    RULE_sorted_expression = 57
    RULE_selector_expression = 58
    RULE_constructor_expression = 59
    RULE_copy_from = 60
    RULE_argument_assignment_list = 61
    RULE_argument_assignment = 62
    RULE_assign_instance_statement = 63
    RULE_child_instance = 64
    RULE_assign_tuple_statement = 65
    RULE_null_literal = 66
    RULE_declaration_list = 67
    RULE_declarations = 68
    RULE_declaration = 69
    RULE_resource_declaration = 70
    RULE_enum_declaration = 71
    RULE_native_symbol_list = 72
    RULE_category_symbol_list = 73
    RULE_symbol_list = 74
    RULE_attribute_constraint = 75
    RULE_list_literal = 76
    RULE_set_literal = 77
    RULE_expression_list = 78
    RULE_range_literal = 79
    RULE_typedef = 80
    RULE_primary_type = 81
    RULE_native_type = 82
    RULE_category_type = 83
    RULE_mutable_category_type = 84
    RULE_code_type = 85
    RULE_category_declaration = 86
    RULE_widget_declaration = 87
    RULE_type_identifier_list = 88
    RULE_method_identifier = 89
    RULE_identifier = 90
    RULE_variable_identifier = 91
    RULE_attribute_identifier = 92
    RULE_type_identifier = 93
    RULE_symbol_identifier = 94
    RULE_argument_list = 95
    RULE_argument = 96
    RULE_operator_argument = 97
    RULE_named_argument = 98
    RULE_code_argument = 99
    RULE_category_or_any_type = 100
    RULE_any_type = 101
    RULE_member_method_declaration_list = 102
    RULE_member_method_declaration = 103
    RULE_native_member_method_declaration_list = 104
    RULE_native_member_method_declaration = 105
    RULE_native_category_binding = 106
    RULE_python_category_binding = 107
    RULE_python_module = 108
    RULE_javascript_category_binding = 109
    RULE_javascript_module = 110
    RULE_variable_identifier_list = 111
    RULE_attribute_identifier_list = 112
    RULE_method_declaration = 113
    RULE_comment_statement = 114
    RULE_native_statement_list = 115
    RULE_native_statement = 116
    RULE_python_native_statement = 117
    RULE_javascript_native_statement = 118
    RULE_statement_list = 119
    RULE_assertion_list = 120
    RULE_switch_case_statement_list = 121
    RULE_catch_statement_list = 122
    RULE_literal_collection = 123
    RULE_atomic_literal = 124
    RULE_literal_list_literal = 125
    RULE_selectable_expression = 126
    RULE_this_expression = 127
    RULE_parenthesis_expression = 128
    RULE_literal_expression = 129
    RULE_collection_literal = 130
    RULE_tuple_literal = 131
    RULE_dict_literal = 132
    RULE_expression_tuple = 133
    RULE_dict_entry_list = 134
    RULE_dict_entry = 135
    RULE_slice_arguments = 136
    RULE_assign_variable_statement = 137
    RULE_assignable_instance = 138
    RULE_is_expression = 139
    RULE_read_all_expression = 140
    RULE_read_one_expression = 141
    RULE_order_by_list = 142
    RULE_order_by = 143
    RULE_operator = 144
    RULE_keyword = 145
    RULE_new_token = 146
    RULE_key_token = 147
    RULE_module_token = 148
    RULE_value_token = 149
    RULE_symbols_token = 150
    RULE_assign = 151
    RULE_multiply = 152
    RULE_divide = 153
    RULE_idivide = 154
    RULE_modulo = 155
    RULE_lfs = 156
    RULE_lfp = 157
    RULE_native_widget_declaration = 158
    RULE_javascript_statement = 159
    RULE_javascript_expression = 160
    RULE_javascript_primary_expression = 161
    RULE_javascript_this_expression = 162
    RULE_javascript_new_expression = 163
    RULE_javascript_selector_expression = 164
    RULE_javascript_method_expression = 165
    RULE_javascript_arguments = 166
    RULE_javascript_item_expression = 167
    RULE_javascript_parenthesis_expression = 168
    RULE_javascript_identifier_expression = 169
    RULE_javascript_literal_expression = 170
    RULE_javascript_identifier = 171
    RULE_python_statement = 172
    RULE_python_expression = 173
    RULE_python_primary_expression = 174
    RULE_python_self_expression = 175
    RULE_python_selector_expression = 176
    RULE_python_method_expression = 177
    RULE_python_argument_list = 178
    RULE_python_ordinal_argument_list = 179
    RULE_python_named_argument_list = 180
    RULE_python_parenthesis_expression = 181
    RULE_python_identifier_expression = 182
    RULE_python_literal_expression = 183
    RULE_python_identifier = 184
    RULE_java_statement = 185
    RULE_java_expression = 186
    RULE_java_primary_expression = 187
    RULE_java_this_expression = 188
    RULE_java_new_expression = 189
    RULE_java_selector_expression = 190
    RULE_java_method_expression = 191
    RULE_java_arguments = 192
    RULE_java_item_expression = 193
    RULE_java_parenthesis_expression = 194
    RULE_java_identifier_expression = 195
    RULE_java_class_identifier_expression = 196
    RULE_java_literal_expression = 197
    RULE_java_identifier = 198
    RULE_csharp_statement = 199
    RULE_csharp_expression = 200
    RULE_csharp_primary_expression = 201
    RULE_csharp_this_expression = 202
    RULE_csharp_new_expression = 203
    RULE_csharp_selector_expression = 204
    RULE_csharp_method_expression = 205
    RULE_csharp_arguments = 206
    RULE_csharp_item_expression = 207
    RULE_csharp_parenthesis_expression = 208
    RULE_csharp_identifier_expression = 209
    RULE_csharp_literal_expression = 210
    RULE_csharp_identifier = 211
    RULE_jsx_expression = 212
    RULE_jsx_element = 213
    RULE_jsx_fragment = 214
    RULE_jsx_fragment_start = 215
    RULE_jsx_fragment_end = 216
    RULE_jsx_self_closing = 217
    RULE_jsx_opening = 218
    RULE_jsx_closing = 219
    RULE_jsx_element_name = 220
    RULE_jsx_identifier = 221
    RULE_jsx_hyphen_identifier = 222
    RULE_hyphen_identifier = 223
    RULE_identifier_or_keyword = 224
    RULE_jsx_attribute = 225
    RULE_jsx_attribute_value = 226
    RULE_jsx_children = 227
    RULE_jsx_child = 228
    RULE_jsx_text = 229

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"category_symbol", u"native_symbol", u"attribute_declaration", 
                   u"concrete_widget_declaration", u"concrete_category_declaration", 
                   u"singleton_category_declaration", u"derived_list", u"category_method_list", 
                   u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_resource_declaration", 
                   u"native_category_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"typed_argument", 
                   u"statement_or_list", u"statement", u"flush_statement", 
                   u"store_statement", u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"break_statement", u"return_statement", 
                   u"method_call", u"method_selector", u"callable_parent", 
                   u"callable_selector", u"expression", u"an_expression", 
                   u"closure_expression", u"instance_expression", u"method_expression", 
                   u"blob_expression", u"document_expression", u"write_statement", 
                   u"filtered_list_expression", u"fetch_store_expression", 
                   u"sorted_expression", u"selector_expression", u"constructor_expression", 
                   u"copy_from", u"argument_assignment_list", u"argument_assignment", 
                   u"assign_instance_statement", u"child_instance", u"assign_tuple_statement", 
                   u"null_literal", u"declaration_list", u"declarations", 
                   u"declaration", u"resource_declaration", u"enum_declaration", 
                   u"native_symbol_list", u"category_symbol_list", u"symbol_list", 
                   u"attribute_constraint", u"list_literal", u"set_literal", 
                   u"expression_list", u"range_literal", u"typedef", u"primary_type", 
                   u"native_type", u"category_type", u"mutable_category_type", 
                   u"code_type", u"category_declaration", u"widget_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"attribute_identifier", u"type_identifier", 
                   u"symbol_identifier", u"argument_list", u"argument", 
                   u"operator_argument", u"named_argument", u"code_argument", 
                   u"category_or_any_type", u"any_type", u"member_method_declaration_list", 
                   u"member_method_declaration", u"native_member_method_declaration_list", 
                   u"native_member_method_declaration", u"native_category_binding", 
                   u"python_category_binding", u"python_module", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"attribute_identifier_list", 
                   u"method_declaration", u"comment_statement", u"native_statement_list", 
                   u"native_statement", u"python_native_statement", u"javascript_native_statement", 
                   u"statement_list", u"assertion_list", u"switch_case_statement_list", 
                   u"catch_statement_list", u"literal_collection", u"atomic_literal", 
                   u"literal_list_literal", u"selectable_expression", u"this_expression", 
                   u"parenthesis_expression", u"literal_expression", u"collection_literal", 
                   u"tuple_literal", u"dict_literal", u"expression_tuple", 
                   u"dict_entry_list", u"dict_entry", u"slice_arguments", 
                   u"assign_variable_statement", u"assignable_instance", 
                   u"is_expression", u"read_all_expression", u"read_one_expression", 
                   u"order_by_list", u"order_by", u"operator", u"keyword", 
                   u"new_token", u"key_token", u"module_token", u"value_token", 
                   u"symbols_token", u"assign", u"multiply", u"divide", 
                   u"idivide", u"modulo", u"lfs", u"lfp", u"native_widget_declaration", 
                   u"javascript_statement", u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_new_expression", 
                   u"javascript_selector_expression", u"javascript_method_expression", 
                   u"javascript_arguments", u"javascript_item_expression", 
                   u"javascript_parenthesis_expression", u"javascript_identifier_expression", 
                   u"javascript_literal_expression", u"javascript_identifier", 
                   u"python_statement", u"python_expression", u"python_primary_expression", 
                   u"python_self_expression", u"python_selector_expression", 
                   u"python_method_expression", u"python_argument_list", 
                   u"python_ordinal_argument_list", u"python_named_argument_list", 
                   u"python_parenthesis_expression", u"python_identifier_expression", 
                   u"python_literal_expression", u"python_identifier", u"java_statement", 
                   u"java_expression", u"java_primary_expression", u"java_this_expression", 
                   u"java_new_expression", u"java_selector_expression", 
                   u"java_method_expression", u"java_arguments", u"java_item_expression", 
                   u"java_parenthesis_expression", u"java_identifier_expression", 
                   u"java_class_identifier_expression", u"java_literal_expression", 
                   u"java_identifier", u"csharp_statement", u"csharp_expression", 
                   u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_new_expression", u"csharp_selector_expression", 
                   u"csharp_method_expression", u"csharp_arguments", u"csharp_item_expression", 
                   u"csharp_parenthesis_expression", u"csharp_identifier_expression", 
                   u"csharp_literal_expression", u"csharp_identifier", u"jsx_expression", 
                   u"jsx_element", u"jsx_fragment", u"jsx_fragment_start", 
                   u"jsx_fragment_end", u"jsx_self_closing", u"jsx_opening", 
                   u"jsx_closing", u"jsx_element_name", u"jsx_identifier", 
                   u"jsx_hyphen_identifier", u"hyphen_identifier", u"identifier_or_keyword", 
                   u"jsx_attribute", u"jsx_attribute_value", u"jsx_children", 
                   u"jsx_child", u"jsx_text" ]

    EOF = Token.EOF
    SPACE=1
    WS=2
    LF=3
    COMMENT=4
    JAVA=5
    CSHARP=6
    PYTHON2=7
    PYTHON3=8
    JAVASCRIPT=9
    SWIFT=10
    COLON=11
    SEMI=12
    COMMA=13
    RANGE=14
    DOT=15
    LPAR=16
    RPAR=17
    LBRAK=18
    RBRAK=19
    LCURL=20
    RCURL=21
    QMARK=22
    XMARK=23
    AMP=24
    AMP2=25
    PIPE=26
    PIPE2=27
    PLUS=28
    MINUS=29
    STAR=30
    SLASH=31
    BSLASH=32
    PERCENT=33
    GT=34
    GTE=35
    LT=36
    LTE=37
    LTGT=38
    EQ=39
    XEQ=40
    EQ2=41
    TEQ=42
    TILDE=43
    LARROW=44
    RARROW=45
    BOOLEAN=46
    CHARACTER=47
    TEXT=48
    INTEGER=49
    DECIMAL=50
    DATE=51
    TIME=52
    DATETIME=53
    PERIOD=54
    VERSION=55
    METHOD_T=56
    CODE=57
    DOCUMENT=58
    BLOB=59
    IMAGE=60
    UUID=61
    ITERATOR=62
    CURSOR=63
    HTML=64
    ABSTRACT=65
    ALL=66
    ALWAYS=67
    AND=68
    ANY=69
    AS=70
    ASC=71
    ATTR=72
    ATTRIBUTE=73
    ATTRIBUTES=74
    BINDINGS=75
    BREAK=76
    BY=77
    CASE=78
    CATCH=79
    CATEGORY=80
    CLASS=81
    CLOSE=82
    CONTAINS=83
    DEF=84
    DEFAULT=85
    DEFINE=86
    DELETE=87
    DESC=88
    DO=89
    DOING=90
    EACH=91
    ELSE=92
    ENUM=93
    ENUMERATED=94
    EXCEPT=95
    EXECUTE=96
    EXPECTING=97
    EXTENDS=98
    FETCH=99
    FILTERED=100
    FINALLY=101
    FLUSH=102
    FOR=103
    FROM=104
    GETTER=105
    HAS=106
    IF=107
    IN=108
    INDEX=109
    INVOKE=110
    IS=111
    MATCHING=112
    METHOD=113
    METHODS=114
    MODULO=115
    MUTABLE=116
    NATIVE=117
    NONE=118
    NOT=119
    NOTHING=120
    NULL=121
    ON=122
    ONE=123
    OPEN=124
    OPERATOR=125
    OR=126
    ORDER=127
    OTHERWISE=128
    PASS=129
    RAISE=130
    READ=131
    RECEIVING=132
    RESOURCE=133
    RETURN=134
    RETURNING=135
    ROWS=136
    SELF=137
    SETTER=138
    SINGLETON=139
    SORTED=140
    STORABLE=141
    STORE=142
    SWITCH=143
    TEST=144
    THIS=145
    THROW=146
    TO=147
    TRY=148
    VERIFYING=149
    WIDGET=150
    WITH=151
    WHEN=152
    WHERE=153
    WHILE=154
    WRITE=155
    BOOLEAN_LITERAL=156
    CHAR_LITERAL=157
    MIN_INTEGER=158
    MAX_INTEGER=159
    SYMBOL_IDENTIFIER=160
    TYPE_IDENTIFIER=161
    VARIABLE_IDENTIFIER=162
    NATIVE_IDENTIFIER=163
    DOLLAR_IDENTIFIER=164
    TEXT_LITERAL=165
    UUID_LITERAL=166
    INTEGER_LITERAL=167
    HEXA_LITERAL=168
    DECIMAL_LITERAL=169
    DATETIME_LITERAL=170
    TIME_LITERAL=171
    DATE_LITERAL=172
    PERIOD_LITERAL=173
    VERSION_LITERAL=174

    def __init__(self, input, output=sys.stdout):
        super(OParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.derived = None # Type_identifierContext
            self.symbols = None # Category_symbol_listContext

        def ENUMERATED(self):
            return self.getToken(OParser.ENUMERATED, 0)

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(OParser.Category_symbol_listContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_category_declaration"):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_category_declaration"):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = OParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(OParser.ENUMERATED)
            self.state = 461
            self.match(OParser.CATEGORY)
            self.state = 462
            localctx.name = self.type_identifier()
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 463
                self.match(OParser.LPAR)
                self.state = 464
                localctx.attrs = self.attribute_identifier_list()
                self.state = 465
                self.match(OParser.RPAR)


            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 469
                self.match(OParser.EXTENDS)
                self.state = 470
                localctx.derived = self.type_identifier()


            self.state = 473
            self.match(OParser.LCURL)
            self.state = 474
            localctx.symbols = self.category_symbol_list()
            self.state = 475
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_native_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUMERATED(self):
            return self.getToken(OParser.ENUMERATED, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(OParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(OParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_native_declaration"):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_native_declaration"):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = OParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(OParser.ENUMERATED)
            self.state = 478
            localctx.name = self.type_identifier()
            self.state = 479
            self.match(OParser.LPAR)
            self.state = 480
            localctx.typ = self.native_type()
            self.state = 481
            self.match(OParser.RPAR)
            self.state = 482
            self.match(OParser.LCURL)
            self.state = 483
            localctx.symbols = self.native_symbol_list()
            self.state = 484
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_category_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol"):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol"):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = OParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_category_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            localctx.name = self.symbol_identifier()
            self.state = 487
            self.match(OParser.LPAR)
            self.state = 488
            localctx.args = self.argument_assignment_list(0)
            self.state = 489
            self.match(OParser.RPAR)
            self.state = 490
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol"):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol"):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = OParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            localctx.name = self.symbol_identifier()
            self.state = 493
            self.match(OParser.EQ)
            self.state = 494
            localctx.exp = self.expression(0)
            self.state = 495
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Variable_identifier_listContext

        def ATTRIBUTE(self):
            return self.getToken(OParser.ATTRIBUTE, 0)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def attribute_identifier(self):
            return self.getTypedRuleContext(OParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def INDEX(self):
            return self.getToken(OParser.INDEX, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(OParser.Attribute_constraintContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(OParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_declaration"):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_declaration"):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = OParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 497
                self.match(OParser.STORABLE)


            self.state = 500
            self.match(OParser.ATTRIBUTE)
            self.state = 501
            localctx.name = self.attribute_identifier()
            self.state = 502
            self.match(OParser.COLON)
            self.state = 503
            localctx.typ = self.typedef(0)
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.IN or _la==OParser.MATCHING:
                self.state = 504
                localctx.match = self.attribute_constraint()


            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.WITH:
                self.state = 507
                self.match(OParser.WITH)
                self.state = 508
                self.match(OParser.INDEX)
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 509
                    self.match(OParser.LPAR)
                    self.state = 510
                    localctx.indices = self.variable_identifier_list()
                    self.state = 511
                    self.match(OParser.RPAR)




            self.state = 517
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_widget_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Concrete_widget_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.methods = None # Category_method_listContext

        def WIDGET(self):
            return self.getToken(OParser.WIDGET, 0)

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Type_identifierContext,i)


        def category_method_list(self):
            return self.getTypedRuleContext(OParser.Category_method_listContext,0)


        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def getRuleIndex(self):
            return OParser.RULE_concrete_widget_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_widget_declaration"):
                listener.enterConcrete_widget_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_widget_declaration"):
                listener.exitConcrete_widget_declaration(self)




    def concrete_widget_declaration(self):

        localctx = OParser.Concrete_widget_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_widget_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(OParser.WIDGET)
            self.state = 520
            localctx.name = self.type_identifier()
            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 521
                self.match(OParser.EXTENDS)
                self.state = 522
                localctx.derived = self.type_identifier()


            self.state = 525
            localctx.methods = self.category_method_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.derived = None # Derived_listContext
            self.methods = None # Category_method_listContext

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def category_method_list(self):
            return self.getTypedRuleContext(OParser.Category_method_listContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def derived_list(self):
            return self.getTypedRuleContext(OParser.Derived_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_category_declaration"):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_category_declaration"):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = OParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 527
                self.match(OParser.STORABLE)


            self.state = 530
            self.match(OParser.CATEGORY)
            self.state = 531
            localctx.name = self.type_identifier()
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 532
                self.match(OParser.LPAR)
                self.state = 533
                localctx.attrs = self.attribute_identifier_list()
                self.state = 534
                self.match(OParser.RPAR)


            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 538
                self.match(OParser.EXTENDS)
                self.state = 539
                localctx.derived = self.derived_list(0)


            self.state = 542
            localctx.methods = self.category_method_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Singleton_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.methods = None # Category_method_listContext

        def SINGLETON(self):
            return self.getToken(OParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def category_method_list(self):
            return self.getTypedRuleContext(OParser.Category_method_listContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSingleton_category_declaration"):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleton_category_declaration"):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = OParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleton_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(OParser.SINGLETON)
            self.state = 545
            localctx.name = self.type_identifier()
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 546
                self.match(OParser.LPAR)
                self.state = 547
                localctx.attrs = self.attribute_identifier_list()
                self.state = 548
                self.match(OParser.RPAR)


            self.state = 552
            localctx.methods = self.category_method_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_derived_list

     
        def copyFrom(self, ctx):
            super(OParser.Derived_listContext, self).copyFrom(ctx)


    class DerivedListItemContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Derived_listContext)
            super(OParser.DerivedListItemContext, self).__init__(parser)
            self.items = None # Derived_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def derived_list(self):
            return self.getTypedRuleContext(OParser.Derived_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDerivedListItem"):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerivedListItem"):
                listener.exitDerivedListItem(self)


    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Derived_listContext)
            super(OParser.DerivedListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDerivedList"):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerivedList"):
                listener.exitDerivedList(self)



    def derived_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Derived_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_derived_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.DerivedListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 555
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 562
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.DerivedListItemContext(self, OParser.Derived_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_derived_list)
                    self.state = 557
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 558
                    self.match(OParser.COMMA)
                    self.state = 559
                    localctx.item = self.type_identifier() 
                self.state = 564
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_method_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_method_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_category_method_list

     
        def copyFrom(self, ctx):
            super(OParser.Category_method_listContext, self).copyFrom(ctx)



    class EmptyCategoryMethodListContext(Category_method_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_method_listContext)
            super(OParser.EmptyCategoryMethodListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterEmptyCategoryMethodList"):
                listener.enterEmptyCategoryMethodList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEmptyCategoryMethodList"):
                listener.exitEmptyCategoryMethodList(self)


    class CurlyCategoryMethodListContext(Category_method_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_method_listContext)
            super(OParser.CurlyCategoryMethodListContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Member_method_declaration_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCurlyCategoryMethodList"):
                listener.enterCurlyCategoryMethodList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCurlyCategoryMethodList"):
                listener.exitCurlyCategoryMethodList(self)



    def category_method_list(self):

        localctx = OParser.Category_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_category_method_list)
        self._la = 0 # Token type
        try:
            self.state = 571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SEMI]:
                localctx = OParser.EmptyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(OParser.LCURL)
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ABSTRACT - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.METHOD - 113)) | (1 << (OParser.OPERATOR - 113)) | (1 << (OParser.SETTER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)))) != 0):
                    self.state = 567
                    localctx.items = self.member_method_declaration_list()


                self.state = 570
                self.match(OParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypedefContext
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.stmts = None # Statement_listContext

        def OPERATOR(self):
            return self.getToken(OParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def operator(self):
            return self.getTypedRuleContext(OParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(OParser.Operator_argumentContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_method_declaration"):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_method_declaration"):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = OParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 573
                localctx.typ = self.typedef(0)


            self.state = 576
            self.match(OParser.OPERATOR)
            self.state = 577
            localctx.op = self.operator()
            self.state = 578
            self.match(OParser.LPAR)
            self.state = 579
            localctx.arg = self.operator_argument()
            self.state = 580
            self.match(OParser.RPAR)
            self.state = 581
            self.match(OParser.LCURL)
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 582
                localctx.stmts = self.statement_list()


            self.state = 585
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def SETTER(self):
            return self.getToken(OParser.SETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSetter_method_declaration"):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetter_method_declaration"):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = OParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_setter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(OParser.SETTER)
            self.state = 588
            localctx.name = self.variable_identifier()
            self.state = 589
            self.match(OParser.LCURL)
            self.state = 591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 590
                localctx.stmts = self.statement_list()


            self.state = 593
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_setter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def SETTER(self):
            return self.getToken(OParser.SETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_setter_declaration"):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_setter_declaration"):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = OParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 595
                self.match(OParser.NATIVE)


            self.state = 598
            self.match(OParser.SETTER)
            self.state = 599
            localctx.name = self.variable_identifier()
            self.state = 600
            self.match(OParser.LCURL)
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 601
                localctx.stmts = self.native_statement_list()


            self.state = 604
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def GETTER(self):
            return self.getToken(OParser.GETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterGetter_method_declaration"):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGetter_method_declaration"):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = OParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_getter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(OParser.GETTER)
            self.state = 607
            localctx.name = self.variable_identifier()
            self.state = 608
            self.match(OParser.LCURL)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 609
                localctx.stmts = self.statement_list()


            self.state = 612
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_getter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def GETTER(self):
            return self.getToken(OParser.GETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_getter_declaration"):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_getter_declaration"):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = OParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 614
                self.match(OParser.NATIVE)


            self.state = 617
            self.match(OParser.GETTER)
            self.state = 618
            localctx.name = self.variable_identifier()
            self.state = 619
            self.match(OParser.LCURL)
            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 620
                localctx.stmts = self.native_statement_list()


            self.state = 623
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(OParser.RESOURCE, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_resource_declaration"):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_resource_declaration"):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = OParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 625
                self.match(OParser.STORABLE)


            self.state = 628
            self.match(OParser.NATIVE)
            self.state = 629
            self.match(OParser.RESOURCE)
            self.state = 630
            localctx.name = self.type_identifier()
            self.state = 635
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 631
                self.match(OParser.LPAR)
                self.state = 632
                localctx.attrs = self.attribute_identifier_list()
                self.state = 633
                self.match(OParser.RPAR)


            self.state = 637
            self.match(OParser.LCURL)
            self.state = 638
            localctx.bindings = self.native_category_bindings()
            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.METHOD - 113)) | (1 << (OParser.NATIVE - 113)) | (1 << (OParser.SETTER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)))) != 0):
                self.state = 639
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 642
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_declaration"):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_declaration"):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = OParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 644
                self.match(OParser.STORABLE)


            self.state = 647
            self.match(OParser.NATIVE)
            self.state = 648
            self.match(OParser.CATEGORY)
            self.state = 649
            localctx.name = self.type_identifier()
            self.state = 654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 650
                self.match(OParser.LPAR)
                self.state = 651
                localctx.attrs = self.attribute_identifier_list()
                self.state = 652
                self.match(OParser.RPAR)


            self.state = 656
            self.match(OParser.LCURL)
            self.state = 657
            localctx.bindings = self.native_category_bindings()
            self.state = 659
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.METHOD - 113)) | (1 << (OParser.NATIVE - 113)) | (1 << (OParser.SETTER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)))) != 0):
                self.state = 658
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 661
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def BINDINGS(self):
            return self.getToken(OParser.BINDINGS, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(OParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_bindings"):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_bindings"):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = OParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 663
            self.match(OParser.CATEGORY)
            self.state = 664
            self.match(OParser.BINDINGS)
            self.state = 665
            self.match(OParser.LCURL)
            self.state = 666
            localctx.items = self.native_category_binding_list(0)
            self.state = 667
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(OParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_binding_listContext)
            super(OParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def native_category_binding_list(self):
            return self.getTypedRuleContext(OParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingListItem"):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingListItem"):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_binding_listContext)
            super(OParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def native_category_binding(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingList"):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingList"):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 670
            localctx.item = self.native_category_binding()
            self.state = 671
            self.match(OParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 679
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeCategoryBindingListItemContext(self, OParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 673
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 674
                    localctx.item = self.native_category_binding()
                    self.state = 675
                    self.match(OParser.SEMI) 
                self.state = 681
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypedefContext
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext

        def ABSTRACT(self):
            return self.getToken(OParser.ABSTRACT, 0)

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAbstract_method_declaration"):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAbstract_method_declaration"):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = OParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.match(OParser.ABSTRACT)
            self.state = 684
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 683
                localctx.typ = self.typedef(0)


            self.state = 686
            self.match(OParser.METHOD)
            self.state = 687
            localctx.name = self.method_identifier()
            self.state = 688
            self.match(OParser.LPAR)
            self.state = 690
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.MUTABLE - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 689
                localctx.args = self.argument_list()


            self.state = 692
            self.match(OParser.RPAR)
            self.state = 693
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypedefContext
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.stmts = None # Statement_listContext

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_method_declaration"):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_method_declaration"):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = OParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 695
                localctx.typ = self.typedef(0)


            self.state = 698
            self.match(OParser.METHOD)
            self.state = 699
            localctx.name = self.method_identifier()
            self.state = 700
            self.match(OParser.LPAR)
            self.state = 702
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.MUTABLE - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 701
                localctx.args = self.argument_list()


            self.state = 704
            self.match(OParser.RPAR)
            self.state = 705
            self.match(OParser.LCURL)
            self.state = 707
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 706
                localctx.stmts = self.statement_list()


            self.state = 709
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.stmts = None # Native_statement_listContext

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_method_declaration"):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_method_declaration"):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = OParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 711
                localctx.typ = self.category_or_any_type()


            self.state = 715
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 714
                self.match(OParser.NATIVE)


            self.state = 717
            self.match(OParser.METHOD)
            self.state = 718
            localctx.name = self.method_identifier()
            self.state = 719
            self.match(OParser.LPAR)
            self.state = 721
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (OParser.MUTABLE - 116)) | (1 << (OParser.TYPE_IDENTIFIER - 116)) | (1 << (OParser.VARIABLE_IDENTIFIER - 116)))) != 0):
                self.state = 720
                localctx.args = self.argument_list()


            self.state = 723
            self.match(OParser.RPAR)
            self.state = 724
            self.match(OParser.LCURL)
            self.state = 725
            localctx.stmts = self.native_statement_list()
            self.state = 726
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.LCURL)
            else:
                return self.getToken(OParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.RCURL)
            else:
                return self.getToken(OParser.RCURL, i)

        def VERIFYING(self):
            return self.getToken(OParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def assertion_list(self):
            return self.getTypedRuleContext(OParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterTest_method_declaration"):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTest_method_declaration"):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = OParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 728
            self.match(OParser.TEST)
            self.state = 729
            self.match(OParser.METHOD)
            self.state = 730
            localctx.name = self.match(OParser.TEXT_LITERAL)
            self.state = 731
            self.match(OParser.LPAR)
            self.state = 732
            self.match(OParser.RPAR)
            self.state = 733
            self.match(OParser.LCURL)
            self.state = 734
            localctx.stmts = self.statement_list()
            self.state = 735
            self.match(OParser.RCURL)
            self.state = 736
            self.match(OParser.VERIFYING)
            self.state = 744
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.LCURL]:
                self.state = 737
                self.match(OParser.LCURL)
                self.state = 738
                localctx.exps = self.assertion_list()
                self.state = 739
                self.match(OParser.RCURL)
                pass
            elif token in [OParser.SYMBOL_IDENTIFIER]:
                self.state = 741
                localctx.error = self.symbol_identifier()
                self.state = 742
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssertionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assertion

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion"):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion"):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = OParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            localctx.exp = self.expression(0)
            self.state = 747
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_identifier_listContext
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_typed_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterTyped_argument"):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTyped_argument"):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = OParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            localctx.typ = self.category_or_any_type()
            self.state = 754
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 750
                self.match(OParser.LPAR)
                self.state = 751
                localctx.attrs = self.attribute_identifier_list()
                self.state = 752
                self.match(OParser.RPAR)


            self.state = 756
            localctx.name = self.variable_identifier()
            self.state = 759
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 757
                self.match(OParser.EQ)
                self.state = 758
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_or_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Statement_or_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_statement_or_list

     
        def copyFrom(self, ctx):
            super(OParser.Statement_or_listContext, self).copyFrom(ctx)



    class CurlyStatementListContext(Statement_or_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_or_listContext)
            super(OParser.CurlyStatementListContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCurlyStatementList"):
                listener.enterCurlyStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCurlyStatementList"):
                listener.exitCurlyStatementList(self)


    class SingleStatementContext(Statement_or_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_or_listContext)
            super(OParser.SingleStatementContext, self).__init__(parser)
            self.stmt = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(OParser.StatementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingleStatement"):
                listener.enterSingleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleStatement"):
                listener.exitSingleStatement(self)



    def statement_or_list(self):

        localctx = OParser.Statement_or_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement_or_list)
        try:
            self.state = 768
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.COMMENT, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.HTML, OParser.BREAK, OParser.DELETE, OParser.DO, OParser.FLUSH, OParser.FOR, OParser.IF, OParser.METHOD, OParser.RETURN, OParser.STORE, OParser.SWITCH, OParser.THROW, OParser.TRY, OParser.WITH, OParser.WHILE, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.SingleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 761
                localctx.stmt = self.statement()
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyStatementListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 762
                self.match(OParser.LCURL)
                self.state = 766
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 763
                    localctx.items = self.statement_list()
                    self.state = 764
                    self.match(OParser.RCURL)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(OParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(OParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCommentStatement"):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCommentStatement"):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(OParser.Store_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterStoreStatement"):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStoreStatement"):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(OParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithSingletonStatement"):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithSingletonStatement"):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(OParser.Write_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWriteStatement"):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWriteStatement"):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(OParser.While_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWhileStatement"):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhileStatement"):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(OParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithResourceStatement"):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithResourceStatement"):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(OParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRaiseStatement"):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaiseStatement"):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(OParser.Break_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBreakStatement"):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreakStatement"):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(OParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignInstanceStatement"):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignInstanceStatement"):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(OParser.If_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIfStatement"):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIfStatement"):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(OParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSwitchStatement"):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitchStatement"):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(OParser.Try_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTryStatement"):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTryStatement"):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def method_call(self):
            return self.getTypedRuleContext(OParser.Method_callContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodCallStatement"):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodCallStatement"):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(OParser.Return_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReturnStatement"):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturnStatement"):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(OParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignTupleStatement"):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignTupleStatement"):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureStatement"):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureStatement"):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(OParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFlushStatement"):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlushStatement"):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(OParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDoWhileStatement"):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDoWhileStatement"):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(OParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterForEachStatement"):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitForEachStatement"):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = OParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 770
                localctx.stmt = self.method_call()
                self.state = 771
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                localctx = OParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = OParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 774
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = OParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 775
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = OParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 776
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = OParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 777
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = OParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 778
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = OParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 779
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = OParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 780
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = OParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 781
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = OParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 782
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = OParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 783
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = OParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 784
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 14:
                localctx = OParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 785
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 15:
                localctx = OParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 786
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = OParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 787
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = OParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 788
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = OParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 789
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = OParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 790
                localctx.decl = self.comment_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Flush_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(OParser.FLUSH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def getRuleIndex(self):
            return OParser.RULE_flush_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFlush_statement"):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlush_statement"):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = OParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.match(OParser.FLUSH)
            self.state = 794
            self.match(OParser.LPAR)
            self.state = 795
            self.match(OParser.RPAR)
            self.state = 796
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(OParser.DELETE, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(OParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(OParser.STORE, 0)

        def AND(self):
            return self.getToken(OParser.AND, 0)

        def getRuleIndex(self):
            return OParser.RULE_store_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterStore_statement"):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStore_statement"):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = OParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_store_statement)
        try:
            self.state = 821
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 798
                self.match(OParser.DELETE)
                self.state = 799
                self.match(OParser.LPAR)
                self.state = 800
                localctx.to_del = self.expression_list()
                self.state = 801
                self.match(OParser.RPAR)
                self.state = 802
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 804
                self.match(OParser.STORE)
                self.state = 805
                self.match(OParser.LPAR)
                self.state = 806
                localctx.to_add = self.expression_list()
                self.state = 807
                self.match(OParser.RPAR)
                self.state = 808
                self.match(OParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 810
                self.match(OParser.DELETE)
                self.state = 811
                self.match(OParser.LPAR)
                self.state = 812
                localctx.to_del = self.expression_list()
                self.state = 813
                self.match(OParser.RPAR)
                self.state = 814
                self.match(OParser.AND)
                self.state = 815
                self.match(OParser.STORE)
                self.state = 816
                self.match(OParser.LPAR)
                self.state = 817
                localctx.to_add = self.expression_list()
                self.state = 818
                self.match(OParser.RPAR)
                self.state = 819
                self.match(OParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_resource_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_or_listContext

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def assign_variable_statement(self):
            return self.getTypedRuleContext(OParser.Assign_variable_statementContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_resource_statement"):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_resource_statement"):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = OParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 823
            self.match(OParser.WITH)
            self.state = 824
            self.match(OParser.LPAR)
            self.state = 825
            localctx.stmt = self.assign_variable_statement()
            self.state = 826
            self.match(OParser.RPAR)
            self.state = 827
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_singleton_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_or_listContext

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_singleton_statement"):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_singleton_statement"):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = OParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(OParser.WITH)
            self.state = 830
            self.match(OParser.LPAR)
            self.state = 831
            localctx.typ = self.type_identifier()
            self.state = 832
            self.match(OParser.RPAR)
            self.state = 833
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(OParser.SWITCH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(OParser.Switch_case_statement_listContext,0)


        def DEFAULT(self):
            return self.getToken(OParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_switch_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_statement"):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_statement"):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = OParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 835
            self.match(OParser.SWITCH)
            self.state = 836
            self.match(OParser.LPAR)
            self.state = 837
            localctx.exp = self.expression(0)
            self.state = 838
            self.match(OParser.RPAR)
            self.state = 839
            self.match(OParser.LCURL)
            self.state = 840
            localctx.cases = self.switch_case_statement_list()
            self.state = 846
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DEFAULT:
                self.state = 841
                self.match(OParser.DEFAULT)
                self.state = 842
                self.match(OParser.COLON)
                self.state = 844
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 843
                    localctx.stmts = self.statement_list()




            self.state = 848
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(OParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Switch_case_statementContext)
            super(OParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(OParser.CASE, 0)
        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAtomicSwitchCase"):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomicSwitchCase"):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Switch_case_statementContext)
            super(OParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(OParser.CASE, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def literal_collection(self):
            return self.getTypedRuleContext(OParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCollectionSwitchCase"):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollectionSwitchCase"):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = OParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_case_statement)
        self._la = 0 # Token type
        try:
            self.state = 863
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = OParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 850
                self.match(OParser.CASE)
                self.state = 851
                localctx.exp = self.atomic_literal()
                self.state = 852
                self.match(OParser.COLON)
                self.state = 854
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 853
                    localctx.stmts = self.statement_list()


                pass

            elif la_ == 2:
                localctx = OParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 856
                self.match(OParser.CASE)
                self.state = 857
                self.match(OParser.IN)
                self.state = 858
                localctx.exp = self.literal_collection()
                self.state = 859
                self.match(OParser.COLON)
                self.state = 861
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 860
                    localctx.stmts = self.statement_list()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_each_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_or_listContext

        def FOR(self):
            return self.getToken(OParser.FOR, 0)

        def EACH(self):
            return self.getToken(OParser.EACH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def IN(self):
            return self.getToken(OParser.IN, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)

        def getRuleIndex(self):
            return OParser.RULE_for_each_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFor_each_statement"):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFor_each_statement"):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = OParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 865
            self.match(OParser.FOR)
            self.state = 866
            self.match(OParser.EACH)
            self.state = 867
            self.match(OParser.LPAR)
            self.state = 868
            localctx.name1 = self.variable_identifier()
            self.state = 871
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 869
                self.match(OParser.COMMA)
                self.state = 870
                localctx.name2 = self.variable_identifier()


            self.state = 873
            self.match(OParser.IN)
            self.state = 874
            localctx.source = self.expression(0)
            self.state = 875
            self.match(OParser.RPAR)
            self.state = 876
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(OParser.DO, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def WHILE(self):
            return self.getToken(OParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_do_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterDo_while_statement"):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDo_while_statement"):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = OParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            self.match(OParser.DO)
            self.state = 879
            self.match(OParser.LCURL)
            self.state = 881
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 880
                localctx.stmts = self.statement_list()


            self.state = 883
            self.match(OParser.RCURL)
            self.state = 884
            self.match(OParser.WHILE)
            self.state = 885
            self.match(OParser.LPAR)
            self.state = 886
            localctx.exp = self.expression(0)
            self.state = 887
            self.match(OParser.RPAR)
            self.state = 888
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext

        def WHILE(self):
            return self.getToken(OParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWhile_statement"):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhile_statement"):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = OParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 890
            self.match(OParser.WHILE)
            self.state = 891
            self.match(OParser.LPAR)
            self.state = 892
            localctx.exp = self.expression(0)
            self.state = 893
            self.match(OParser.RPAR)
            self.state = 894
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_or_listContext

        def IF(self):
            return self.getToken(OParser.IF, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_or_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Statement_or_listContext)
            else:
                return self.getTypedRuleContext(OParser.Statement_or_listContext,i)


        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(OParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_if_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterIf_statement"):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf_statement"):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = OParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 896
            self.match(OParser.IF)
            self.state = 897
            self.match(OParser.LPAR)
            self.state = 898
            localctx.exp = self.expression(0)
            self.state = 899
            self.match(OParser.RPAR)
            self.state = 900
            localctx.stmts = self.statement_or_list()
            self.state = 902
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 901
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 906
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 904
                self.match(OParser.ELSE)
                self.state = 905
                localctx.elseStmts = self.statement_or_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_if_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(OParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Else_if_statement_listContext)
            super(OParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)
        def IF(self):
            return self.getToken(OParser.IF, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementList"):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementList"):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Else_if_statement_listContext)
            super(OParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)
        def IF(self):
            return self.getToken(OParser.IF, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def else_if_statement_list(self):
            return self.getTypedRuleContext(OParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementListItem"):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementListItem"):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 909
            self.match(OParser.ELSE)
            self.state = 910
            self.match(OParser.IF)
            self.state = 911
            self.match(OParser.LPAR)
            self.state = 912
            localctx.exp = self.expression(0)
            self.state = 913
            self.match(OParser.RPAR)
            self.state = 914
            localctx.stmts = self.statement_or_list()
            self._ctx.stop = self._input.LT(-1)
            self.state = 926
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ElseIfStatementListItemContext(self, OParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 916
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 917
                    self.match(OParser.ELSE)
                    self.state = 918
                    self.match(OParser.IF)
                    self.state = 919
                    self.match(OParser.LPAR)
                    self.state = 920
                    localctx.exp = self.expression(0)
                    self.state = 921
                    self.match(OParser.RPAR)
                    self.state = 922
                    localctx.stmts = self.statement_or_list() 
                self.state = 928
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def THROW(self):
            return self.getToken(OParser.THROW, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_raise_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterRaise_statement"):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaise_statement"):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = OParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 929
            self.match(OParser.THROW)
            self.state = 930
            localctx.exp = self.expression(0)
            self.state = 931
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Try_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(OParser.TRY, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.LCURL)
            else:
                return self.getToken(OParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.RCURL)
            else:
                return self.getToken(OParser.RCURL, i)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def FINALLY(self):
            return self.getToken(OParser.FINALLY, 0)

        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(OParser.Statement_listContext,i)


        def catch_statement_list(self):
            return self.getTypedRuleContext(OParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_try_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterTry_statement"):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTry_statement"):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = OParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 933
            self.match(OParser.TRY)
            self.state = 934
            self.match(OParser.LPAR)
            self.state = 935
            localctx.name = self.variable_identifier()
            self.state = 936
            self.match(OParser.RPAR)
            self.state = 937
            self.match(OParser.LCURL)
            self.state = 939
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 938
                localctx.stmts = self.statement_list()


            self.state = 941
            self.match(OParser.RCURL)
            self.state = 943
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 942
                localctx.handlers = self.catch_statement_list()


            self.state = 954
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 945
                self.match(OParser.CATCH)
                self.state = 946
                self.match(OParser.LPAR)
                self.state = 947
                self.match(OParser.ANY)
                self.state = 948
                self.match(OParser.RPAR)
                self.state = 949
                self.match(OParser.LCURL)
                self.state = 951
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 950
                    localctx.anyStmts = self.statement_list()


                self.state = 953
                self.match(OParser.RCURL)


            self.state = 962
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 956
                self.match(OParser.FINALLY)
                self.state = 957
                self.match(OParser.LCURL)
                self.state = 959
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 958
                    localctx.finalStmts = self.statement_list()


                self.state = 961
                self.match(OParser.RCURL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(OParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Catch_statementContext)
            super(OParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchAtomicStatement"):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchAtomicStatement"):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Catch_statementContext)
            super(OParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(OParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchCollectionStatement"):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchCollectionStatement"):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = OParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_catch_statement)
        self._la = 0 # Token type
        try:
            self.state = 985
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = OParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 964
                self.match(OParser.CATCH)
                self.state = 965
                self.match(OParser.LPAR)
                self.state = 966
                localctx.name = self.symbol_identifier()
                self.state = 967
                self.match(OParser.RPAR)
                self.state = 968
                self.match(OParser.LCURL)
                self.state = 970
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 969
                    localctx.stmts = self.statement_list()


                self.state = 972
                self.match(OParser.RCURL)
                pass

            elif la_ == 2:
                localctx = OParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 974
                self.match(OParser.CATCH)
                self.state = 975
                self.match(OParser.IN)
                self.state = 976
                self.match(OParser.LPAR)
                self.state = 977
                localctx.exp = self.symbol_list()
                self.state = 978
                self.match(OParser.RPAR)
                self.state = 979
                self.match(OParser.LCURL)
                self.state = 981
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                    self.state = 980
                    localctx.stmts = self.statement_list()


                self.state = 983
                self.match(OParser.RCURL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(OParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def getRuleIndex(self):
            return OParser.RULE_break_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterBreak_statement"):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreak_statement"):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = OParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 987
            self.match(OParser.BREAK)
            self.state = 988
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_return_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterReturn_statement"):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturn_statement"):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = OParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 990
            self.match(OParser.RETURN)
            self.state = 992
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 991
                localctx.exp = self.expression(0)


            self.state = 994
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(OParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_call

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_call"):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_call"):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = OParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 996
            localctx.method = self.method_selector()
            self.state = 997
            self.match(OParser.LPAR)
            self.state = 999
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 998
                localctx.args = self.argument_assignment_list(0)


            self.state = 1001
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(OParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_selectorContext)
            super(OParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(OParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodParent"):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodParent"):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_selectorContext)
            super(OParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodName"):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodName"):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = OParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_selector)
        try:
            self.state = 1008
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1003
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1004
                localctx.parent = self.callable_parent(0)
                self.state = 1005
                self.match(OParser.DOT)
                self.state = 1006
                localctx.name = self.method_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Callable_parentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(OParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_parentContext)
            super(OParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(OParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(OParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableSelector"):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableSelector"):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_parentContext)
            super(OParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableRoot"):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableRoot"):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1011
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1017
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CallableSelectorContext(self, OParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 1013
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1014
                    localctx.select = self.callable_selector() 
                self.state = 1019
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(OParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_selectorContext)
            super(OParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableItemSelector"):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableItemSelector"):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_selectorContext)
            super(OParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableMemberSelector"):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableMemberSelector"):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = OParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_callable_selector)
        try:
            self.state = 1026
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1020
                self.match(OParser.DOT)
                self.state = 1021
                localctx.name = self.variable_identifier()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1022
                self.match(OParser.LBRAK)
                self.state = 1023
                localctx.exp = self.expression(0)
                self.state = 1024
                self.match(OParser.RBRAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(OParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(OParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIntDivideExpression"):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntDivideExpression"):
                listener.exitIntDivideExpression(self)


    class HasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.HasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ANY(self):
            return self.getToken(OParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAnyExpression"):
                listener.enterHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAnyExpression"):
                listener.exitHasAnyExpression(self)


    class HasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.HasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasExpression"):
                listener.enterHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasExpression"):
                listener.exitHasExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.TernaryExpressionContext, self).__init__(parser)
            self.test = None # ExpressionContext
            self.ifTrue = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def QMARK(self):
            return self.getToken(OParser.QMARK, 0)
        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterTernaryExpression"):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTernaryExpression"):
                listener.exitTernaryExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(OParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotEqualsExpression"):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotEqualsExpression"):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterInExpression"):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInExpression"):
                listener.exitInExpression(self)


    class IsAnExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsAnExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # An_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def an_expression(self):
            return self.getTypedRuleContext(OParser.An_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsAnExpression"):
                listener.enterIsAnExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsAnExpression"):
                listener.exitIsAnExpression(self)


    class JsxExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.JsxExpressionContext, self).__init__(parser)
            self.exp = None # Jsx_expressionContext
            self.copyFrom(ctx)

        def jsx_expression(self):
            return self.getTypedRuleContext(OParser.Jsx_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxExpression"):
                listener.enterJsxExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxExpression"):
                listener.exitJsxExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def XMARK(self):
            return self.getToken(OParser.XMARK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotExpression"):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotExpression"):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(OParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanExpression"):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanExpression"):
                listener.exitGreaterThanExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def PIPE2(self):
            return self.getToken(OParser.PIPE2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOrExpression"):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrExpression"):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeExpression"):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeExpression"):
                listener.exitCodeExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(OParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanOrEqualExpression"):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanOrEqualExpression"):
                listener.exitLessThanOrEqualExpression(self)


    class NotHasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotHasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ANY(self):
            return self.getToken(OParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAnyExpression"):
                listener.enterNotHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAnyExpression"):
                listener.exitNotHasAnyExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AMP2(self):
            return self.getToken(OParser.AMP2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndExpression"):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndExpression"):
                listener.exitAndExpression(self)


    class NotHasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotHasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasExpression"):
                listener.enterNotHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasExpression"):
                listener.exitNotHasExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(OParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureExpression"):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureExpression"):
                listener.exitClosureExpression(self)


    class NotHasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotHasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAllExpression"):
                listener.enterNotHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAllExpression"):
                listener.exitNotHasAllExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterContainsExpression"):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContainsExpression"):
                listener.exitContainsExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotContainsExpression"):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotContainsExpression"):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(OParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterMultiplyExpression"):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiplyExpression"):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(OParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterRoughlyEqualsExpression"):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRoughlyEqualsExpression"):
                listener.exitRoughlyEqualsExpression(self)


    class IsNotAnExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsNotAnExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # An_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def an_expression(self):
            return self.getTypedRuleContext(OParser.An_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsNotAnExpression"):
                listener.enterIsNotAnExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotAnExpression"):
                listener.exitIsNotAnExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(OParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExecuteExpression"):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExecuteExpression"):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(OParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodExpression"):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodExpression"):
                listener.exitMethodExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(OParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanOrEqualExpression"):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanOrEqualExpression"):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotInExpression"):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotInExpression"):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(OParser.FOR, 0)
        def EACH(self):
            return self.getToken(OParser.EACH, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorExpression"):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorExpression"):
                listener.exitIteratorExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsNotExpression"):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotExpression"):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(OParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterDivideExpression"):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivideExpression"):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsExpression"):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsExpression"):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMinusExpression"):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinusExpression"):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(OParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAddExpression"):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddExpression"):
                listener.exitAddExpression(self)


    class HasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.HasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAllExpression"):
                listener.enterHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAllExpression"):
                listener.exitHasAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(OParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterInstanceExpression"):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInstanceExpression"):
                listener.exitInstanceExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.CastExpressionContext, self).__init__(parser)
            self.right = None # Category_or_any_typeContext
            self.left = None # ExpressionContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCastExpression"):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCastExpression"):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(OParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterModuloExpression"):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModuloExpression"):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(OParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanExpression"):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanExpression"):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(OParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterEqualsExpression"):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEqualsExpression"):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1052
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                localctx = OParser.JsxExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1029
                localctx.exp = self.jsx_expression()
                pass

            elif la_ == 2:
                localctx = OParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1030
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 3:
                localctx = OParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1031
                localctx.exp = self.method_expression()
                pass

            elif la_ == 4:
                localctx = OParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1032
                self.match(OParser.MINUS)
                self.state = 1033
                localctx.exp = self.expression(36)
                pass

            elif la_ == 5:
                localctx = OParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1034
                self.match(OParser.XMARK)
                self.state = 1035
                localctx.exp = self.expression(35)
                pass

            elif la_ == 6:
                localctx = OParser.CastExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1036
                self.match(OParser.LPAR)
                self.state = 1037
                localctx.right = self.category_or_any_type()
                self.state = 1038
                self.match(OParser.RPAR)
                self.state = 1039
                localctx.left = self.expression(29)
                pass

            elif la_ == 7:
                localctx = OParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1041
                self.match(OParser.CODE)
                self.state = 1042
                self.match(OParser.LPAR)
                self.state = 1043
                localctx.exp = self.expression(0)
                self.state = 1044
                self.match(OParser.RPAR)
                pass

            elif la_ == 8:
                localctx = OParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1046
                self.match(OParser.EXECUTE)
                self.state = 1047
                self.match(OParser.LPAR)
                self.state = 1048
                localctx.name = self.variable_identifier()
                self.state = 1049
                self.match(OParser.RPAR)
                pass

            elif la_ == 9:
                localctx = OParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1051
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1168
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        localctx = OParser.MultiplyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1054
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 1055
                        self.multiply()
                        self.state = 1056
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 2:
                        localctx = OParser.DivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1058
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 1059
                        self.divide()
                        self.state = 1060
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 3:
                        localctx = OParser.ModuloExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1062
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1063
                        self.modulo()
                        self.state = 1064
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 4:
                        localctx = OParser.IntDivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1066
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1067
                        self.idivide()
                        self.state = 1068
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 5:
                        localctx = OParser.AddExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1070
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1071
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==OParser.PLUS or _la==OParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 1072
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 6:
                        localctx = OParser.LessThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1073
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1074
                        self.match(OParser.LT)
                        self.state = 1075
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 7:
                        localctx = OParser.LessThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1076
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1077
                        self.match(OParser.LTE)
                        self.state = 1078
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 8:
                        localctx = OParser.GreaterThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1079
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1080
                        self.match(OParser.GT)
                        self.state = 1081
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 9:
                        localctx = OParser.GreaterThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1082
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1083
                        self.match(OParser.GTE)
                        self.state = 1084
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 10:
                        localctx = OParser.IsNotExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1085
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1086
                        self.match(OParser.IS)
                        self.state = 1087
                        self.match(OParser.NOT)
                        self.state = 1088
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 11:
                        localctx = OParser.IsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1089
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1090
                        self.match(OParser.IS)
                        self.state = 1091
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 12:
                        localctx = OParser.EqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1092
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1093
                        self.match(OParser.EQ2)
                        self.state = 1094
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 13:
                        localctx = OParser.NotEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1095
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1096
                        self.match(OParser.XEQ)
                        self.state = 1097
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 14:
                        localctx = OParser.RoughlyEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1098
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1099
                        self.match(OParser.TEQ)
                        self.state = 1100
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 15:
                        localctx = OParser.ContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1101
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1102
                        self.match(OParser.CONTAINS)
                        self.state = 1103
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 16:
                        localctx = OParser.InExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1104
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1105
                        self.match(OParser.IN)
                        self.state = 1106
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 17:
                        localctx = OParser.HasExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1107
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1108
                        self.match(OParser.HAS)
                        self.state = 1109
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 18:
                        localctx = OParser.HasAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1110
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1111
                        self.match(OParser.HAS)
                        self.state = 1112
                        self.match(OParser.ALL)
                        self.state = 1113
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 19:
                        localctx = OParser.HasAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1114
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1115
                        self.match(OParser.HAS)
                        self.state = 1116
                        self.match(OParser.ANY)
                        self.state = 1117
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 20:
                        localctx = OParser.NotContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1118
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1119
                        self.match(OParser.NOT)
                        self.state = 1120
                        self.match(OParser.CONTAINS)
                        self.state = 1121
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 21:
                        localctx = OParser.NotInExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1122
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1123
                        self.match(OParser.NOT)
                        self.state = 1124
                        self.match(OParser.IN)
                        self.state = 1125
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 22:
                        localctx = OParser.NotHasExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1126
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1127
                        self.match(OParser.NOT)
                        self.state = 1128
                        self.match(OParser.HAS)
                        self.state = 1129
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 23:
                        localctx = OParser.NotHasAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1130
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1131
                        self.match(OParser.NOT)
                        self.state = 1132
                        self.match(OParser.HAS)
                        self.state = 1133
                        self.match(OParser.ALL)
                        self.state = 1134
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 24:
                        localctx = OParser.NotHasAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1135
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1136
                        self.match(OParser.NOT)
                        self.state = 1137
                        self.match(OParser.HAS)
                        self.state = 1138
                        self.match(OParser.ANY)
                        self.state = 1139
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 25:
                        localctx = OParser.OrExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1140
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1141
                        self.match(OParser.PIPE2)
                        self.state = 1142
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 26:
                        localctx = OParser.AndExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1143
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1144
                        self.match(OParser.AMP2)
                        self.state = 1145
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 27:
                        localctx = OParser.TernaryExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.test = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1146
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1147
                        self.match(OParser.QMARK)
                        self.state = 1148
                        localctx.ifTrue = self.expression(0)
                        self.state = 1149
                        self.match(OParser.COLON)
                        self.state = 1150
                        localctx.ifFalse = self.expression(6)
                        pass

                    elif la_ == 28:
                        localctx = OParser.IsNotAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1152
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1153
                        self.match(OParser.IS)
                        self.state = 1154
                        self.match(OParser.NOT)
                        self.state = 1155
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 29:
                        localctx = OParser.IsAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1156
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1157
                        self.match(OParser.IS)
                        self.state = 1158
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 30:
                        localctx = OParser.IteratorExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1159
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1160
                        self.match(OParser.FOR)
                        self.state = 1161
                        self.match(OParser.EACH)
                        self.state = 1162
                        self.match(OParser.LPAR)
                        self.state = 1163
                        localctx.name = self.variable_identifier()
                        self.state = 1164
                        self.match(OParser.IN)
                        self.state = 1165
                        localctx.source = self.expression(0)
                        self.state = 1166
                        self.match(OParser.RPAR)
                        pass

             
                self.state = 1172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class An_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.An_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return OParser.RULE_an_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterAn_expression"):
                listener.enterAn_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAn_expression"):
                listener.exitAn_expression(self)




    def an_expression(self):

        localctx = OParser.An_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_an_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1173
            if not self.willBeAOrAn():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBeAOrAn()")
            self.state = 1174
            self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1175
            localctx.typ = self.category_or_any_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_closure_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterClosure_expression"):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosure_expression"):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = OParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1177
            localctx.name = self.type_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(OParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Instance_expressionContext)
            super(OParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Selector_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(OParser.Instance_expressionContext,0)

        def selector_expression(self):
            return self.getTypedRuleContext(OParser.Selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectorExpression"):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectorExpression"):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Instance_expressionContext)
            super(OParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(OParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectableExpression"):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectableExpression"):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1180
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.SelectorExpressionContext(self, OParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1182
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1183
                    localctx.selector = self.selector_expression() 
                self.state = 1188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blob_expression(self):
            return self.getTypedRuleContext(OParser.Blob_expressionContext,0)


        def document_expression(self):
            return self.getTypedRuleContext(OParser.Document_expressionContext,0)


        def filtered_list_expression(self):
            return self.getTypedRuleContext(OParser.Filtered_list_expressionContext,0)


        def fetch_store_expression(self):
            return self.getTypedRuleContext(OParser.Fetch_store_expressionContext,0)


        def read_all_expression(self):
            return self.getTypedRuleContext(OParser.Read_all_expressionContext,0)


        def read_one_expression(self):
            return self.getTypedRuleContext(OParser.Read_one_expressionContext,0)


        def sorted_expression(self):
            return self.getTypedRuleContext(OParser.Sorted_expressionContext,0)


        def method_call(self):
            return self.getTypedRuleContext(OParser.Method_callContext,0)


        def constructor_expression(self):
            return self.getTypedRuleContext(OParser.Constructor_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_expression"):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_expression"):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = OParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_method_expression)
        try:
            self.state = 1198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1189
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1190
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1191
                self.filtered_list_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1192
                self.fetch_store_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1193
                self.read_all_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1194
                self.read_one_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1195
                self.sorted_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1196
                self.method_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1197
                self.constructor_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Blob_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def getRuleIndex(self):
            return OParser.RULE_blob_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterBlob_expression"):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlob_expression"):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = OParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_blob_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1200
            self.match(OParser.BLOB)
            self.state = 1201
            self.match(OParser.LPAR)
            self.state = 1202
            self.expression(0)
            self.state = 1203
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_document_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterDocument_expression"):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocument_expression"):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = OParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self.match(OParser.DOCUMENT)
            self.state = 1206
            self.match(OParser.LPAR)
            self.state = 1208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1207
                self.expression(0)


            self.state = 1210
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def TO(self):
            return self.getToken(OParser.TO, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OParser.RULE_write_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWrite_statement"):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWrite_statement"):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = OParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1212
            self.match(OParser.WRITE)
            self.state = 1213
            self.match(OParser.LPAR)
            self.state = 1214
            localctx.what = self.expression(0)
            self.state = 1215
            self.match(OParser.RPAR)
            self.state = 1216
            self.match(OParser.TO)
            self.state = 1217
            localctx.target = self.expression(0)
            self.state = 1218
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filtered_list_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Filtered_list_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.predicate = None # ExpressionContext

        def FILTERED(self):
            return self.getToken(OParser.FILTERED, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_filtered_list_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterFiltered_list_expression"):
                listener.enterFiltered_list_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFiltered_list_expression"):
                listener.exitFiltered_list_expression(self)




    def filtered_list_expression(self):

        localctx = OParser.Filtered_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_filtered_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1220
            self.match(OParser.FILTERED)
            self.state = 1221
            self.match(OParser.LPAR)
            self.state = 1222
            localctx.source = self.expression(0)
            self.state = 1223
            self.match(OParser.RPAR)
            self.state = 1224
            self.match(OParser.WITH)
            self.state = 1225
            self.match(OParser.LPAR)
            self.state = 1226
            localctx.name = self.variable_identifier()
            self.state = 1227
            self.match(OParser.RPAR)
            self.state = 1228
            self.match(OParser.WHERE)
            self.state = 1229
            self.match(OParser.LPAR)
            self.state = 1230
            localctx.predicate = self.expression(0)
            self.state = 1231
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_store_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(OParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_store_expressionContext)
            super(OParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
        def ONE(self):
            return self.getToken(OParser.ONE, 0)
        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)
        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)
        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchOne"):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchOne"):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_store_expressionContext)
            super(OParser.FetchManyContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)
        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)
        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)
        def ORDER(self):
            return self.getToken(OParser.ORDER, 0)
        def BY(self):
            return self.getToken(OParser.BY, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def ROWS(self):
            return self.getToken(OParser.ROWS, 0)
        def TO(self):
            return self.getToken(OParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)

        def order_by_list(self):
            return self.getTypedRuleContext(OParser.Order_by_listContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchMany"):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchMany"):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = OParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = OParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1233
                self.match(OParser.FETCH)
                self.state = 1234
                self.match(OParser.ONE)
                self.state = 1239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 1235
                    self.match(OParser.LPAR)
                    self.state = 1236
                    localctx.typ = self.mutable_category_type()
                    self.state = 1237
                    self.match(OParser.RPAR)


                self.state = 1241
                self.match(OParser.WHERE)
                self.state = 1242
                self.match(OParser.LPAR)
                self.state = 1243
                localctx.predicate = self.expression(0)
                self.state = 1244
                self.match(OParser.RPAR)
                pass

            elif la_ == 2:
                localctx = OParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1246
                self.match(OParser.FETCH)
                self.state = 1267
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [OParser.ALL]:
                    self.state = 1247
                    self.match(OParser.ALL)
                    self.state = 1252
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                    if la_ == 1:
                        self.state = 1248
                        self.match(OParser.LPAR)
                        self.state = 1249
                        localctx.typ = self.mutable_category_type()
                        self.state = 1250
                        self.match(OParser.RPAR)


                    pass
                elif token in [OParser.LPAR, OParser.ROWS]:
                    self.state = 1258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==OParser.LPAR:
                        self.state = 1254
                        self.match(OParser.LPAR)
                        self.state = 1255
                        localctx.typ = self.mutable_category_type()
                        self.state = 1256
                        self.match(OParser.RPAR)


                    self.state = 1260
                    self.match(OParser.ROWS)
                    self.state = 1261
                    self.match(OParser.LPAR)
                    self.state = 1262
                    localctx.xstart = self.expression(0)
                    self.state = 1263
                    self.match(OParser.TO)
                    self.state = 1264
                    localctx.xstop = self.expression(0)
                    self.state = 1265
                    self.match(OParser.RPAR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1274
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                if la_ == 1:
                    self.state = 1269
                    self.match(OParser.WHERE)
                    self.state = 1270
                    self.match(OParser.LPAR)
                    self.state = 1271
                    localctx.predicate = self.expression(0)
                    self.state = 1272
                    self.match(OParser.RPAR)


                self.state = 1282
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                if la_ == 1:
                    self.state = 1276
                    self.match(OParser.ORDER)
                    self.state = 1277
                    self.match(OParser.BY)
                    self.state = 1278
                    self.match(OParser.LPAR)
                    self.state = 1279
                    localctx.orderby = self.order_by_list()
                    self.state = 1280
                    self.match(OParser.RPAR)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sorted_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(OParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(OParser.Instance_expressionContext,i)


        def DESC(self):
            return self.getToken(OParser.DESC, 0)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(OParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def getRuleIndex(self):
            return OParser.RULE_sorted_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterSorted_expression"):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSorted_expression"):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = OParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1286
            self.match(OParser.SORTED)
            self.state = 1288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DESC:
                self.state = 1287
                self.match(OParser.DESC)


            self.state = 1290
            self.match(OParser.LPAR)
            self.state = 1291
            localctx.source = self.instance_expression(0)
            self.state = 1297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 1292
                self.match(OParser.COMMA)
                self.state = 1293
                self.key_token()
                self.state = 1294
                self.match(OParser.EQ)
                self.state = 1295
                localctx.key = self.instance_expression(0)


            self.state = 1299
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Selector_expressionContext, self).copyFrom(ctx)



    class SliceSelectorContext(Selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selector_expressionContext)
            super(OParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(OParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceSelector"):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceSelector"):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selector_expressionContext)
            super(OParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberSelector"):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberSelector"):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selector_expressionContext)
            super(OParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemSelector"):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemSelector"):
                listener.exitItemSelector(self)



    def selector_expression(self):

        localctx = OParser.Selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_selector_expression)
        try:
            self.state = 1311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                localctx = OParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1301
                self.match(OParser.DOT)
                self.state = 1302
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1303
                self.match(OParser.LBRAK)
                self.state = 1304
                localctx.exp = self.expression(0)
                self.state = 1305
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1307
                self.match(OParser.LBRAK)
                self.state = 1308
                localctx.xslice = self.slice_arguments()
                self.state = 1309
                self.match(OParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(OParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Constructor_expressionContext)
            super(OParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.copyExp = None # Copy_fromContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)

        def copy_from(self):
            return self.getTypedRuleContext(OParser.Copy_fromContext,0)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorFrom"):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorFrom"):
                listener.exitConstructorFrom(self)


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Constructor_expressionContext)
            super(OParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorNoFrom"):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorNoFrom"):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = OParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                localctx = OParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1313
                localctx.typ = self.mutable_category_type()
                self.state = 1314
                self.match(OParser.LPAR)
                self.state = 1315
                localctx.copyExp = self.copy_from()
                self.state = 1318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.COMMA:
                    self.state = 1316
                    self.match(OParser.COMMA)
                    self.state = 1317
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1320
                self.match(OParser.RPAR)
                pass

            elif la_ == 2:
                localctx = OParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1322
                localctx.typ = self.mutable_category_type()
                self.state = 1323
                self.match(OParser.LPAR)
                self.state = 1325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                    self.state = 1324
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1327
                self.match(OParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Copy_fromContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Copy_fromContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_copy_from

        def enterRule(self, listener):
            if hasattr(listener, "enterCopy_from"):
                listener.enterCopy_from(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCopy_from"):
                listener.exitCopy_from(self)




    def copy_from(self):

        localctx = OParser.Copy_fromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_copy_from)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1331
            self.match(OParser.FROM)
            self.state = 1332
            self.assign()
            self.state = 1333
            localctx.exp = self.expression(0)
            self.state = 1334
            if not self.willNotBe(self.equalToken()):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(OParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExpressionAssignmentList"):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpressionAssignmentList"):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(OParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentList"):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentList"):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(OParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentListItem"):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListItem"):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                localctx = OParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1337
                localctx.exp = self.expression(0)
                self.state = 1338
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = OParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1340
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ArgumentAssignmentListItemContext(self, OParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1343
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1344
                    self.match(OParser.COMMA)
                    self.state = 1345
                    localctx.item = self.argument_assignment() 
                self.state = 1350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_argument_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_assignment"):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_assignment"):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = OParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1351
            localctx.name = self.variable_identifier()
            self.state = 1355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 1352
                self.assign()
                self.state = 1353
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def assignable_instance(self):
            return self.getTypedRuleContext(OParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_instance_statement"):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_instance_statement"):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = OParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1357
            localctx.inst = self.assignable_instance(0)
            self.state = 1358
            self.assign()
            self.state = 1359
            localctx.exp = self.expression(0)
            self.state = 1360
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Child_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(OParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Child_instanceContext)
            super(OParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberInstance"):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberInstance"):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Child_instanceContext)
            super(OParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemInstance"):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemInstance"):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = OParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_child_instance)
        try:
            self.state = 1368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1362
                self.match(OParser.DOT)
                self.state = 1363
                localctx.name = self.variable_identifier()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1364
                self.match(OParser.LBRAK)
                self.state = 1365
                localctx.exp = self.expression(0)
                self.state = 1366
                self.match(OParser.RBRAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_tuple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(OParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_tuple_statement"):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_tuple_statement"):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = OParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1370
            localctx.items = self.variable_identifier_list()
            self.state = 1371
            self.assign()
            self.state = 1372
            localctx.exp = self.expression(0)
            self.state = 1373
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_null_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterNull_literal"):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNull_literal"):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = OParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1375
            self.match(OParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(OParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Declaration_listContext)
            super(OParser.FullDeclarationListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(OParser.LfsContext,0)

        def EOF(self):
            return self.getToken(OParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(OParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFullDeclarationList"):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFullDeclarationList"):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = OParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = OParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.NATIVE - 64)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.SINGLETON - 139)) | (1 << (OParser.STORABLE - 139)) | (1 << (OParser.TEST - 139)) | (1 << (OParser.WIDGET - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)))) != 0):
                self.state = 1377
                self.declarations()


            self.state = 1380
            self.lfs()
            self.state = 1381
            self.match(OParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(OParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_declarations

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclarations"):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclarations"):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = OParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1383
            self.declaration()
            self.state = 1389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.NATIVE - 64)))) != 0) or ((((_la - 139)) & ~0x3f) == 0 and ((1 << (_la - 139)) & ((1 << (OParser.SINGLETON - 139)) | (1 << (OParser.STORABLE - 139)) | (1 << (OParser.TEST - 139)) | (1 << (OParser.WIDGET - 139)) | (1 << (OParser.TYPE_IDENTIFIER - 139)))) != 0):
                self.state = 1384
                self.lfp()
                self.state = 1385
                self.declaration()
                self.state = 1391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(OParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(OParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(OParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_declarationContext,0)


        def widget_declaration(self):
            return self.getTypedRuleContext(OParser.Widget_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(OParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = OParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMENT:
                self.state = 1392
                self.comment_statement()
                self.state = 1393
                self.lfp()
                self.state = 1399
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.state = 1400
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1401
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1402
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1403
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1404
                self.widget_declaration()
                pass

            elif la_ == 6:
                self.state = 1405
                self.method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(OParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterResource_declaration"):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResource_declaration"):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = OParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1408
            self.native_resource_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_declaration"):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_declaration"):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = OParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_enum_declaration)
        try:
            self.state = 1412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1410
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1411
                self.enum_native_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(OParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol_list"):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol_list"):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = OParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_native_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1414
            self.native_symbol()
            self.state = 1420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1415
                self.lfp()
                self.state = 1416
                self.native_symbol()
                self.state = 1422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(OParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol_list"):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol_list"):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = OParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_category_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1423
            self.category_symbol()
            self.state = 1429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1424
                self.lfp()
                self.state = 1425
                self.category_symbol()
                self.state = 1431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_list"):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_list"):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = OParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1432
            self.symbol_identifier()
            self.state = 1437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1433
                self.match(OParser.COMMA)
                self.state = 1434
                self.symbol_identifier()
                self.state = 1439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(OParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(OParser.Set_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingSet"):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingSet"):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(OParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingPattern"):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingPattern"):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(OParser.List_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingList"):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingList"):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(OParser.Range_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingRange"):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingRange"):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(OParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingExpression"):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingExpression"):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = OParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_attribute_constraint)
        try:
            self.state = 1450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                localctx = OParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1440
                self.match(OParser.IN)
                self.state = 1441
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = OParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1442
                self.match(OParser.IN)
                self.state = 1443
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = OParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1444
                self.match(OParser.IN)
                self.state = 1445
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = OParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1446
                self.match(OParser.MATCHING)
                self.state = 1447
                localctx.text = self.match(OParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = OParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1448
                self.match(OParser.MATCHING)
                self.state = 1449
                localctx.exp = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(OParser.Expression_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterList_literal"):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList_literal"):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = OParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1452
                self.match(OParser.MUTABLE)


            self.state = 1455
            self.match(OParser.LBRAK)
            self.state = 1457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1456
                self.expression_list()


            self.state = 1459
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(OParser.Expression_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_set_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterSet_literal"):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSet_literal"):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = OParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1461
                self.match(OParser.MUTABLE)


            self.state = 1464
            self.match(OParser.LT)
            self.state = 1466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1465
                self.expression_list()


            self.state = 1468
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_expression_list

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_list"):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_list"):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = OParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1470
            self.expression(0)
            self.state = 1475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1471
                self.match(OParser.COMMA)
                self.state = 1472
                self.expression(0)
                self.state = 1477
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(OParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OParser.RULE_range_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterRange_literal"):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_literal"):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = OParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1478
            self.match(OParser.LBRAK)
            self.state = 1479
            localctx.low = self.expression(0)
            self.state = 1480
            self.match(OParser.RANGE)
            self.state = 1481
            localctx.high = self.expression(0)
            self.state = 1482
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(OParser.TypedefContext, self).copyFrom(ctx)


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(OParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(OParser.LT, 0)
        def GT(self):
            return self.getToken(OParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorType"):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorType"):
                listener.exitIteratorType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(OParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSetType"):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetType"):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterListType"):
                listener.enterListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitListType"):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDictType"):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDictType"):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(OParser.CURSOR, 0)
        def LT(self):
            return self.getToken(OParser.LT, 0)
        def GT(self):
            return self.getToken(OParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCursorType"):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCursorType"):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(OParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPrimaryType"):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrimaryType"):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 160
        self.enterRecursionRule(localctx, 160, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.HTML, OParser.TYPE_IDENTIFIER]:
                localctx = OParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1485
                localctx.p = self.primary_type()
                pass
            elif token in [OParser.CURSOR]:
                localctx = OParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1486
                self.match(OParser.CURSOR)
                self.state = 1487
                self.match(OParser.LT)
                self.state = 1488
                localctx.c = self.typedef(0)
                self.state = 1489
                self.match(OParser.GT)
                pass
            elif token in [OParser.ITERATOR]:
                localctx = OParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1491
                self.match(OParser.ITERATOR)
                self.state = 1492
                self.match(OParser.LT)
                self.state = 1493
                localctx.i = self.typedef(0)
                self.state = 1494
                self.match(OParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1506
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
                    if la_ == 1:
                        localctx = OParser.SetTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1498
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1499
                        self.match(OParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = OParser.ListTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1500
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1501
                        self.match(OParser.LBRAK)
                        self.state = 1502
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = OParser.DictTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1503
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1504
                        self.match(OParser.LCURL)
                        self.state = 1505
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,107,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(OParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Primary_typeContext)
            super(OParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(OParser.Native_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeType"):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeType"):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Primary_typeContext)
            super(OParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCategoryType"):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategoryType"):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = OParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_primary_type)
        try:
            self.state = 1513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.HTML]:
                localctx = OParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1511
                localctx.n = self.native_type()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1512
                localctx.c = self.category_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(OParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodType"):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodType"):
                listener.exitPeriodType(self)


    class HtmlTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.HtmlTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def HTML(self):
            return self.getToken(OParser.HTML, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHtmlType"):
                listener.enterHtmlType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHtmlType"):
                listener.exitHtmlType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanType"):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanType"):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDocumentType"):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocumentType"):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterType"):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterType"):
                listener.exitCharacterType(self)


    class VersionTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.VersionTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionType"):
                listener.enterVersionType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionType"):
                listener.exitVersionType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextType"):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextType"):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(OParser.IMAGE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterImageType"):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImageType"):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeType"):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeType"):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerType"):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerType"):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeType"):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeType"):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBlobType"):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlobType"):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDType"):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDType"):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalType"):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalType"):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCodeType"):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeType"):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateType"):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateType"):
                listener.exitDateType(self)



    def native_type(self):

        localctx = OParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_native_type)
        try:
            self.state = 1531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN]:
                localctx = OParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1515
                self.match(OParser.BOOLEAN)
                pass
            elif token in [OParser.CHARACTER]:
                localctx = OParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1516
                self.match(OParser.CHARACTER)
                pass
            elif token in [OParser.TEXT]:
                localctx = OParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1517
                self.match(OParser.TEXT)
                pass
            elif token in [OParser.IMAGE]:
                localctx = OParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1518
                self.match(OParser.IMAGE)
                pass
            elif token in [OParser.INTEGER]:
                localctx = OParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1519
                self.match(OParser.INTEGER)
                pass
            elif token in [OParser.DECIMAL]:
                localctx = OParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1520
                self.match(OParser.DECIMAL)
                pass
            elif token in [OParser.DOCUMENT]:
                localctx = OParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1521
                self.match(OParser.DOCUMENT)
                pass
            elif token in [OParser.DATE]:
                localctx = OParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1522
                self.match(OParser.DATE)
                pass
            elif token in [OParser.DATETIME]:
                localctx = OParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1523
                self.match(OParser.DATETIME)
                pass
            elif token in [OParser.TIME]:
                localctx = OParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1524
                self.match(OParser.TIME)
                pass
            elif token in [OParser.PERIOD]:
                localctx = OParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1525
                self.match(OParser.PERIOD)
                pass
            elif token in [OParser.VERSION]:
                localctx = OParser.VersionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1526
                self.match(OParser.VERSION)
                pass
            elif token in [OParser.CODE]:
                localctx = OParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1527
                self.match(OParser.CODE)
                pass
            elif token in [OParser.BLOB]:
                localctx = OParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1528
                self.match(OParser.BLOB)
                pass
            elif token in [OParser.UUID]:
                localctx = OParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1529
                self.match(OParser.UUID)
                pass
            elif token in [OParser.HTML]:
                localctx = OParser.HtmlTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 1530
                self.match(OParser.HTML)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_type"):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_type"):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = OParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1533
            localctx.t1 = self.match(OParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def getRuleIndex(self):
            return OParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterMutable_category_type"):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMutable_category_type"):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = OParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1535
                self.match(OParser.MUTABLE)


            self.state = 1538
            self.category_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def getRuleIndex(self):
            return OParser.RULE_code_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_type"):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_type"):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = OParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1540
            localctx.t1 = self.match(OParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(OParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConcreteCategoryDeclaration"):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteCategoryDeclaration"):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(OParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryDeclaration"):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryDeclaration"):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(OParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingletonCategoryDeclaration"):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingletonCategoryDeclaration"):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = OParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_category_declaration)
        try:
            self.state = 1545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                localctx = OParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1542
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1543
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1544
                localctx.decl = self.singleton_category_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Widget_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Widget_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_widget_declaration

     
        def copyFrom(self, ctx):
            super(OParser.Widget_declarationContext, self).copyFrom(ctx)



    class ConcreteWidgetDeclarationContext(Widget_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Widget_declarationContext)
            super(OParser.ConcreteWidgetDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_widget_declarationContext
            self.copyFrom(ctx)

        def concrete_widget_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_widget_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConcreteWidgetDeclaration"):
                listener.enterConcreteWidgetDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteWidgetDeclaration"):
                listener.exitConcreteWidgetDeclaration(self)



    def widget_declaration(self):

        localctx = OParser.Widget_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_widget_declaration)
        try:
            localctx = OParser.ConcreteWidgetDeclarationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1547
            localctx.decl = self.concrete_widget_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier_list"):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier_list"):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = OParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1549
            self.type_identifier()
            self.state = 1554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1550
                self.match(OParser.COMMA)
                self.state = 1551
                self.type_identifier()
                self.state = 1556
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_identifier"):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_identifier"):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = OParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_method_identifier)
        try:
            self.state = 1559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1557
                self.variable_identifier()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1558
                self.type_identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(OParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTypeIdentifier"):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTypeIdentifier"):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSymbolIdentifier"):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbolIdentifier"):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterVariableIdentifier"):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableIdentifier"):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = OParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_identifier)
        try:
            self.state = 1564
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1561
                self.variable_identifier()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1562
                self.type_identifier()
                pass
            elif token in [OParser.SYMBOL_IDENTIFIER]:
                localctx = OParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1563
                self.symbol_identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_variable_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier"):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier"):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = OParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1566
            self.match(OParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def getRuleIndex(self):
            return OParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier"):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier"):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = OParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1568
            _la = self._input.LA(1)
            if not(_la==OParser.STORABLE or _la==OParser.VARIABLE_IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_type_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier"):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier"):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = OParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1570
            self.match(OParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_identifier"):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_identifier"):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = OParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1572
            self.match(OParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(OParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_argument_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_list"):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_list"):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = OParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1574
            self.argument()
            self.state = 1579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1575
                self.match(OParser.COMMA)
                self.state = 1576
                self.argument()
                self.state = 1581
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(OParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a OParser.ArgumentContext)
            super(OParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(OParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorArgument"):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorArgument"):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a OParser.ArgumentContext)
            super(OParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(OParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeArgument"):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeArgument"):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = OParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
            if la_ == 1:
                localctx = OParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1582
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = OParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.MUTABLE:
                    self.state = 1583
                    self.match(OParser.MUTABLE)


                self.state = 1586
                localctx.arg = self.operator_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def named_argument(self):
            return self.getTypedRuleContext(OParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(OParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return OParser.RULE_operator_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_argument"):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_argument"):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = OParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_operator_argument)
        try:
            self.state = 1591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1589
                self.named_argument()
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.HTML, OParser.ANY, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1590
                self.typed_argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Named_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_named_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterNamed_argument"):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNamed_argument"):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = OParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1593
            self.variable_identifier()
            self.state = 1596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 1594
                self.match(OParser.EQ)
                self.state = 1595
                self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(OParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_code_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_argument"):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_argument"):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = OParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1598
            self.code_type()
            self.state = 1599
            localctx.name = self.variable_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_or_any_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)


        def getRuleIndex(self):
            return OParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_or_any_type"):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_or_any_type"):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = OParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_category_or_any_type)
        try:
            self.state = 1603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.HTML, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1601
                self.typedef(0)
                pass
            elif token in [OParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1602
                self.any_type(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Any_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(OParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyListType"):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyListType"):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyType"):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyType"):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyDictType"):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyDictType"):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 202
        self.enterRecursionRule(localctx, 202, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1606
            self.match(OParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1616
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1614
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
                    if la_ == 1:
                        localctx = OParser.AnyListTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1608
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1609
                        self.match(OParser.LBRAK)
                        self.state = 1610
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = OParser.AnyDictTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1611
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1612
                        self.match(OParser.LCURL)
                        self.state = 1613
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1618
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(OParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration_list"):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration_list"):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = OParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1619
            self.member_method_declaration()
            self.state = 1625
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ABSTRACT - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.METHOD - 113)) | (1 << (OParser.OPERATOR - 113)) | (1 << (OParser.SETTER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)))) != 0):
                self.state = 1620
                self.lfp()
                self.state = 1621
                self.member_method_declaration()
                self.state = 1627
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(OParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(OParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(OParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(OParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration"):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration"):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = OParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_member_method_declaration)
        try:
            self.state = 1633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1628
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1629
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1630
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1631
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1632
                self.operator_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(OParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration_list"):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration_list"):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = OParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1635
            self.native_member_method_declaration()
            self.state = 1641
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.HTML - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 113)) & ~0x3f) == 0 and ((1 << (_la - 113)) & ((1 << (OParser.METHOD - 113)) | (1 << (OParser.NATIVE - 113)) | (1 << (OParser.SETTER - 113)) | (1 << (OParser.TYPE_IDENTIFIER - 113)))) != 0):
                self.state = 1636
                self.lfp()
                self.state = 1637
                self.native_member_method_declaration()
                self.state = 1643
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(OParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(OParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration"):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration"):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = OParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_native_member_method_declaration)
        try:
            self.state = 1647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1644
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1645
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1646
                self.native_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(OParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(OParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(OParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2CategoryBinding"):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2CategoryBinding"):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(OParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(OParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3CategoryBinding"):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3CategoryBinding"):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(OParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCategoryBinding"):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCategoryBinding"):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(OParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCategoryBinding"):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCategoryBinding"):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(OParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(OParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptCategoryBinding"):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptCategoryBinding"):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = OParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_native_category_binding)
        try:
            self.state = 1659
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1649
                self.match(OParser.JAVA)
                self.state = 1650
                localctx.binding = self.java_class_identifier_expression(0)
                pass
            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1651
                self.match(OParser.CSHARP)
                self.state = 1652
                localctx.binding = self.csharp_identifier_expression(0)
                pass
            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1653
                self.match(OParser.PYTHON2)
                self.state = 1654
                localctx.binding = self.python_category_binding()
                pass
            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1655
                self.match(OParser.PYTHON3)
                self.state = 1656
                localctx.binding = self.python_category_binding()
                pass
            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1657
                self.match(OParser.JAVASCRIPT)
                self.state = 1658
                localctx.binding = self.javascript_category_binding()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(OParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_category_binding"):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_category_binding"):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = OParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_python_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1661
            self.identifier()
            self.state = 1663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1662
                self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(OParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(OParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(OParser.DOT)
            else:
                return self.getToken(OParser.DOT, i)

        def getRuleIndex(self):
            return OParser.RULE_python_module

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_module"):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_module"):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = OParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_python_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1665
            self.match(OParser.FROM)
            self.state = 1666
            self.module_token()
            self.state = 1667
            self.match(OParser.COLON)
            self.state = 1668
            self.identifier()
            self.state = 1673
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1669
                self.match(OParser.DOT)
                self.state = 1670
                self.identifier()
                self.state = 1675
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(OParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_category_binding"):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_category_binding"):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = OParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_javascript_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1676
            self.identifier()
            self.state = 1678
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1677
                self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(OParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(OParser.SLASH)
            else:
                return self.getToken(OParser.SLASH, i)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)

        def getRuleIndex(self):
            return OParser.RULE_javascript_module

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_module"):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_module"):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = OParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1680
            self.match(OParser.FROM)
            self.state = 1681
            self.module_token()
            self.state = 1682
            self.match(OParser.COLON)
            self.state = 1684
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SLASH:
                self.state = 1683
                self.match(OParser.SLASH)


            self.state = 1686
            self.javascript_identifier()
            self.state = 1691
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SLASH:
                self.state = 1687
                self.match(OParser.SLASH)
                self.state = 1688
                self.javascript_identifier()
                self.state = 1693
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DOT:
                self.state = 1694
                self.match(OParser.DOT)
                self.state = 1695
                self.javascript_identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier_list"):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier_list"):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = OParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1698
            self.variable_identifier()
            self.state = 1703
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1699
                self.match(OParser.COMMA)
                self.state = 1700
                self.variable_identifier()
                self.state = 1705
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier_list"):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier_list"):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = OParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1706
            self.attribute_identifier()
            self.state = 1711
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1707
                self.match(OParser.COMMA)
                self.state = 1708
                self.attribute_identifier()
                self.state = 1713
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(OParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(OParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_declaration"):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_declaration"):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = OParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_method_declaration)
        try:
            self.state = 1718
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1714
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1715
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1716
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1717
                self.test_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comment_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(OParser.COMMENT, 0)

        def getRuleIndex(self):
            return OParser.RULE_comment_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterComment_statement"):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComment_statement"):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = OParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720
            self.match(OParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_native_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_statement_list"):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_statement_list"):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = OParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_native_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1722
            self.native_statement()
            self.state = 1728
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 1723
                self.lfp()
                self.state = 1724
                self.native_statement()
                self.state = 1730
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(OParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.CSharpNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(OParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(OParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpNativeStatement"):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpNativeStatement"):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(OParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(OParser.Java_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaNativeStatement"):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaNativeStatement"):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(OParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(OParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptNativeStatement"):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptNativeStatement"):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(OParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(OParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2NativeStatement"):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2NativeStatement"):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(OParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(OParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3NativeStatement"):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3NativeStatement"):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = OParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_native_statement)
        try:
            self.state = 1741
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1731
                self.match(OParser.JAVA)
                self.state = 1732
                self.java_statement()
                pass
            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1733
                self.match(OParser.CSHARP)
                self.state = 1734
                self.csharp_statement()
                pass
            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1735
                self.match(OParser.PYTHON2)
                self.state = 1736
                self.python_native_statement()
                pass
            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1737
                self.match(OParser.PYTHON3)
                self.state = 1738
                self.python_native_statement()
                pass
            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1739
                self.match(OParser.JAVASCRIPT)
                self.state = 1740
                self.javascript_native_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(OParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(OParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_native_statement"):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_native_statement"):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = OParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1743
            self.python_statement()
            self.state = 1745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1744
                self.match(OParser.SEMI)


            self.state = 1748
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1747
                self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(OParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(OParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_native_statement"):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_native_statement"):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = OParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1750
            self.javascript_statement()
            self.state = 1752
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1751
                self.match(OParser.SEMI)


            self.state = 1755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1754
                self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.StatementContext)
            else:
                return self.getTypedRuleContext(OParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterStatement_list"):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStatement_list"):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = OParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1757
            self.statement()
            self.state = 1763
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.METHOD - 64)))) != 0) or ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (OParser.RETURN - 134)) | (1 << (OParser.STORE - 134)) | (1 << (OParser.SWITCH - 134)) | (1 << (OParser.THROW - 134)) | (1 << (OParser.TRY - 134)) | (1 << (OParser.WITH - 134)) | (1 << (OParser.WHILE - 134)) | (1 << (OParser.WRITE - 134)) | (1 << (OParser.SYMBOL_IDENTIFIER - 134)) | (1 << (OParser.TYPE_IDENTIFIER - 134)) | (1 << (OParser.VARIABLE_IDENTIFIER - 134)))) != 0):
                self.state = 1758
                self.lfp()
                self.state = 1759
                self.statement()
                self.state = 1765
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.AssertionContext)
            else:
                return self.getTypedRuleContext(OParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_assertion_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion_list"):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion_list"):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = OParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_assertion_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1766
            self.assertion()
            self.state = 1772
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1767
                self.lfp()
                self.state = 1768
                self.assertion()
                self.state = 1774
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_case_statement_list"):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_case_statement_list"):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = OParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_switch_case_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1775
            self.switch_case_statement()
            self.state = 1781
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.CASE:
                self.state = 1776
                self.lfp()
                self.state = 1777
                self.switch_case_statement()
                self.state = 1783
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCatch_statement_list"):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatch_statement_list"):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = OParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1784
            self.catch_statement()
            self.state = 1790
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1785
                    self.lfp()
                    self.state = 1786
                    self.catch_statement() 
                self.state = 1792
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(OParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_collectionContext)
            super(OParser.LiteralListLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralListLiteral"):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralListLiteral"):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_collectionContext)
            super(OParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(OParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(OParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralRangeLiteral"):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralRangeLiteral"):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_collectionContext)
            super(OParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(OParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralSetLiteral"):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralSetLiteral"):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = OParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_literal_collection)
        try:
            self.state = 1807
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                localctx = OParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1793
                self.match(OParser.LBRAK)
                self.state = 1794
                localctx.low = self.atomic_literal()
                self.state = 1795
                self.match(OParser.RANGE)
                self.state = 1796
                localctx.high = self.atomic_literal()
                self.state = 1797
                self.match(OParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = OParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1799
                self.match(OParser.LBRAK)
                self.state = 1800
                self.literal_list_literal()
                self.state = 1801
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1803
                self.match(OParser.LT)
                self.state = 1804
                self.literal_list_literal()
                self.state = 1805
                self.match(OParser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atomic_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(OParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(OParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMinIntegerLiteral"):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinIntegerLiteral"):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(OParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateLiteral"):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateLiteral"):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanLiteral"):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanLiteral"):
                listener.exitBooleanLiteral(self)


    class VersionLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.VersionLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def VERSION_LITERAL(self):
            return self.getToken(OParser.VERSION_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionLiteral"):
                listener.enterVersionLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionLiteral"):
                listener.exitVersionLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(OParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHexadecimalLiteral"):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHexadecimalLiteral"):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(OParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDLiteral"):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDLiteral"):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(OParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMaxIntegerLiteral"):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMaxIntegerLiteral"):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(OParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeLiteral"):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeLiteral"):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(OParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodLiteral"):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodLiteral"):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalLiteral"):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalLiteral"):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextLiteral"):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextLiteral"):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(OParser.Null_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNullLiteral"):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNullLiteral"):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerLiteral"):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerLiteral"):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(OParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeLiteral"):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeLiteral"):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterLiteral"):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterLiteral"):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = OParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_atomic_literal)
        try:
            self.state = 1824
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.MIN_INTEGER]:
                localctx = OParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1809
                localctx.t = self.match(OParser.MIN_INTEGER)
                pass
            elif token in [OParser.MAX_INTEGER]:
                localctx = OParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1810
                localctx.t = self.match(OParser.MAX_INTEGER)
                pass
            elif token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1811
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.HEXA_LITERAL]:
                localctx = OParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1812
                localctx.t = self.match(OParser.HEXA_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1813
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            elif token in [OParser.DATE_LITERAL]:
                localctx = OParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1814
                localctx.t = self.match(OParser.DATE_LITERAL)
                pass
            elif token in [OParser.TIME_LITERAL]:
                localctx = OParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1815
                localctx.t = self.match(OParser.TIME_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1816
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1817
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.DATETIME_LITERAL]:
                localctx = OParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1818
                localctx.t = self.match(OParser.DATETIME_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1819
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.PERIOD_LITERAL]:
                localctx = OParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1820
                localctx.t = self.match(OParser.PERIOD_LITERAL)
                pass
            elif token in [OParser.VERSION_LITERAL]:
                localctx = OParser.VersionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1821
                localctx.t = self.match(OParser.VERSION_LITERAL)
                pass
            elif token in [OParser.UUID_LITERAL]:
                localctx = OParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1822
                localctx.t = self.match(OParser.UUID_LITERAL)
                pass
            elif token in [OParser.NULL]:
                localctx = OParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1823
                localctx.n = self.null_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_list_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(OParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_list_literal"):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_list_literal"):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = OParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1826
            self.atomic_literal()
            self.state = 1831
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1827
                self.match(OParser.COMMA)
                self.state = 1828
                self.atomic_literal()
                self.state = 1833
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(OParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterThisExpression"):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThisExpression"):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesisExpression"):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesisExpression"):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralExpression"):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralExpression"):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifierExpression"):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifierExpression"):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = OParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_selectable_expression)
        try:
            self.state = 1838
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,150,self._ctx)
            if la_ == 1:
                localctx = OParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1834
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1835
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = OParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1836
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = OParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1837
                localctx.exp = self.this_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class This_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def getRuleIndex(self):
            return OParser.RULE_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterThis_expression"):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThis_expression"):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = OParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1840
            _la = self._input.LA(1)
            if not(_la==OParser.SELF or _la==OParser.THIS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def getRuleIndex(self):
            return OParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesis_expression"):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesis_expression"):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = OParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1842
            self.match(OParser.LPAR)
            self.state = 1843
            self.expression(0)
            self.state = 1844
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(OParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return OParser.RULE_literal_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_expression"):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_expression"):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = OParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_literal_expression)
        try:
            self.state = 1848
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.NULL, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.TEXT_LITERAL, OParser.UUID_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL, OParser.VERSION_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1846
                self.atomic_literal()
                pass
            elif token in [OParser.LPAR, OParser.LBRAK, OParser.LCURL, OParser.LT, OParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1847
                self.collection_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Collection_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(OParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(OParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(OParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(OParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(OParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return OParser.RULE_collection_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterCollection_literal"):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollection_literal"):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = OParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_collection_literal)
        try:
            self.state = 1855
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,152,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1850
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1851
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1852
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1853
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1854
                self.tuple_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(OParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_tuple_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterTuple_literal"):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTuple_literal"):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = OParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1858
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1857
                self.match(OParser.MUTABLE)


            self.state = 1860
            self.match(OParser.LPAR)
            self.state = 1862
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1861
                self.expression_tuple()


            self.state = 1864
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(OParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_dict_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_literal"):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_literal"):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = OParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1867
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1866
                self.match(OParser.MUTABLE)


            self.state = 1869
            self.match(OParser.LCURL)
            self.state = 1871
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1870
                self.dict_entry_list()


            self.state = 1873
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_expression_tuple

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_tuple"):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_tuple"):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = OParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1875
            self.expression(0)
            self.state = 1876
            self.match(OParser.COMMA)
            self.state = 1885
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                self.state = 1877
                self.expression(0)
                self.state = 1882
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OParser.COMMA:
                    self.state = 1878
                    self.match(OParser.COMMA)
                    self.state = 1879
                    self.expression(0)
                    self.state = 1884
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(OParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry_list"):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry_list"):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = OParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1887
            self.dict_entry()
            self.state = 1892
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1888
                self.match(OParser.COMMA)
                self.state = 1889
                self.dict_entry()
                self.state = 1894
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_entryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OParser.RULE_dict_entry

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry"):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry"):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = OParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1895
            localctx.key = self.expression(0)
            self.state = 1896
            self.match(OParser.COLON)
            self.state = 1897
            localctx.value = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Slice_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Slice_argumentsContext)
            super(OParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstAndLast"):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstAndLast"):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Slice_argumentsContext)
            super(OParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceLastOnly"):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceLastOnly"):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Slice_argumentsContext)
            super(OParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstOnly"):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstOnly"):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = OParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_slice_arguments)
        try:
            self.state = 1908
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,160,self._ctx)
            if la_ == 1:
                localctx = OParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1899
                localctx.first = self.expression(0)
                self.state = 1900
                self.match(OParser.COLON)
                self.state = 1901
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1903
                localctx.first = self.expression(0)
                self.state = 1904
                self.match(OParser.COLON)
                pass

            elif la_ == 3:
                localctx = OParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1906
                self.match(OParser.COLON)
                self.state = 1907
                localctx.last = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_variable_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_variable_statement"):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_variable_statement"):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = OParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1910
            self.variable_identifier()
            self.state = 1911
            self.assign()
            self.state = 1912
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignable_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(OParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Assignable_instanceContext)
            super(OParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(OParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(OParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterChildInstance"):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitChildInstance"):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Assignable_instanceContext)
            super(OParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRootInstance"):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRootInstance"):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 276
        self.enterRecursionRule(localctx, 276, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1915
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1921
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ChildInstanceContext(self, OParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1917
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1918
                    self.child_instance() 
                self.state = 1923
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(OParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Is_expressionContext)
            super(OParser.IsATypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsATypeExpression"):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsATypeExpression"):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Is_expressionContext)
            super(OParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsOtherExpression"):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsOtherExpression"):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = OParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_is_expression)
        try:
            self.state = 1928
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,162,self._ctx)
            if la_ == 1:
                localctx = OParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1924
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1925
                self.match(OParser.VARIABLE_IDENTIFIER)
                self.state = 1926
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = OParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1927
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_all_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Read_all_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def ALL(self):
            return self.getToken(OParser.ALL, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_read_all_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_all_expression"):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_all_expression"):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = OParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1930
            self.match(OParser.READ)
            self.state = 1931
            self.match(OParser.ALL)
            self.state = 1932
            self.match(OParser.FROM)
            self.state = 1933
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_one_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Read_one_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def ONE(self):
            return self.getToken(OParser.ONE, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_read_one_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_one_expression"):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_one_expression"):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = OParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1935
            self.match(OParser.READ)
            self.state = 1936
            self.match(OParser.ONE)
            self.state = 1937
            self.match(OParser.FROM)
            self.state = 1938
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_by_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Order_byContext)
            else:
                return self.getTypedRuleContext(OParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_order_by_list

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by_list"):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by_list"):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = OParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_order_by_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1940
            self.order_by()
            self.state = 1945
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1941
                self.match(OParser.COMMA)
                self.state = 1942
                self.order_by()
                self.state = 1947
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(OParser.DOT)
            else:
                return self.getToken(OParser.DOT, i)

        def ASC(self):
            return self.getToken(OParser.ASC, 0)

        def DESC(self):
            return self.getToken(OParser.DESC, 0)

        def getRuleIndex(self):
            return OParser.RULE_order_by

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by"):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by"):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = OParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1948
            self.variable_identifier()
            self.state = 1953
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1949
                self.match(OParser.DOT)
                self.state = 1950
                self.variable_identifier()
                self.state = 1955
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1957
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.ASC or _la==OParser.DESC:
                self.state = 1956
                _la = self._input.LA(1)
                if not(_la==OParser.ASC or _la==OParser.DESC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(OParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(OParser.PLUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorPlus"):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorPlus"):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(OParser.DivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorDivide"):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorDivide"):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(OParser.IdivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorIDivide"):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorIDivide"):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(OParser.MultiplyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMultiply"):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMultiply"):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMinus"):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMinus"):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(OParser.ModuloContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorModulo"):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorModulo"):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = OParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_operator)
        try:
            self.state = 1965
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.PLUS]:
                localctx = OParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1959
                self.match(OParser.PLUS)
                pass
            elif token in [OParser.MINUS]:
                localctx = OParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1960
                self.match(OParser.MINUS)
                pass
            elif token in [OParser.STAR]:
                localctx = OParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1961
                self.multiply()
                pass
            elif token in [OParser.SLASH]:
                localctx = OParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1962
                self.divide()
                pass
            elif token in [OParser.BSLASH]:
                localctx = OParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1963
                self.idivide()
                pass
            elif token in [OParser.PERCENT, OParser.MODULO]:
                localctx = OParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1964
                self.modulo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def JAVA(self):
            return self.getToken(OParser.JAVA, 0)

        def CSHARP(self):
            return self.getToken(OParser.CSHARP, 0)

        def PYTHON2(self):
            return self.getToken(OParser.PYTHON2, 0)

        def PYTHON3(self):
            return self.getToken(OParser.PYTHON3, 0)

        def JAVASCRIPT(self):
            return self.getToken(OParser.JAVASCRIPT, 0)

        def SWIFT(self):
            return self.getToken(OParser.SWIFT, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def METHOD_T(self):
            return self.getToken(OParser.METHOD_T, 0)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def IMAGE(self):
            return self.getToken(OParser.IMAGE, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def ITERATOR(self):
            return self.getToken(OParser.ITERATOR, 0)

        def CURSOR(self):
            return self.getToken(OParser.CURSOR, 0)

        def HTML(self):
            return self.getToken(OParser.HTML, 0)

        def ABSTRACT(self):
            return self.getToken(OParser.ABSTRACT, 0)

        def ALL(self):
            return self.getToken(OParser.ALL, 0)

        def ALWAYS(self):
            return self.getToken(OParser.ALWAYS, 0)

        def AND(self):
            return self.getToken(OParser.AND, 0)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def AS(self):
            return self.getToken(OParser.AS, 0)

        def ASC(self):
            return self.getToken(OParser.ASC, 0)

        def ATTR(self):
            return self.getToken(OParser.ATTR, 0)

        def ATTRIBUTE(self):
            return self.getToken(OParser.ATTRIBUTE, 0)

        def ATTRIBUTES(self):
            return self.getToken(OParser.ATTRIBUTES, 0)

        def BINDINGS(self):
            return self.getToken(OParser.BINDINGS, 0)

        def BREAK(self):
            return self.getToken(OParser.BREAK, 0)

        def BY(self):
            return self.getToken(OParser.BY, 0)

        def CASE(self):
            return self.getToken(OParser.CASE, 0)

        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def CLASS(self):
            return self.getToken(OParser.CLASS, 0)

        def CLOSE(self):
            return self.getToken(OParser.CLOSE, 0)

        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)

        def DEF(self):
            return self.getToken(OParser.DEF, 0)

        def DEFAULT(self):
            return self.getToken(OParser.DEFAULT, 0)

        def DEFINE(self):
            return self.getToken(OParser.DEFINE, 0)

        def DELETE(self):
            return self.getToken(OParser.DELETE, 0)

        def DESC(self):
            return self.getToken(OParser.DESC, 0)

        def DO(self):
            return self.getToken(OParser.DO, 0)

        def DOING(self):
            return self.getToken(OParser.DOING, 0)

        def EACH(self):
            return self.getToken(OParser.EACH, 0)

        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)

        def ENUM(self):
            return self.getToken(OParser.ENUM, 0)

        def ENUMERATED(self):
            return self.getToken(OParser.ENUMERATED, 0)

        def EXCEPT(self):
            return self.getToken(OParser.EXCEPT, 0)

        def EXECUTE(self):
            return self.getToken(OParser.EXECUTE, 0)

        def EXPECTING(self):
            return self.getToken(OParser.EXPECTING, 0)

        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)

        def FILTERED(self):
            return self.getToken(OParser.FILTERED, 0)

        def FINALLY(self):
            return self.getToken(OParser.FINALLY, 0)

        def FLUSH(self):
            return self.getToken(OParser.FLUSH, 0)

        def FOR(self):
            return self.getToken(OParser.FOR, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def GETTER(self):
            return self.getToken(OParser.GETTER, 0)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)

        def IF(self):
            return self.getToken(OParser.IF, 0)

        def IN(self):
            return self.getToken(OParser.IN, 0)

        def INDEX(self):
            return self.getToken(OParser.INDEX, 0)

        def INVOKE(self):
            return self.getToken(OParser.INVOKE, 0)

        def IS(self):
            return self.getToken(OParser.IS, 0)

        def MATCHING(self):
            return self.getToken(OParser.MATCHING, 0)

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def METHODS(self):
            return self.getToken(OParser.METHODS, 0)

        def MODULO(self):
            return self.getToken(OParser.MODULO, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)

        def NOTHING(self):
            return self.getToken(OParser.NOTHING, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def ON(self):
            return self.getToken(OParser.ON, 0)

        def ONE(self):
            return self.getToken(OParser.ONE, 0)

        def OPEN(self):
            return self.getToken(OParser.OPEN, 0)

        def OPERATOR(self):
            return self.getToken(OParser.OPERATOR, 0)

        def OR(self):
            return self.getToken(OParser.OR, 0)

        def ORDER(self):
            return self.getToken(OParser.ORDER, 0)

        def OTHERWISE(self):
            return self.getToken(OParser.OTHERWISE, 0)

        def PASS(self):
            return self.getToken(OParser.PASS, 0)

        def RAISE(self):
            return self.getToken(OParser.RAISE, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def RECEIVING(self):
            return self.getToken(OParser.RECEIVING, 0)

        def RESOURCE(self):
            return self.getToken(OParser.RESOURCE, 0)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)

        def RETURNING(self):
            return self.getToken(OParser.RETURNING, 0)

        def ROWS(self):
            return self.getToken(OParser.ROWS, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def SETTER(self):
            return self.getToken(OParser.SETTER, 0)

        def SINGLETON(self):
            return self.getToken(OParser.SINGLETON, 0)

        def SORTED(self):
            return self.getToken(OParser.SORTED, 0)

        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def STORE(self):
            return self.getToken(OParser.STORE, 0)

        def SWITCH(self):
            return self.getToken(OParser.SWITCH, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def THROW(self):
            return self.getToken(OParser.THROW, 0)

        def TO(self):
            return self.getToken(OParser.TO, 0)

        def TRY(self):
            return self.getToken(OParser.TRY, 0)

        def VERIFYING(self):
            return self.getToken(OParser.VERIFYING, 0)

        def WIDGET(self):
            return self.getToken(OParser.WIDGET, 0)

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def WHEN(self):
            return self.getToken(OParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)

        def WHILE(self):
            return self.getToken(OParser.WHILE, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def getRuleIndex(self):
            return OParser.RULE_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterKeyword"):
                listener.enterKeyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKeyword"):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = OParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1967
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT) | (1 << OParser.SWIFT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.METHOD_T) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ALL - 64)) | (1 << (OParser.ALWAYS - 64)) | (1 << (OParser.AND - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.AS - 64)) | (1 << (OParser.ASC - 64)) | (1 << (OParser.ATTR - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.ATTRIBUTES - 64)) | (1 << (OParser.BINDINGS - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.BY - 64)) | (1 << (OParser.CASE - 64)) | (1 << (OParser.CATCH - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.CLASS - 64)) | (1 << (OParser.CLOSE - 64)) | (1 << (OParser.CONTAINS - 64)) | (1 << (OParser.DEF - 64)) | (1 << (OParser.DEFAULT - 64)) | (1 << (OParser.DEFINE - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DESC - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.DOING - 64)) | (1 << (OParser.EACH - 64)) | (1 << (OParser.ELSE - 64)) | (1 << (OParser.ENUM - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.EXCEPT - 64)) | (1 << (OParser.EXECUTE - 64)) | (1 << (OParser.EXPECTING - 64)) | (1 << (OParser.EXTENDS - 64)) | (1 << (OParser.FETCH - 64)) | (1 << (OParser.FILTERED - 64)) | (1 << (OParser.FINALLY - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.FROM - 64)) | (1 << (OParser.GETTER - 64)) | (1 << (OParser.HAS - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.IN - 64)) | (1 << (OParser.INDEX - 64)) | (1 << (OParser.INVOKE - 64)) | (1 << (OParser.IS - 64)) | (1 << (OParser.MATCHING - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.METHODS - 64)) | (1 << (OParser.MODULO - 64)) | (1 << (OParser.MUTABLE - 64)) | (1 << (OParser.NATIVE - 64)) | (1 << (OParser.NONE - 64)) | (1 << (OParser.NOT - 64)) | (1 << (OParser.NOTHING - 64)) | (1 << (OParser.NULL - 64)) | (1 << (OParser.ON - 64)) | (1 << (OParser.ONE - 64)) | (1 << (OParser.OPEN - 64)) | (1 << (OParser.OPERATOR - 64)) | (1 << (OParser.OR - 64)) | (1 << (OParser.ORDER - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.OTHERWISE - 128)) | (1 << (OParser.PASS - 128)) | (1 << (OParser.RAISE - 128)) | (1 << (OParser.READ - 128)) | (1 << (OParser.RECEIVING - 128)) | (1 << (OParser.RESOURCE - 128)) | (1 << (OParser.RETURN - 128)) | (1 << (OParser.RETURNING - 128)) | (1 << (OParser.ROWS - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.SETTER - 128)) | (1 << (OParser.SINGLETON - 128)) | (1 << (OParser.SORTED - 128)) | (1 << (OParser.STORABLE - 128)) | (1 << (OParser.STORE - 128)) | (1 << (OParser.SWITCH - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.THROW - 128)) | (1 << (OParser.TO - 128)) | (1 << (OParser.TRY - 128)) | (1 << (OParser.VERIFYING - 128)) | (1 << (OParser.WIDGET - 128)) | (1 << (OParser.WITH - 128)) | (1 << (OParser.WHEN - 128)) | (1 << (OParser.WHERE - 128)) | (1 << (OParser.WHILE - 128)) | (1 << (OParser.WRITE - 128)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class New_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_new_token

        def enterRule(self, listener):
            if hasattr(listener, "enterNew_token"):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNew_token"):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = OParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1969
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1970
            if not self.isText(localctx.i1,"new"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"new\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Key_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_key_token

        def enterRule(self, listener):
            if hasattr(listener, "enterKey_token"):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey_token"):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = OParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1972
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1973
            if not self.isText(localctx.i1,"key"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"key\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_module_token

        def enterRule(self, listener):
            if hasattr(listener, "enterModule_token"):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModule_token"):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = OParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1975
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1976
            if not self.isText(localctx.i1,"module"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"module\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_value_token

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_token"):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_token"):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = OParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1978
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1979
            if not self.isText(localctx.i1,"value"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"value\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbols_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_symbols_token

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbols_token"):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbols_token"):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = OParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1981
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1982
            if not self.isText(localctx.i1,"symbols"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"symbols\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def getRuleIndex(self):
            return OParser.RULE_assign

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)




    def assign(self):

        localctx = OParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1984
            self.match(OParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(OParser.STAR, 0)

        def getRuleIndex(self):
            return OParser.RULE_multiply

        def enterRule(self, listener):
            if hasattr(listener, "enterMultiply"):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiply"):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = OParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1986
            self.match(OParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def getRuleIndex(self):
            return OParser.RULE_divide

        def enterRule(self, listener):
            if hasattr(listener, "enterDivide"):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivide"):
                listener.exitDivide(self)




    def divide(self):

        localctx = OParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1988
            self.match(OParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(OParser.BSLASH, 0)

        def getRuleIndex(self):
            return OParser.RULE_idivide

        def enterRule(self, listener):
            if hasattr(listener, "enterIdivide"):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdivide"):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = OParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1990
            self.match(OParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(OParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(OParser.MODULO, 0)

        def getRuleIndex(self):
            return OParser.RULE_modulo

        def enterRule(self, listener):
            if hasattr(listener, "enterModulo"):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModulo"):
                listener.exitModulo(self)




    def modulo(self):

        localctx = OParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1992
            _la = self._input.LA(1)
            if not(_la==OParser.PERCENT or _la==OParser.MODULO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_lfs

        def enterRule(self, listener):
            if hasattr(listener, "enterLfs"):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfs"):
                listener.exitLfs(self)




    def lfs(self):

        localctx = OParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_lfp

        def enterRule(self, listener):
            if hasattr(listener, "enterLfp"):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfp"):
                listener.exitLfp(self)




    def lfp(self):

        localctx = OParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_lfp)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_widget_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_widget_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_widget_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_widget_declaration"):
                listener.enterNative_widget_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_widget_declaration"):
                listener.exitNative_widget_declaration(self)




    def native_widget_declaration(self):

        localctx = OParser.Native_widget_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_native_widget_declaration)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_statementContext)
            super(OParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptStatement"):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptStatement"):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_statementContext)
            super(OParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptReturnStatement"):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptReturnStatement"):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = OParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_statement)
        try:
            self.state = 2007
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2000
                self.match(OParser.RETURN)
                self.state = 2001
                localctx.exp = self.javascript_expression(0)
                self.state = 2002
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.LBRAK, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.HTML, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2004
                localctx.exp = self.javascript_expression(0)
                self.state = 2005
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_expressionContext)
            super(OParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptSelectorExpression"):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptSelectorExpression"):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_expressionContext)
            super(OParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptPrimaryExpression"):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptPrimaryExpression"):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2010
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2016
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,168,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptSelectorExpressionContext(self, OParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 2012
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2013
                    localctx.child = self.javascript_selector_expression() 
                self.state = 2018
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_primary_expression"):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_primary_expression"):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = OParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_primary_expression)
        try:
            self.state = 2026
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,169,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2019
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2020
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2021
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2022
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2023
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2024
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2025
                self.javascript_item_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_this_expression"):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_this_expression"):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = OParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2028
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(OParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_new_expression"):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_new_expression"):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = OParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2030
            self.new_token()
            self.state = 2031
            self.javascript_method_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(OParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMemberExpression"):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMemberExpression"):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptItemExpression"):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptItemExpression"):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMethodExpression"):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMethodExpression"):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = OParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_selector_expression)
        try:
            self.state = 2038
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,170,self._ctx)
            if la_ == 1:
                localctx = OParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2033
                self.match(OParser.DOT)
                self.state = 2034
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = OParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2035
                self.match(OParser.DOT)
                self.state = 2036
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = OParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2037
                localctx.exp = self.javascript_item_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(OParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(OParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_method_expression"):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_method_expression"):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = OParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2040
            localctx.name = self.javascript_identifier()
            self.state = 2041
            self.match(OParser.LPAR)
            self.state = 2043
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (OParser.LPAR - 16)) | (1 << (OParser.LBRAK - 16)) | (1 << (OParser.BOOLEAN - 16)) | (1 << (OParser.CHARACTER - 16)) | (1 << (OParser.TEXT - 16)) | (1 << (OParser.INTEGER - 16)) | (1 << (OParser.DECIMAL - 16)) | (1 << (OParser.DATE - 16)) | (1 << (OParser.TIME - 16)) | (1 << (OParser.DATETIME - 16)) | (1 << (OParser.PERIOD - 16)) | (1 << (OParser.VERSION - 16)) | (1 << (OParser.UUID - 16)) | (1 << (OParser.HTML - 16)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.THIS - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.BOOLEAN_LITERAL - 118)) | (1 << (OParser.CHAR_LITERAL - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)) | (1 << (OParser.DOLLAR_IDENTIFIER - 118)) | (1 << (OParser.TEXT_LITERAL - 118)) | (1 << (OParser.INTEGER_LITERAL - 118)) | (1 << (OParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 2042
                localctx.args = self.javascript_arguments(0)


            self.state = 2045
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_argumentsContext)
            super(OParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentList"):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentList"):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_argumentsContext)
            super(OParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(OParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentListItem"):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentListItem"):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 332
        self.enterRecursionRule(localctx, 332, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2048
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2055
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptArgumentListItemContext(self, OParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 2050
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2051
                    self.match(OParser.COMMA)
                    self.state = 2052
                    localctx.item = self.javascript_expression(0) 
                self.state = 2057
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_item_expression"):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_item_expression"):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = OParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2058
            self.match(OParser.LBRAK)
            self.state = 2059
            localctx.exp = self.javascript_expression(0)
            self.state = 2060
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_parenthesis_expression"):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_parenthesis_expression"):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = OParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2062
            self.match(OParser.LPAR)
            self.state = 2063
            localctx.exp = self.javascript_expression(0)
            self.state = 2064
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(OParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier_expression"):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier_expression"):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = OParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2066
            localctx.name = self.javascript_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptIntegerLiteral"):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptIntegerLiteral"):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptBooleanLiteral"):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptBooleanLiteral"):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptCharacterLiteral"):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptCharacterLiteral"):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptTextLiteral"):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptTextLiteral"):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptDecimalLiteral"):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptDecimalLiteral"):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = OParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_javascript_literal_expression)
        try:
            self.state = 2073
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2068
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2069
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2070
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2071
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2072
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def HTML(self):
            return self.getToken(OParser.HTML, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier"):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier"):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = OParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2075
            _la = self._input.LA(1)
            if not(((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.HTML - 46)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)) | (1 << (OParser.DOLLAR_IDENTIFIER - 118)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(OParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_statementContext)
            super(OParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonStatement"):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonStatement"):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_statementContext)
            super(OParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonReturnStatement"):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonReturnStatement"):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = OParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_statement)
        try:
            self.state = 2080
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2077
                self.match(OParser.RETURN)
                self.state = 2078
                localctx.exp = self.python_expression(0)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.HTML, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2079
                localctx.exp = self.python_expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_expressionContext)
            super(OParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(OParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelectorExpression"):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelectorExpression"):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_expressionContext)
            super(OParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(OParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPrimaryExpression"):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPrimaryExpression"):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 346
        self.enterRecursionRule(localctx, 346, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2083
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2089
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,175,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonSelectorExpressionContext(self, OParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2085
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2086
                    localctx.child = self.python_selector_expression() 
                self.state = 2091
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,175,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonParenthesisExpression"):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonParenthesisExpression"):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifierExpression"):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifierExpression"):
                listener.exitPythonIdentifierExpression(self)


    class PythonSelfExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonSelfExpressionContext, self).__init__(parser)
            self.exp = None # Python_self_expressionContext
            self.copyFrom(ctx)

        def python_self_expression(self):
            return self.getTypedRuleContext(OParser.Python_self_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelfExpression"):
                listener.enterPythonSelfExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelfExpression"):
                listener.exitPythonSelfExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(OParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonLiteralExpression"):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonLiteralExpression"):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(OParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonGlobalMethodExpression"):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonGlobalMethodExpression"):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = OParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_python_primary_expression)
        try:
            self.state = 2097
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,176,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonSelfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2092
                localctx.exp = self.python_self_expression()
                pass

            elif la_ == 2:
                localctx = OParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2093
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 3:
                localctx = OParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2094
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 4:
                localctx = OParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2095
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 5:
                localctx = OParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2096
                localctx.exp = self.python_method_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_self_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_self_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_self_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_self_expression"):
                listener.enterPython_self_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_self_expression"):
                listener.exitPython_self_expression(self)




    def python_self_expression(self):

        localctx = OParser.Python_self_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_python_self_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2099
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_selector_expressionContext)
            super(OParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(OParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonMethodExpression"):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonMethodExpression"):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_selector_expressionContext)
            super(OParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonItemExpression"):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonItemExpression"):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = OParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_python_selector_expression)
        try:
            self.state = 2107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2101
                self.match(OParser.DOT)
                self.state = 2102
                localctx.exp = self.python_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2103
                self.match(OParser.LBRAK)
                self.state = 2104
                localctx.exp = self.python_expression(0)
                self.state = 2105
                self.match(OParser.RBRAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_method_expression"):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_method_expression"):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = OParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2109
            localctx.name = self.python_identifier()
            self.state = 2110
            self.match(OParser.LPAR)
            self.state = 2112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (OParser.LPAR - 16)) | (1 << (OParser.BOOLEAN - 16)) | (1 << (OParser.CHARACTER - 16)) | (1 << (OParser.TEXT - 16)) | (1 << (OParser.INTEGER - 16)) | (1 << (OParser.DECIMAL - 16)) | (1 << (OParser.DATE - 16)) | (1 << (OParser.TIME - 16)) | (1 << (OParser.DATETIME - 16)) | (1 << (OParser.PERIOD - 16)) | (1 << (OParser.VERSION - 16)) | (1 << (OParser.UUID - 16)) | (1 << (OParser.HTML - 16)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.THIS - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.BOOLEAN_LITERAL - 118)) | (1 << (OParser.CHAR_LITERAL - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)) | (1 << (OParser.DOLLAR_IDENTIFIER - 118)) | (1 << (OParser.TEXT_LITERAL - 118)) | (1 << (OParser.INTEGER_LITERAL - 118)) | (1 << (OParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 2111
                localctx.args = self.python_argument_list()


            self.state = 2114
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalOnlyArgumentList"):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalOnlyArgumentList"):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedOnlyArgumentList"):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedOnlyArgumentList"):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonArgumentList"):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonArgumentList"):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = OParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_python_argument_list)
        try:
            self.state = 2122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2116
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = OParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2117
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2118
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2119
                self.match(OParser.COMMA)
                self.state = 2120
                localctx.named = self.python_named_argument_list(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_ordinal_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_ordinal_argument_listContext)
            super(OParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentList"):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentList"):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_ordinal_argument_listContext)
            super(OParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentListItem"):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentListItem"):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2125
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,180,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonOrdinalArgumentListItemContext(self, OParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2127
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2128
                    self.match(OParser.COMMA)
                    self.state = 2129
                    localctx.item = self.python_expression(0) 
                self.state = 2134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,180,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_named_argument_listContext)
            super(OParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(OParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentList"):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentList"):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_named_argument_listContext)
            super(OParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def EQ(self):
            return self.getToken(OParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentListItem"):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentListItem"):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2136
            localctx.name = self.python_identifier()
            self.state = 2137
            self.match(OParser.EQ)
            self.state = 2138
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,181,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonNamedArgumentListItemContext(self, OParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2140
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2141
                    self.match(OParser.COMMA)
                    self.state = 2142
                    localctx.name = self.python_identifier()
                    self.state = 2143
                    self.match(OParser.EQ)
                    self.state = 2144
                    localctx.exp = self.python_expression(0) 
                self.state = 2150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,181,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_parenthesis_expression"):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_parenthesis_expression"):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = OParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2151
            self.match(OParser.LPAR)
            self.state = 2152
            localctx.exp = self.python_expression(0)
            self.state = 2153
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonChildIdentifier"):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonChildIdentifier"):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPromptoIdentifier"):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPromptoIdentifier"):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifier"):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifier"):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 364
        self.enterRecursionRule(localctx, 364, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2156
                self.match(OParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.HTML, OParser.NONE, OParser.NULL, OParser.READ, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2157
                localctx.name = self.python_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,183,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonChildIdentifierContext(self, OParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2160
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2161
                    self.match(OParser.DOT)
                    self.state = 2162
                    localctx.name = self.python_identifier() 
                self.state = 2167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,183,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIntegerLiteral"):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIntegerLiteral"):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonBooleanLiteral"):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonBooleanLiteral"):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonCharacterLiteral"):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonCharacterLiteral"):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonTextLiteral"):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonTextLiteral"):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonDecimalLiteral"):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonDecimalLiteral"):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = OParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_python_literal_expression)
        try:
            self.state = 2173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2168
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2169
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2170
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2171
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2172
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def HTML(self):
            return self.getToken(OParser.HTML, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_python_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_identifier"):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_identifier"):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = OParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2175
            _la = self._input.LA(1)
            if not(((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.HTML - 46)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.THIS - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(OParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_statementContext)
            super(OParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaReturnStatement"):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaReturnStatement"):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_statementContext)
            super(OParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaStatement"):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaStatement"):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = OParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_statement)
        try:
            self.state = 2184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2177
                self.match(OParser.RETURN)
                self.state = 2178
                localctx.exp = self.java_expression(0)
                self.state = 2179
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.HTML, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2181
                localctx.exp = self.java_expression(0)
                self.state = 2182
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_expressionContext)
            super(OParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(OParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaSelectorExpression"):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaSelectorExpression"):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_expressionContext)
            super(OParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(OParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaPrimaryExpression"):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaPrimaryExpression"):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 372
        self.enterRecursionRule(localctx, 372, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2187
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaSelectorExpressionContext(self, OParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2189
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2190
                    localctx.child = self.java_selector_expression() 
                self.state = 2195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(OParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(OParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(OParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_primary_expression"):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_primary_expression"):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = OParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_primary_expression)
        try:
            self.state = 2201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,187,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2196
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2197
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2198
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2199
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2200
                self.java_literal_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_this_expression"):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_this_expression"):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = OParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2203
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(OParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(OParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_new_expression"):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_new_expression"):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = OParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2205
            self.new_token()
            self.state = 2206
            self.java_method_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_selector_expressionContext)
            super(OParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(OParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaItemExpression"):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaItemExpression"):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_selector_expressionContext)
            super(OParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(OParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaMethodExpression"):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaMethodExpression"):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = OParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_selector_expression)
        try:
            self.state = 2211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2208
                self.match(OParser.DOT)
                self.state = 2209
                localctx.exp = self.java_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2210
                localctx.exp = self.java_item_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(OParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(OParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_method_expression"):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_method_expression"):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = OParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2213
            localctx.name = self.java_identifier()
            self.state = 2214
            self.match(OParser.LPAR)
            self.state = 2216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (OParser.LPAR - 16)) | (1 << (OParser.BOOLEAN - 16)) | (1 << (OParser.CHARACTER - 16)) | (1 << (OParser.TEXT - 16)) | (1 << (OParser.INTEGER - 16)) | (1 << (OParser.DECIMAL - 16)) | (1 << (OParser.DATE - 16)) | (1 << (OParser.TIME - 16)) | (1 << (OParser.DATETIME - 16)) | (1 << (OParser.PERIOD - 16)) | (1 << (OParser.VERSION - 16)) | (1 << (OParser.UUID - 16)) | (1 << (OParser.HTML - 16)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.THIS - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.BOOLEAN_LITERAL - 118)) | (1 << (OParser.CHAR_LITERAL - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)) | (1 << (OParser.NATIVE_IDENTIFIER - 118)) | (1 << (OParser.DOLLAR_IDENTIFIER - 118)) | (1 << (OParser.TEXT_LITERAL - 118)) | (1 << (OParser.INTEGER_LITERAL - 118)) | (1 << (OParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 2215
                localctx.args = self.java_arguments(0)


            self.state = 2218
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_argumentsContext)
            super(OParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(OParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentListItem"):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentListItem"):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_argumentsContext)
            super(OParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentList"):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentList"):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 384
        self.enterRecursionRule(localctx, 384, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2221
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,190,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaArgumentListItemContext(self, OParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2223
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2224
                    self.match(OParser.COMMA)
                    self.state = 2225
                    localctx.item = self.java_expression(0) 
                self.state = 2230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,190,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_item_expression"):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_item_expression"):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = OParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2231
            self.match(OParser.LBRAK)
            self.state = 2232
            localctx.exp = self.java_expression(0)
            self.state = 2233
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_parenthesis_expression"):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_parenthesis_expression"):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = OParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2235
            self.match(OParser.LPAR)
            self.state = 2236
            localctx.exp = self.java_expression(0)
            self.state = 2237
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_identifier_expressionContext)
            super(OParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(OParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIdentifier"):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIdentifier"):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_identifier_expressionContext)
            super(OParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(OParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildIdentifier"):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildIdentifier"):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 390
        self.enterRecursionRule(localctx, 390, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2240
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildIdentifierContext(self, OParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2242
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2243
                    self.match(OParser.DOT)
                    self.state = 2244
                    localctx.name = self.java_identifier() 
                self.state = 2249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_class_identifier_expressionContext)
            super(OParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaClassIdentifier"):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaClassIdentifier"):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_class_identifier_expressionContext)
            super(OParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildClassIdentifier"):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildClassIdentifier"):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 392
        self.enterRecursionRule(localctx, 392, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2251
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,192,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildClassIdentifierContext(self, OParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2253
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2254
                    localctx.name = self.match(OParser.DOLLAR_IDENTIFIER) 
                self.state = 2259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,192,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaBooleanLiteral"):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaBooleanLiteral"):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCharacterLiteral"):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCharacterLiteral"):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIntegerLiteral"):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIntegerLiteral"):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaTextLiteral"):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaTextLiteral"):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaDecimalLiteral"):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaDecimalLiteral"):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = OParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_java_literal_expression)
        try:
            self.state = 2265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2260
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2261
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2262
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2263
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2264
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(OParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def HTML(self):
            return self.getToken(OParser.HTML, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_java_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_identifier"):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_identifier"):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = OParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2267
            _la = self._input.LA(1)
            if not(((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.HTML - 46)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)) | (1 << (OParser.NATIVE_IDENTIFIER - 118)) | (1 << (OParser.DOLLAR_IDENTIFIER - 118)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_statementContext)
            super(OParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpReturnStatement"):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpReturnStatement"):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_statementContext)
            super(OParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpStatement"):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpStatement"):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = OParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_statement)
        try:
            self.state = 2276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2269
                self.match(OParser.RETURN)
                self.state = 2270
                localctx.exp = self.csharp_expression(0)
                self.state = 2271
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.HTML, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2273
                localctx.exp = self.csharp_expression(0)
                self.state = 2274
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_expressionContext)
            super(OParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpSelectorExpression"):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpSelectorExpression"):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_expressionContext)
            super(OParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPrimaryExpression"):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPrimaryExpression"):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 400
        self.enterRecursionRule(localctx, 400, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2279
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpSelectorExpressionContext(self, OParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2281
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2282
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_primary_expression"):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_primary_expression"):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = OParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_primary_expression)
        try:
            self.state = 2293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,196,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2288
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2289
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2290
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2291
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2292
                self.csharp_literal_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_this_expression"):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_this_expression"):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = OParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2295
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(OParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_new_expression"):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_new_expression"):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = OParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2297
            self.new_token()
            self.state = 2298
            self.csharp_method_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_selector_expressionContext)
            super(OParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpMethodExpression"):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpMethodExpression"):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_selector_expressionContext)
            super(OParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpItemExpression"):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpItemExpression"):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = OParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_selector_expression)
        try:
            self.state = 2303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2300
                self.match(OParser.DOT)
                self.state = 2301
                localctx.exp = self.csharp_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2302
                localctx.exp = self.csharp_item_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(OParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(OParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_method_expression"):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_method_expression"):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = OParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2305
            localctx.name = self.csharp_identifier()
            self.state = 2306
            self.match(OParser.LPAR)
            self.state = 2308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (OParser.LPAR - 16)) | (1 << (OParser.BOOLEAN - 16)) | (1 << (OParser.CHARACTER - 16)) | (1 << (OParser.TEXT - 16)) | (1 << (OParser.INTEGER - 16)) | (1 << (OParser.DECIMAL - 16)) | (1 << (OParser.DATE - 16)) | (1 << (OParser.TIME - 16)) | (1 << (OParser.DATETIME - 16)) | (1 << (OParser.PERIOD - 16)) | (1 << (OParser.VERSION - 16)) | (1 << (OParser.UUID - 16)) | (1 << (OParser.HTML - 16)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.THIS - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.BOOLEAN_LITERAL - 118)) | (1 << (OParser.CHAR_LITERAL - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)) | (1 << (OParser.DOLLAR_IDENTIFIER - 118)) | (1 << (OParser.TEXT_LITERAL - 118)) | (1 << (OParser.INTEGER_LITERAL - 118)) | (1 << (OParser.DECIMAL_LITERAL - 118)))) != 0):
                self.state = 2307
                localctx.args = self.csharp_arguments(0)


            self.state = 2310
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_argumentsContext)
            super(OParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentList"):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentList"):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_argumentsContext)
            super(OParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(OParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentListItem"):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentListItem"):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 412
        self.enterRecursionRule(localctx, 412, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2313
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,199,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpArgumentListItemContext(self, OParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2315
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2316
                    self.match(OParser.COMMA)
                    self.state = 2317
                    localctx.item = self.csharp_expression(0) 
                self.state = 2322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,199,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_item_expression"):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_item_expression"):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = OParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2323
            self.match(OParser.LBRAK)
            self.state = 2324
            localctx.exp = self.csharp_expression(0)
            self.state = 2325
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_parenthesis_expression"):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_parenthesis_expression"):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = OParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2327
            self.match(OParser.LPAR)
            self.state = 2328
            localctx.exp = self.csharp_expression(0)
            self.state = 2329
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(OParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIdentifier"):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIdentifier"):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(OParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpChildIdentifier"):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpChildIdentifier"):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPromptoIdentifier"):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPromptoIdentifier"):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 418
        self.enterRecursionRule(localctx, 418, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2332
                self.match(OParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.HTML, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2333
                localctx.name = self.csharp_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,201,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpChildIdentifierContext(self, OParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2336
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2337
                    self.match(OParser.DOT)
                    self.state = 2338
                    localctx.name = self.csharp_identifier() 
                self.state = 2343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,201,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpBooleanLiteral"):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpBooleanLiteral"):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIntegerLiteral"):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIntegerLiteral"):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpDecimalLiteral"):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpDecimalLiteral"):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCharacterLiteral"):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCharacterLiteral"):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpTextLiteral"):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpTextLiteral"):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = OParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_csharp_literal_expression)
        try:
            self.state = 2349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2344
                self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2345
                self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2346
                self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2347
                self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2348
                self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def HTML(self):
            return self.getToken(OParser.HTML, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_identifier"):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_identifier"):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = OParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2351
            _la = self._input.LA(1)
            if not(((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.HTML - 46)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (OParser.NONE - 118)) | (1 << (OParser.NULL - 118)) | (1 << (OParser.READ - 118)) | (1 << (OParser.SELF - 118)) | (1 << (OParser.TEST - 118)) | (1 << (OParser.WRITE - 118)) | (1 << (OParser.SYMBOL_IDENTIFIER - 118)) | (1 << (OParser.TYPE_IDENTIFIER - 118)) | (1 << (OParser.VARIABLE_IDENTIFIER - 118)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_element(self):
            return self.getTypedRuleContext(OParser.Jsx_elementContext,0)


        def jsx_fragment(self):
            return self.getTypedRuleContext(OParser.Jsx_fragmentContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_expression"):
                listener.enterJsx_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_expression"):
                listener.exitJsx_expression(self)




    def jsx_expression(self):

        localctx = OParser.Jsx_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_jsx_expression)
        try:
            self.state = 2355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,203,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2353
                self.jsx_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2354
                self.jsx_fragment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_elementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_elementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_jsx_element

     
        def copyFrom(self, ctx):
            super(OParser.Jsx_elementContext, self).copyFrom(ctx)



    class JsxSelfClosingContext(Jsx_elementContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_elementContext)
            super(OParser.JsxSelfClosingContext, self).__init__(parser)
            self.jsx = None # Jsx_self_closingContext
            self.copyFrom(ctx)

        def jsx_self_closing(self):
            return self.getTypedRuleContext(OParser.Jsx_self_closingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxSelfClosing"):
                listener.enterJsxSelfClosing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxSelfClosing"):
                listener.exitJsxSelfClosing(self)


    class JsxElementContext(Jsx_elementContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_elementContext)
            super(OParser.JsxElementContext, self).__init__(parser)
            self.jsx = None # Jsx_openingContext
            self.children_ = None # Jsx_childrenContext
            self.copyFrom(ctx)

        def jsx_closing(self):
            return self.getTypedRuleContext(OParser.Jsx_closingContext,0)

        def jsx_opening(self):
            return self.getTypedRuleContext(OParser.Jsx_openingContext,0)

        def jsx_children(self):
            return self.getTypedRuleContext(OParser.Jsx_childrenContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxElement"):
                listener.enterJsxElement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxElement"):
                listener.exitJsxElement(self)



    def jsx_element(self):

        localctx = OParser.Jsx_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_jsx_element)
        try:
            self.state = 2364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,205,self._ctx)
            if la_ == 1:
                localctx = OParser.JsxSelfClosingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2357
                localctx.jsx = self.jsx_self_closing()
                pass

            elif la_ == 2:
                localctx = OParser.JsxElementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2358
                localctx.jsx = self.jsx_opening()
                self.state = 2360
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,204,self._ctx)
                if la_ == 1:
                    self.state = 2359
                    localctx.children_ = self.jsx_children()


                self.state = 2362
                self.jsx_closing()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_fragmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_fragmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.children_ = None # Jsx_childrenContext

        def jsx_fragment_start(self):
            return self.getTypedRuleContext(OParser.Jsx_fragment_startContext,0)


        def jsx_fragment_end(self):
            return self.getTypedRuleContext(OParser.Jsx_fragment_endContext,0)


        def jsx_children(self):
            return self.getTypedRuleContext(OParser.Jsx_childrenContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_fragment

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment"):
                listener.enterJsx_fragment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment"):
                listener.exitJsx_fragment(self)




    def jsx_fragment(self):

        localctx = OParser.Jsx_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_jsx_fragment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2366
            self.jsx_fragment_start()
            self.state = 2368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,206,self._ctx)
            if la_ == 1:
                self.state = 2367
                localctx.children_ = self.jsx_children()


            self.state = 2370
            self.jsx_fragment_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_fragment_startContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_fragment_startContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def LTGT(self):
            return self.getToken(OParser.LTGT, 0)

        def getRuleIndex(self):
            return OParser.RULE_jsx_fragment_start

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment_start"):
                listener.enterJsx_fragment_start(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment_start"):
                listener.exitJsx_fragment_start(self)




    def jsx_fragment_start(self):

        localctx = OParser.Jsx_fragment_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_jsx_fragment_start)
        try:
            self.state = 2375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.LT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2372
                self.match(OParser.LT)
                self.state = 2373
                self.match(OParser.GT)
                pass
            elif token in [OParser.LTGT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2374
                self.match(OParser.LTGT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_fragment_endContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_fragment_endContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def getRuleIndex(self):
            return OParser.RULE_jsx_fragment_end

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment_end"):
                listener.enterJsx_fragment_end(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment_end"):
                listener.exitJsx_fragment_end(self)




    def jsx_fragment_end(self):

        localctx = OParser.Jsx_fragment_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_jsx_fragment_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2377
            self.match(OParser.LT)
            self.state = 2378
            self.match(OParser.SLASH)
            self.state = 2379
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_self_closingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_self_closingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext
            self.attributes = None # Jsx_attributeContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(OParser.Jsx_element_nameContext,0)


        def jsx_attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_attributeContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_attributeContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_self_closing

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_self_closing"):
                listener.enterJsx_self_closing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_self_closing"):
                listener.exitJsx_self_closing(self)




    def jsx_self_closing(self):

        localctx = OParser.Jsx_self_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_jsx_self_closing)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2381
            self.match(OParser.LT)
            self.state = 2382
            localctx.name = self.jsx_element_name()
            self.state = 2386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT) | (1 << OParser.SWIFT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.METHOD_T) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ALL - 64)) | (1 << (OParser.ALWAYS - 64)) | (1 << (OParser.AND - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.AS - 64)) | (1 << (OParser.ASC - 64)) | (1 << (OParser.ATTR - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.ATTRIBUTES - 64)) | (1 << (OParser.BINDINGS - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.BY - 64)) | (1 << (OParser.CASE - 64)) | (1 << (OParser.CATCH - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.CLASS - 64)) | (1 << (OParser.CLOSE - 64)) | (1 << (OParser.CONTAINS - 64)) | (1 << (OParser.DEF - 64)) | (1 << (OParser.DEFAULT - 64)) | (1 << (OParser.DEFINE - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DESC - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.DOING - 64)) | (1 << (OParser.EACH - 64)) | (1 << (OParser.ELSE - 64)) | (1 << (OParser.ENUM - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.EXCEPT - 64)) | (1 << (OParser.EXECUTE - 64)) | (1 << (OParser.EXPECTING - 64)) | (1 << (OParser.EXTENDS - 64)) | (1 << (OParser.FETCH - 64)) | (1 << (OParser.FILTERED - 64)) | (1 << (OParser.FINALLY - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.FROM - 64)) | (1 << (OParser.GETTER - 64)) | (1 << (OParser.HAS - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.IN - 64)) | (1 << (OParser.INDEX - 64)) | (1 << (OParser.INVOKE - 64)) | (1 << (OParser.IS - 64)) | (1 << (OParser.MATCHING - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.METHODS - 64)) | (1 << (OParser.MODULO - 64)) | (1 << (OParser.MUTABLE - 64)) | (1 << (OParser.NATIVE - 64)) | (1 << (OParser.NONE - 64)) | (1 << (OParser.NOT - 64)) | (1 << (OParser.NOTHING - 64)) | (1 << (OParser.NULL - 64)) | (1 << (OParser.ON - 64)) | (1 << (OParser.ONE - 64)) | (1 << (OParser.OPEN - 64)) | (1 << (OParser.OPERATOR - 64)) | (1 << (OParser.OR - 64)) | (1 << (OParser.ORDER - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.OTHERWISE - 128)) | (1 << (OParser.PASS - 128)) | (1 << (OParser.RAISE - 128)) | (1 << (OParser.READ - 128)) | (1 << (OParser.RECEIVING - 128)) | (1 << (OParser.RESOURCE - 128)) | (1 << (OParser.RETURN - 128)) | (1 << (OParser.RETURNING - 128)) | (1 << (OParser.ROWS - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.SETTER - 128)) | (1 << (OParser.SINGLETON - 128)) | (1 << (OParser.SORTED - 128)) | (1 << (OParser.STORABLE - 128)) | (1 << (OParser.STORE - 128)) | (1 << (OParser.SWITCH - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.THROW - 128)) | (1 << (OParser.TO - 128)) | (1 << (OParser.TRY - 128)) | (1 << (OParser.VERIFYING - 128)) | (1 << (OParser.WIDGET - 128)) | (1 << (OParser.WITH - 128)) | (1 << (OParser.WHEN - 128)) | (1 << (OParser.WHERE - 128)) | (1 << (OParser.WHILE - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)))) != 0):
                self.state = 2383
                localctx.attributes = self.jsx_attribute()
                self.state = 2388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2389
            self.match(OParser.SLASH)
            self.state = 2390
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_openingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_openingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext
            self.attributes = None # Jsx_attributeContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(OParser.Jsx_element_nameContext,0)


        def jsx_attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_attributeContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_attributeContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_opening

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_opening"):
                listener.enterJsx_opening(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_opening"):
                listener.exitJsx_opening(self)




    def jsx_opening(self):

        localctx = OParser.Jsx_openingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_jsx_opening)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2392
            self.match(OParser.LT)
            self.state = 2393
            localctx.name = self.jsx_element_name()
            self.state = 2397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT) | (1 << OParser.SWIFT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.METHOD_T) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.HTML - 64)) | (1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ALL - 64)) | (1 << (OParser.ALWAYS - 64)) | (1 << (OParser.AND - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.AS - 64)) | (1 << (OParser.ASC - 64)) | (1 << (OParser.ATTR - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.ATTRIBUTES - 64)) | (1 << (OParser.BINDINGS - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.BY - 64)) | (1 << (OParser.CASE - 64)) | (1 << (OParser.CATCH - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.CLASS - 64)) | (1 << (OParser.CLOSE - 64)) | (1 << (OParser.CONTAINS - 64)) | (1 << (OParser.DEF - 64)) | (1 << (OParser.DEFAULT - 64)) | (1 << (OParser.DEFINE - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DESC - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.DOING - 64)) | (1 << (OParser.EACH - 64)) | (1 << (OParser.ELSE - 64)) | (1 << (OParser.ENUM - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.EXCEPT - 64)) | (1 << (OParser.EXECUTE - 64)) | (1 << (OParser.EXPECTING - 64)) | (1 << (OParser.EXTENDS - 64)) | (1 << (OParser.FETCH - 64)) | (1 << (OParser.FILTERED - 64)) | (1 << (OParser.FINALLY - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.FROM - 64)) | (1 << (OParser.GETTER - 64)) | (1 << (OParser.HAS - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.IN - 64)) | (1 << (OParser.INDEX - 64)) | (1 << (OParser.INVOKE - 64)) | (1 << (OParser.IS - 64)) | (1 << (OParser.MATCHING - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.METHODS - 64)) | (1 << (OParser.MODULO - 64)) | (1 << (OParser.MUTABLE - 64)) | (1 << (OParser.NATIVE - 64)) | (1 << (OParser.NONE - 64)) | (1 << (OParser.NOT - 64)) | (1 << (OParser.NOTHING - 64)) | (1 << (OParser.NULL - 64)) | (1 << (OParser.ON - 64)) | (1 << (OParser.ONE - 64)) | (1 << (OParser.OPEN - 64)) | (1 << (OParser.OPERATOR - 64)) | (1 << (OParser.OR - 64)) | (1 << (OParser.ORDER - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.OTHERWISE - 128)) | (1 << (OParser.PASS - 128)) | (1 << (OParser.RAISE - 128)) | (1 << (OParser.READ - 128)) | (1 << (OParser.RECEIVING - 128)) | (1 << (OParser.RESOURCE - 128)) | (1 << (OParser.RETURN - 128)) | (1 << (OParser.RETURNING - 128)) | (1 << (OParser.ROWS - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.SETTER - 128)) | (1 << (OParser.SINGLETON - 128)) | (1 << (OParser.SORTED - 128)) | (1 << (OParser.STORABLE - 128)) | (1 << (OParser.STORE - 128)) | (1 << (OParser.SWITCH - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.THROW - 128)) | (1 << (OParser.TO - 128)) | (1 << (OParser.TRY - 128)) | (1 << (OParser.VERIFYING - 128)) | (1 << (OParser.WIDGET - 128)) | (1 << (OParser.WITH - 128)) | (1 << (OParser.WHEN - 128)) | (1 << (OParser.WHERE - 128)) | (1 << (OParser.WHILE - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)))) != 0):
                self.state = 2394
                localctx.attributes = self.jsx_attribute()
                self.state = 2399
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2400
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_closingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_closingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(OParser.Jsx_element_nameContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_closing

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_closing"):
                listener.enterJsx_closing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_closing"):
                listener.exitJsx_closing(self)




    def jsx_closing(self):

        localctx = OParser.Jsx_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_jsx_closing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2402
            self.match(OParser.LT)
            self.state = 2403
            self.match(OParser.SLASH)
            self.state = 2404
            localctx.name = self.jsx_element_name()
            self.state = 2405
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_element_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_element_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(OParser.DOT)
            else:
                return self.getToken(OParser.DOT, i)

        def getRuleIndex(self):
            return OParser.RULE_jsx_element_name

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_element_name"):
                listener.enterJsx_element_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_element_name"):
                listener.exitJsx_element_name(self)




    def jsx_element_name(self):

        localctx = OParser.Jsx_element_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_jsx_element_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2407
            self.jsx_identifier()
            self.state = 2412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 2408
                self.match(OParser.DOT)
                self.state = 2409
                self.jsx_identifier()
                self.state = 2414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(OParser.Identifier_or_keywordContext,0)


        def jsx_hyphen_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_hyphen_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_hyphen_identifierContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_identifier"):
                listener.enterJsx_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_identifier"):
                listener.exitJsx_identifier(self)




    def jsx_identifier(self):

        localctx = OParser.Jsx_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_jsx_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2415
            self.identifier_or_keyword()
            self.state = 2419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,211,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2416
                    self.jsx_hyphen_identifier() 
                self.state = 2421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,211,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_hyphen_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_hyphen_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def hyphen_identifier(self):
            return self.getTypedRuleContext(OParser.Hyphen_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_hyphen_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_hyphen_identifier"):
                listener.enterJsx_hyphen_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_hyphen_identifier"):
                listener.exitJsx_hyphen_identifier(self)




    def jsx_hyphen_identifier(self):

        localctx = OParser.Jsx_hyphen_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_jsx_hyphen_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2422
            if not self.wasNotWhiteSpace():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNotWhiteSpace()")
            self.state = 2423
            self.match(OParser.MINUS)
            self.state = 2424
            self.hyphen_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hyphen_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Hyphen_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(OParser.Identifier_or_keywordContext,0)


        def getRuleIndex(self):
            return OParser.RULE_hyphen_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterHyphen_identifier"):
                listener.enterHyphen_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHyphen_identifier"):
                listener.exitHyphen_identifier(self)




    def hyphen_identifier(self):

        localctx = OParser.Hyphen_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_hyphen_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2426
            if not self.wasNotWhiteSpace():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNotWhiteSpace()")
            self.state = 2427
            self.identifier_or_keyword()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Identifier_or_keywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Identifier_or_keywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def keyword(self):
            return self.getTypedRuleContext(OParser.KeywordContext,0)


        def getRuleIndex(self):
            return OParser.RULE_identifier_or_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifier_or_keyword"):
                listener.enterIdentifier_or_keyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifier_or_keyword"):
                listener.exitIdentifier_or_keyword(self)




    def identifier_or_keyword(self):

        localctx = OParser.Identifier_or_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_identifier_or_keyword)
        try:
            self.state = 2431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2429
                self.identifier()
                pass
            elif token in [OParser.JAVA, OParser.CSHARP, OParser.PYTHON2, OParser.PYTHON3, OParser.JAVASCRIPT, OParser.SWIFT, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.METHOD_T, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.HTML, OParser.ABSTRACT, OParser.ALL, OParser.ALWAYS, OParser.AND, OParser.ANY, OParser.AS, OParser.ASC, OParser.ATTR, OParser.ATTRIBUTE, OParser.ATTRIBUTES, OParser.BINDINGS, OParser.BREAK, OParser.BY, OParser.CASE, OParser.CATCH, OParser.CATEGORY, OParser.CLASS, OParser.CLOSE, OParser.CONTAINS, OParser.DEF, OParser.DEFAULT, OParser.DEFINE, OParser.DELETE, OParser.DESC, OParser.DO, OParser.DOING, OParser.EACH, OParser.ELSE, OParser.ENUM, OParser.ENUMERATED, OParser.EXCEPT, OParser.EXECUTE, OParser.EXPECTING, OParser.EXTENDS, OParser.FETCH, OParser.FILTERED, OParser.FINALLY, OParser.FLUSH, OParser.FOR, OParser.FROM, OParser.GETTER, OParser.HAS, OParser.IF, OParser.IN, OParser.INDEX, OParser.INVOKE, OParser.IS, OParser.MATCHING, OParser.METHOD, OParser.METHODS, OParser.MODULO, OParser.MUTABLE, OParser.NATIVE, OParser.NONE, OParser.NOT, OParser.NOTHING, OParser.NULL, OParser.ON, OParser.ONE, OParser.OPEN, OParser.OPERATOR, OParser.OR, OParser.ORDER, OParser.OTHERWISE, OParser.PASS, OParser.RAISE, OParser.READ, OParser.RECEIVING, OParser.RESOURCE, OParser.RETURN, OParser.RETURNING, OParser.ROWS, OParser.SELF, OParser.SETTER, OParser.SINGLETON, OParser.SORTED, OParser.STORABLE, OParser.STORE, OParser.SWITCH, OParser.TEST, OParser.THIS, OParser.THROW, OParser.TO, OParser.TRY, OParser.VERIFYING, OParser.WIDGET, OParser.WITH, OParser.WHEN, OParser.WHERE, OParser.WHILE, OParser.WRITE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2430
                self.keyword()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_attributeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_identifierContext
            self.value = None # Jsx_attribute_valueContext

        def jsx_identifier(self):
            return self.getTypedRuleContext(OParser.Jsx_identifierContext,0)


        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def jsx_attribute_value(self):
            return self.getTypedRuleContext(OParser.Jsx_attribute_valueContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_attribute

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_attribute"):
                listener.enterJsx_attribute(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_attribute"):
                listener.exitJsx_attribute(self)




    def jsx_attribute(self):

        localctx = OParser.Jsx_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_jsx_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2433
            localctx.name = self.jsx_identifier()
            self.state = 2436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 2434
                self.match(OParser.EQ)
                self.state = 2435
                localctx.value = self.jsx_attribute_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_attribute_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_attribute_valueContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_jsx_attribute_value

     
        def copyFrom(self, ctx):
            super(OParser.Jsx_attribute_valueContext, self).copyFrom(ctx)



    class JsxValueContext(Jsx_attribute_valueContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_attribute_valueContext)
            super(OParser.JsxValueContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxValue"):
                listener.enterJsxValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxValue"):
                listener.exitJsxValue(self)


    class JsxLiteralContext(Jsx_attribute_valueContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_attribute_valueContext)
            super(OParser.JsxLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJsxLiteral"):
                listener.enterJsxLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxLiteral"):
                listener.exitJsxLiteral(self)



    def jsx_attribute_value(self):

        localctx = OParser.Jsx_attribute_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_jsx_attribute_value)
        try:
            self.state = 2443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JsxLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2438
                self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.JsxValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2439
                self.match(OParser.LCURL)
                self.state = 2440
                localctx.exp = self.expression(0)
                self.state = 2441
                self.match(OParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_childrenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_childrenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_child(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_childContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_childContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_children

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_children"):
                listener.enterJsx_children(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_children"):
                listener.exitJsx_children(self)




    def jsx_children(self):

        localctx = OParser.Jsx_childrenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_jsx_children)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2446 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2445
                    self.jsx_child()

                else:
                    raise NoViableAltException(self)
                self.state = 2448 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,215,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_childContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_childContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_jsx_child

     
        def copyFrom(self, ctx):
            super(OParser.Jsx_childContext, self).copyFrom(ctx)



    class JsxTextContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_childContext)
            super(OParser.JsxTextContext, self).__init__(parser)
            self.text = None # Jsx_textContext
            self.copyFrom(ctx)

        def jsx_text(self):
            return self.getTypedRuleContext(OParser.Jsx_textContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxText"):
                listener.enterJsxText(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxText"):
                listener.exitJsxText(self)


    class JsxChildContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_childContext)
            super(OParser.JsxChildContext, self).__init__(parser)
            self.jsx = None # Jsx_elementContext
            self.copyFrom(ctx)

        def jsx_element(self):
            return self.getTypedRuleContext(OParser.Jsx_elementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxChild"):
                listener.enterJsxChild(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxChild"):
                listener.exitJsxChild(self)


    class JsxCodeContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_childContext)
            super(OParser.JsxCodeContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxCode"):
                listener.enterJsxCode(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxCode"):
                listener.exitJsxCode(self)



    def jsx_child(self):

        localctx = OParser.Jsx_childContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_jsx_child)
        self._la = 0 # Token type
        try:
            self.state = 2457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SPACE, OParser.WS, OParser.LF, OParser.COMMENT, OParser.JAVA, OParser.CSHARP, OParser.PYTHON2, OParser.PYTHON3, OParser.JAVASCRIPT, OParser.SWIFT, OParser.COLON, OParser.SEMI, OParser.COMMA, OParser.RANGE, OParser.DOT, OParser.LPAR, OParser.RPAR, OParser.LBRAK, OParser.RBRAK, OParser.QMARK, OParser.XMARK, OParser.AMP, OParser.AMP2, OParser.PIPE, OParser.PIPE2, OParser.PLUS, OParser.MINUS, OParser.STAR, OParser.SLASH, OParser.BSLASH, OParser.PERCENT, OParser.GTE, OParser.LTE, OParser.LTGT, OParser.EQ, OParser.XEQ, OParser.EQ2, OParser.TEQ, OParser.TILDE, OParser.LARROW, OParser.RARROW, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.METHOD_T, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.HTML, OParser.ABSTRACT, OParser.ALL, OParser.ALWAYS, OParser.AND, OParser.ANY, OParser.AS, OParser.ASC, OParser.ATTR, OParser.ATTRIBUTE, OParser.ATTRIBUTES, OParser.BINDINGS, OParser.BREAK, OParser.BY, OParser.CASE, OParser.CATCH, OParser.CATEGORY, OParser.CLASS, OParser.CLOSE, OParser.CONTAINS, OParser.DEF, OParser.DEFAULT, OParser.DEFINE, OParser.DELETE, OParser.DESC, OParser.DO, OParser.DOING, OParser.EACH, OParser.ELSE, OParser.ENUM, OParser.ENUMERATED, OParser.EXCEPT, OParser.EXECUTE, OParser.EXPECTING, OParser.EXTENDS, OParser.FETCH, OParser.FILTERED, OParser.FINALLY, OParser.FLUSH, OParser.FOR, OParser.FROM, OParser.GETTER, OParser.HAS, OParser.IF, OParser.IN, OParser.INDEX, OParser.INVOKE, OParser.IS, OParser.MATCHING, OParser.METHOD, OParser.METHODS, OParser.MODULO, OParser.MUTABLE, OParser.NATIVE, OParser.NONE, OParser.NOT, OParser.NOTHING, OParser.NULL, OParser.ON, OParser.ONE, OParser.OPEN, OParser.OPERATOR, OParser.OR, OParser.ORDER, OParser.OTHERWISE, OParser.PASS, OParser.RAISE, OParser.READ, OParser.RECEIVING, OParser.RESOURCE, OParser.RETURN, OParser.RETURNING, OParser.ROWS, OParser.SELF, OParser.SETTER, OParser.SINGLETON, OParser.SORTED, OParser.STORABLE, OParser.STORE, OParser.SWITCH, OParser.TEST, OParser.THIS, OParser.THROW, OParser.TO, OParser.TRY, OParser.VERIFYING, OParser.WIDGET, OParser.WITH, OParser.WHEN, OParser.WHERE, OParser.WHILE, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.UUID_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL, OParser.VERSION_LITERAL]:
                localctx = OParser.JsxTextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2450
                localctx.text = self.jsx_text()
                pass
            elif token in [OParser.LT]:
                localctx = OParser.JsxChildContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2451
                localctx.jsx = self.jsx_element()
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.JsxCodeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2452
                self.match(OParser.LCURL)
                self.state = 2454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (OParser.EXECUTE - 96)) | (1 << (OParser.FETCH - 96)) | (1 << (OParser.FILTERED - 96)) | (1 << (OParser.MUTABLE - 96)) | (1 << (OParser.NULL - 96)) | (1 << (OParser.READ - 96)) | (1 << (OParser.SELF - 96)) | (1 << (OParser.SORTED - 96)) | (1 << (OParser.THIS - 96)) | (1 << (OParser.BOOLEAN_LITERAL - 96)) | (1 << (OParser.CHAR_LITERAL - 96)) | (1 << (OParser.MIN_INTEGER - 96)) | (1 << (OParser.MAX_INTEGER - 96)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (OParser.SYMBOL_IDENTIFIER - 160)) | (1 << (OParser.TYPE_IDENTIFIER - 160)) | (1 << (OParser.VARIABLE_IDENTIFIER - 160)) | (1 << (OParser.TEXT_LITERAL - 160)) | (1 << (OParser.UUID_LITERAL - 160)) | (1 << (OParser.INTEGER_LITERAL - 160)) | (1 << (OParser.HEXA_LITERAL - 160)) | (1 << (OParser.DECIMAL_LITERAL - 160)) | (1 << (OParser.DATETIME_LITERAL - 160)) | (1 << (OParser.TIME_LITERAL - 160)) | (1 << (OParser.DATE_LITERAL - 160)) | (1 << (OParser.PERIOD_LITERAL - 160)) | (1 << (OParser.VERSION_LITERAL - 160)))) != 0):
                    self.state = 2453
                    localctx.exp = self.expression(0)


                self.state = 2456
                self.match(OParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_textContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_textContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.LCURL)
            else:
                return self.getToken(OParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.RCURL)
            else:
                return self.getToken(OParser.RCURL, i)

        def LT(self, i=None):
            if i is None:
                return self.getTokens(OParser.LT)
            else:
                return self.getToken(OParser.LT, i)

        def GT(self, i=None):
            if i is None:
                return self.getTokens(OParser.GT)
            else:
                return self.getToken(OParser.GT, i)

        def getRuleIndex(self):
            return OParser.RULE_jsx_text

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_text"):
                listener.enterJsx_text(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_text"):
                listener.exitJsx_text(self)




    def jsx_text(self):

        localctx = OParser.Jsx_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_jsx_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2460 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2459
                    _la = self._input.LA(1)
                    if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LCURL) | (1 << OParser.RCURL) | (1 << OParser.GT) | (1 << OParser.LT))) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 2462 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,218,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.derived_list_sempred
        self._predicates[18] = self.native_category_binding_list_sempred
        self._predicates[37] = self.else_if_statement_list_sempred
        self._predicates[45] = self.callable_parent_sempred
        self._predicates[47] = self.expression_sempred
        self._predicates[48] = self.an_expression_sempred
        self._predicates[50] = self.instance_expression_sempred
        self._predicates[60] = self.copy_from_sempred
        self._predicates[61] = self.argument_assignment_list_sempred
        self._predicates[80] = self.typedef_sempred
        self._predicates[101] = self.any_type_sempred
        self._predicates[138] = self.assignable_instance_sempred
        self._predicates[139] = self.is_expression_sempred
        self._predicates[146] = self.new_token_sempred
        self._predicates[147] = self.key_token_sempred
        self._predicates[148] = self.module_token_sempred
        self._predicates[149] = self.value_token_sempred
        self._predicates[150] = self.symbols_token_sempred
        self._predicates[160] = self.javascript_expression_sempred
        self._predicates[166] = self.javascript_arguments_sempred
        self._predicates[173] = self.python_expression_sempred
        self._predicates[179] = self.python_ordinal_argument_list_sempred
        self._predicates[180] = self.python_named_argument_list_sempred
        self._predicates[182] = self.python_identifier_expression_sempred
        self._predicates[186] = self.java_expression_sempred
        self._predicates[192] = self.java_arguments_sempred
        self._predicates[195] = self.java_identifier_expression_sempred
        self._predicates[196] = self.java_class_identifier_expression_sempred
        self._predicates[200] = self.csharp_expression_sempred
        self._predicates[206] = self.csharp_arguments_sempred
        self._predicates[209] = self.csharp_identifier_expression_sempred
        self._predicates[222] = self.jsx_hyphen_identifier_sempred
        self._predicates[223] = self.hyphen_identifier_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def derived_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def callable_parent_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 32:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def an_expression_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.willBeAOrAn()
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def copy_from_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.willNotBe(self.equalToken())
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 40:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 41:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def jsx_hyphen_identifier_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.wasNotWhiteSpace()
         

    def hyphen_identifier_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.wasNotWhiteSpace()
         




