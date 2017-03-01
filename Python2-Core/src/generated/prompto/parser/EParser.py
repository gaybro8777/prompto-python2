# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .EParserListener import EParserListener
else:
    from EParserListener import EParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00af\u0926\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1\t\u00d1\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\5\2\u01a9\n\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\5\2\u01b0\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u01ce\n\5\3\6\3\6\3\6\3")
        buf.write(u"\6\5\6\u01d4\n\6\3\6\3\6\3\6\5\6\u01d9\n\6\3\6\3\6\3")
        buf.write(u"\6\3\6\5\6\u01df\n\6\5\6\u01e1\n\6\3\6\5\6\u01e4\n\6")
        buf.write(u"\3\7\3\7\3\7\3\7\5\7\u01ea\n\7\3\7\3\7\5\7\u01ee\n\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01f9\n\7\3")
        buf.write(u"\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0202\n\7\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0211\n")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u021a\n\b\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\5\t\u0221\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\5\n\u022b\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write(u"\3\f\5\f\u0241\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write(u"\5\16\u0258\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\17\3\17\3\17\3\17\5\17\u0265\n\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\5\17\u0270\n\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write(u"\u027e\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\5\20\u028c\n\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u029a\n")
        buf.write(u"\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u02ac\n\22\f\22\16")
        buf.write(u"\22\u02af\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\5\23\u02b9\n\23\5\23\u02bb\n\23\3\24\3\24\3\24\3")
        buf.write(u"\24\3\24\3\24\3\24\5\24\u02c4\n\24\3\24\3\24\5\24\u02c8")
        buf.write(u"\n\24\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u02d0\n\25\3")
        buf.write(u"\25\3\25\5\25\u02d4\n\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\26\3\26\3\26\3\26\5\26\u02e0\n\26\3\26\3\26\3\26\5")
        buf.write(u"\26\u02e5\n\26\3\26\3\26\5\26\u02e9\n\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\5\27\u0304\n\27\3\30\3\30\3\31\3\31\3\31\5\31")
        buf.write(u"\u030b\n\31\3\32\3\32\3\32\5\32\u0310\n\32\3\32\3\32")
        buf.write(u"\5\32\u0314\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\5\33\u0329\n\33\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\35\5\35\u0337\n\35\3\36\3\36")
        buf.write(u"\5\36\u033b\n\36\3\36\5\36\u033e\n\36\3\37\3\37\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(u" \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u035f")
        buf.write(u"\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\5\"\u0372\n\"\3#\3#\3#\3#\3#\5#\u0379")
        buf.write(u"\n#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u039b")
        buf.write(u"\n&\3&\3&\3&\3&\3&\3&\3&\5&\u03a4\n&\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\7\'\u03b9\n\'\f\'\16\'\u03bc\13\'\3(\3(\3(\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u03cb\n)\3)\3)\3)\5)")
        buf.write(u"\u03d0\n)\3)\3)\3)\3)\3)\3)\5)\u03d8\n)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\5)\u03e1\n)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*")
        buf.write(u"\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u03f8\n*\3+\3+\3,\3")
        buf.write(u",\5,\u03fe\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u041c")
        buf.write(u"\n-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-")
        buf.write(u"\u0485\n-\f-\16-\u0488\13-\3.\3.\3.\3.\3.\7.\u048f\n")
        buf.write(u".\f.\16.\u0492\13.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\7\62\u04a4\n\62")
        buf.write(u"\f\62\16\62\u04a7\13\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write(u"\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u04b6\n\63\3")
        buf.write(u"\64\3\64\3\64\5\64\u04bb\n\64\3\65\3\65\3\65\3\65\3\66")
        buf.write(u"\3\66\3\66\3\66\5\66\u04c5\n\66\3\66\3\66\3\66\5\66\u04ca")
        buf.write(u"\n\66\5\66\u04cc\n\66\3\66\3\66\3\66\3\66\5\66\u04d2")
        buf.write(u"\n\66\5\66\u04d4\n\66\5\66\u04d6\n\66\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\38\38\38\38\39\39\39\39\39\39\3:\3:\3:\5:")
        buf.write(u"\u04ea\n:\3:\3:\3:\3:\3:\5:\u04f1\n:\3:\3:\5:\u04f5\n")
        buf.write(u":\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0500\n:\3:\3:\5:\u0504")
        buf.write(u"\n:\3:\3:\3:\5:\u0509\n:\5:\u050b\n:\3;\3;\5;\u050f\n")
        buf.write(u";\3;\3;\3;\3;\3;\3;\5;\u0517\n;\3<\3<\3<\3<\3<\5<\u051e")
        buf.write(u"\n<\5<\u0520\n<\3<\3<\3<\5<\u0525\n<\5<\u0527\n<\3=\3")
        buf.write(u"=\3=\3=\3=\3=\3=\7=\u0530\n=\f=\16=\u0533\13=\3>\3>\3")
        buf.write(u">\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0545\n@")
        buf.write(u"\3A\3A\3A\3A\3B\7B\u054c\nB\fB\16B\u054f\13B\3C\6C\u0552")
        buf.write(u"\nC\rC\16C\u0553\3D\6D\u0557\nD\rD\16D\u0558\3D\3D\3")
        buf.write(u"E\7E\u055e\nE\fE\16E\u0561\13E\3E\3E\3F\3F\3G\5G\u0568")
        buf.write(u"\nG\3G\3G\3G\3H\3H\3H\3H\7H\u0571\nH\fH\16H\u0574\13")
        buf.write(u"H\3I\3I\3I\7I\u0579\nI\fI\16I\u057c\13I\3I\3I\3I\3I\3")
        buf.write(u"I\5I\u0583\nI\3J\3J\3K\3K\5K\u0589\nK\3L\3L\3L\3L\7L")
        buf.write(u"\u058f\nL\fL\16L\u0592\13L\3M\3M\3M\3M\7M\u0598\nM\f")
        buf.write(u"M\16M\u059b\13M\3N\3N\3N\7N\u05a0\nN\fN\16N\u05a3\13")
        buf.write(u"N\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u05af\nO\3P\5P\u05b2")
        buf.write(u"\nP\3P\3P\5P\u05b6\nP\3P\3P\3Q\5Q\u05bb\nQ\3Q\3Q\5Q\u05bf")
        buf.write(u"\nQ\3Q\3Q\3R\3R\3R\7R\u05c6\nR\fR\16R\u05c9\13R\3S\3")
        buf.write(u"S\3S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\5T")
        buf.write(u"\u05dd\nT\3T\3T\3T\3T\3T\3T\3T\3T\7T\u05e7\nT\fT\16T")
        buf.write(u"\u05ea\13T\3U\3U\5U\u05ee\nU\3V\3V\3V\3V\3V\3V\3V\3V")
        buf.write(u"\3V\3V\3V\3V\3V\3V\5V\u05fe\nV\3W\3W\3X\5X\u0603\nX\3")
        buf.write(u"X\3X\3Y\3Y\3Z\3Z\3Z\5Z\u060c\nZ\3[\3[\3[\7[\u0611\n[")
        buf.write(u"\f[\16[\u0614\13[\3\\\3\\\5\\\u0618\n\\\3]\3]\3]\5]\u061d")
        buf.write(u"\n]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3b\3b\7b\u062a\nb\fb\16")
        buf.write(u"b\u062d\13b\3c\3c\5c\u0631\nc\3c\5c\u0634\nc\3d\3d\5")
        buf.write(u"d\u0638\nd\3e\3e\3e\5e\u063d\ne\3f\3f\3f\3g\3g\5g\u0644")
        buf.write(u"\ng\3h\3h\3h\3h\3h\3h\3h\3h\3h\7h\u064f\nh\fh\16h\u0652")
        buf.write(u"\13h\3i\3i\3i\3i\7i\u0658\ni\fi\16i\u065b\13i\3j\3j\3")
        buf.write(u"j\3j\3j\5j\u0662\nj\3k\3k\3k\3k\7k\u0668\nk\fk\16k\u066b")
        buf.write(u"\13k\3l\3l\3l\5l\u0670\nl\3m\3m\3m\3m\3m\3m\3m\3m\3m")
        buf.write(u"\3m\5m\u067c\nm\3n\3n\5n\u0680\nn\3o\3o\3o\3o\3o\3o\7")
        buf.write(u"o\u0688\no\fo\16o\u068b\13o\3p\3p\5p\u068f\np\3q\3q\3")
        buf.write(u"q\3q\5q\u0695\nq\3q\3q\3q\7q\u069a\nq\fq\16q\u069d\13")
        buf.write(u"q\3q\3q\5q\u06a1\nq\3r\3r\3r\7r\u06a6\nr\fr\16r\u06a9")
        buf.write(u"\13r\3s\3s\3s\7s\u06ae\ns\fs\16s\u06b1\13s\3t\3t\3t\3")
        buf.write(u"t\5t\u06b7\nt\3u\3u\3v\3v\3v\3v\7v\u06bf\nv\fv\16v\u06c2")
        buf.write(u"\13v\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\5w\u06ce\nw\3x\3x")
        buf.write(u"\5x\u06d2\nx\3x\5x\u06d5\nx\3y\3y\5y\u06d9\ny\3y\5y\u06dc")
        buf.write(u"\ny\3z\3z\3z\3z\7z\u06e2\nz\fz\16z\u06e5\13z\3{\3{\3")
        buf.write(u"{\3{\7{\u06eb\n{\f{\16{\u06ee\13{\3|\3|\3|\3|\7|\u06f4")
        buf.write(u"\n|\f|\16|\u06f7\13|\3}\3}\3}\3}\7}\u06fd\n}\f}\16}\u0700")
        buf.write(u"\13}\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\5~\u0710")
        buf.write(u"\n~\3\177\3\177\3\177\3\177\3\177\3\177\3\177\3\177\3")
        buf.write(u"\177\3\177\3\177\3\177\3\177\3\177\5\177\u0720\n\177")
        buf.write(u"\3\u0080\3\u0080\3\u0080\7\u0080\u0725\n\u0080\f\u0080")
        buf.write(u"\16\u0080\u0728\13\u0080\3\u0081\3\u0081\3\u0081\3\u0081")
        buf.write(u"\5\u0081\u072e\n\u0081\3\u0082\3\u0082\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0084\3\u0084\5\u0084\u0738\n\u0084")
        buf.write(u"\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085\5\u0085\u073f")
        buf.write(u"\n\u0085\3\u0086\5\u0086\u0742\n\u0086\3\u0086\3\u0086")
        buf.write(u"\5\u0086\u0746\n\u0086\3\u0086\3\u0086\3\u0087\5\u0087")
        buf.write(u"\u074b\n\u0087\3\u0087\3\u0087\5\u0087\u074f\n\u0087")
        buf.write(u"\3\u0087\3\u0087\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088")
        buf.write(u"\7\u0088\u0758\n\u0088\f\u0088\16\u0088\u075b\13\u0088")
        buf.write(u"\5\u0088\u075d\n\u0088\3\u0089\3\u0089\3\u0089\7\u0089")
        buf.write(u"\u0762\n\u0089\f\u0089\16\u0089\u0765\13\u0089\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\3\u008b\3\u008b\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b\u0774")
        buf.write(u"\n\u008b\3\u008c\3\u008c\3\u008c\3\u008c\3\u008d\3\u008d")
        buf.write(u"\3\u008d\3\u008d\3\u008d\7\u008d\u077f\n\u008d\f\u008d")
        buf.write(u"\16\u008d\u0782\13\u008d\3\u008e\3\u008e\3\u008e\3\u008e")
        buf.write(u"\5\u008e\u0788\n\u008e\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0091")
        buf.write(u"\3\u0091\3\u0091\7\u0091\u0797\n\u0091\f\u0091\16\u0091")
        buf.write(u"\u079a\13\u0091\3\u0092\3\u0092\3\u0092\7\u0092\u079f")
        buf.write(u"\n\u0092\f\u0092\16\u0092\u07a2\13\u0092\3\u0092\5\u0092")
        buf.write(u"\u07a5\n\u0092\3\u0093\3\u0093\3\u0093\3\u0093\3\u0093")
        buf.write(u"\3\u0093\5\u0093\u07ad\n\u0093\3\u0094\3\u0094\3\u0094")
        buf.write(u"\3\u0095\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0097")
        buf.write(u"\3\u0097\3\u0097\3\u0098\3\u0098\3\u0098\3\u0099\3\u0099")
        buf.write(u"\3\u009a\3\u009a\3\u009b\3\u009b\3\u009c\3\u009c\3\u009d")
        buf.write(u"\3\u009d\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\5\u009e\u07cf\n\u009e\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\7\u009f\u07d6\n\u009f\f\u009f\16\u009f")
        buf.write(u"\u07d9\13\u009f\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a0\5\u00a0\u07e2\n\u00a0\3\u00a1\3\u00a1")
        buf.write(u"\3\u00a2\3\u00a2\3\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\5\u00a3\u07ee\n\u00a3\3\u00a4\3\u00a4\3\u00a4")
        buf.write(u"\5\u00a4\u07f3\n\u00a4\3\u00a4\3\u00a4\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u07fd\n\u00a5")
        buf.write(u"\f\u00a5\16\u00a5\u0800\13\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\5\u00a9\u0811")
        buf.write(u"\n\u00a9\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ab\5\u00ab")
        buf.write(u"\u0818\n\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\7\u00ac\u081f\n\u00ac\f\u00ac\16\u00ac\u0822\13\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u0828\n\u00ad")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\5\u00ae")
        buf.write(u"\u0830\n\u00ae\3\u00af\3\u00af\3\u00af\5\u00af\u0835")
        buf.write(u"\n\u00af\3\u00af\3\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\5\u00b0\u083f\n\u00b0\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u0847\n\u00b1")
        buf.write(u"\f\u00b1\16\u00b1\u084a\13\u00b1\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\7\u00b2\u0857\n\u00b2\f\u00b2\16\u00b2\u085a")
        buf.write(u"\13\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b4\5\u00b4\u0863\n\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\7\u00b4\u0868\n\u00b4\f\u00b4\16\u00b4\u086b\13\u00b4")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u0872")
        buf.write(u"\n\u00b5\3\u00b6\3\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\5\u00b7\u087d\n\u00b7\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\3\u00b8\3\u00b8\7\u00b8\u0884\n\u00b8")
        buf.write(u"\f\u00b8\16\u00b8\u0887\13\u00b8\3\u00b9\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\3\u00b9\5\u00b9\u088e\n\u00b9\3\u00ba\3\u00ba")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bc\3\u00bc\3\u00bc\5\u00bc")
        buf.write(u"\u0898\n\u00bc\3\u00bd\3\u00bd\3\u00bd\5\u00bd\u089d")
        buf.write(u"\n\u00bd\3\u00bd\3\u00bd\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00be\3\u00be\7\u00be\u08a7\n\u00be\f\u00be\16\u00be")
        buf.write(u"\u08aa\13\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c0\3\u00c0\3\u00c1\3\u00c1\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c1\3\u00c1\7\u00c1\u08ba\n\u00c1\f\u00c1\16\u00c1")
        buf.write(u"\u08bd\13\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write(u"\7\u00c2\u08c4\n\u00c2\f\u00c2\16\u00c2\u08c7\13\u00c2")
        buf.write(u"\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\5\u00c3\u08ce")
        buf.write(u"\n\u00c3\3\u00c4\3\u00c4\3\u00c5\3\u00c5\3\u00c5\3\u00c5")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u08d9\n\u00c5\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\3\u00c6\7\u00c6\u08e0\n\u00c6")
        buf.write(u"\f\u00c6\16\u00c6\u08e3\13\u00c6\3\u00c7\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c7\5\u00c7\u08ea\n\u00c7\3\u00c8\3\u00c8")
        buf.write(u"\3\u00c9\3\u00c9\3\u00c9\3\u00ca\3\u00ca\3\u00ca\5\u00ca")
        buf.write(u"\u08f4\n\u00ca\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u08f9")
        buf.write(u"\n\u00cb\3\u00cb\3\u00cb\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\3\u00cc\3\u00cc\7\u00cc\u0903\n\u00cc\f\u00cc\16\u00cc")
        buf.write(u"\u0906\13\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00ce")
        buf.write(u"\3\u00ce\3\u00ce\3\u00ce\3\u00cf\3\u00cf\3\u00cf\5\u00cf")
        buf.write(u"\u0913\n\u00cf\3\u00cf\3\u00cf\3\u00cf\7\u00cf\u0918")
        buf.write(u"\n\u00cf\f\u00cf\16\u00cf\u091b\13\u00cf\3\u00d0\3\u00d0")
        buf.write(u"\3\u00d0\3\u00d0\3\u00d0\5\u00d0\u0922\n\u00d0\3\u00d1")
        buf.write(u"\3\u00d1\3\u00d1\2\30\"LXZbx\u00a6\u00ce\u0118\u013c")
        buf.write(u"\u0148\u0156\u0160\u0162\u0166\u016e\u017a\u0180\u0182")
        buf.write(u"\u018a\u0196\u019c\u00d2\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write(u"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`")
        buf.write(u"bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write(u"\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write(u"\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0")
        buf.write(u"\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2")
        buf.write(u"\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4")
        buf.write(u"\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6")
        buf.write(u"\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8")
        buf.write(u"\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a")
        buf.write(u"\u010c\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c")
        buf.write(u"\u011e\u0120\u0122\u0124\u0126\u0128\u012a\u012c\u012e")
        buf.write(u"\u0130\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140")
        buf.write(u"\u0142\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152")
        buf.write(u"\u0154\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164")
        buf.write(u"\u0166\u0168\u016a\u016c\u016e\u0170\u0172\u0174\u0176")
        buf.write(u"\u0178\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188")
        buf.write(u"\u018a\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a")
        buf.write(u"\u019c\u019e\u01a0\2\13\3\2\"#\4\2\u0090\u0090\u00a4")
        buf.write(u"\u00a4\4\2\u008c\u008c\u0094\u0094\4\2KK\\\\\4\2\'\'")
        buf.write(u"vv\b\2\64<\u0086\u0086\u0093\u0093\u009d\u009d\u00a2")
        buf.write(u"\u00a4\u00a6\u00a6\b\2\64<\u0086\u0086\u008c\u008c\u0093")
        buf.write(u"\u0094\u009d\u009d\u00a2\u00a4\7\2\64<\u0086\u0086\u0093")
        buf.write(u"\u0093\u009d\u009d\u00a2\u00a6\7\2\64<\u0086\u0086\u0093")
        buf.write(u"\u0093\u009d\u009d\u00a2\u00a4\u09ad\2\u01a2\3\2\2\2")
        buf.write(u"\4\u01b7\3\2\2\2\6\u01c3\3\2\2\2\b\u01c9\3\2\2\2\n\u01cf")
        buf.write(u"\3\2\2\2\f\u01e5\3\2\2\2\16\u0203\3\2\2\2\20\u0220\3")
        buf.write(u"\2\2\2\22\u0222\3\2\2\2\24\u0232\3\2\2\2\26\u023c\3\2")
        buf.write(u"\2\2\30\u0249\3\2\2\2\32\u0253\3\2\2\2\34\u0260\3\2\2")
        buf.write(u"\2\36\u027f\3\2\2\2 \u029b\3\2\2\2\"\u02a4\3\2\2\2$\u02ba")
        buf.write(u"\3\2\2\2&\u02bc\3\2\2\2(\u02c9\3\2\2\2*\u02db\3\2\2\2")
        buf.write(u",\u02f0\3\2\2\2.\u0305\3\2\2\2\60\u0307\3\2\2\2\62\u030c")
        buf.write(u"\3\2\2\2\64\u0328\3\2\2\2\66\u032a\3\2\2\28\u0336\3\2")
        buf.write(u"\2\2:\u033d\3\2\2\2<\u033f\3\2\2\2>\u0348\3\2\2\2@\u0351")
        buf.write(u"\3\2\2\2B\u0371\3\2\2\2D\u0373\3\2\2\2F\u0381\3\2\2\2")
        buf.write(u"H\u038a\3\2\2\2J\u0391\3\2\2\2L\u03a5\3\2\2\2N\u03bd")
        buf.write(u"\3\2\2\2P\u03c0\3\2\2\2R\u03f7\3\2\2\2T\u03f9\3\2\2\2")
        buf.write(u"V\u03fb\3\2\2\2X\u041b\3\2\2\2Z\u0489\3\2\2\2\\\u0493")
        buf.write(u"\3\2\2\2^\u0497\3\2\2\2`\u049c\3\2\2\2b\u049e\3\2\2\2")
        buf.write(u"d\u04b5\3\2\2\2f\u04b7\3\2\2\2h\u04bc\3\2\2\2j\u04d5")
        buf.write(u"\3\2\2\2l\u04d7\3\2\2\2n\u04dc\3\2\2\2p\u04e0\3\2\2\2")
        buf.write(u"r\u050a\3\2\2\2t\u050c\3\2\2\2v\u0526\3\2\2\2x\u0528")
        buf.write(u"\3\2\2\2z\u0534\3\2\2\2|\u0538\3\2\2\2~\u0544\3\2\2\2")
        buf.write(u"\u0080\u0546\3\2\2\2\u0082\u054d\3\2\2\2\u0084\u0551")
        buf.write(u"\3\2\2\2\u0086\u0556\3\2\2\2\u0088\u055f\3\2\2\2\u008a")
        buf.write(u"\u0564\3\2\2\2\u008c\u0567\3\2\2\2\u008e\u056c\3\2\2")
        buf.write(u"\2\u0090\u057a\3\2\2\2\u0092\u0584\3\2\2\2\u0094\u0588")
        buf.write(u"\3\2\2\2\u0096\u058a\3\2\2\2\u0098\u0593\3\2\2\2\u009a")
        buf.write(u"\u059c\3\2\2\2\u009c\u05ae\3\2\2\2\u009e\u05b1\3\2\2")
        buf.write(u"\2\u00a0\u05ba\3\2\2\2\u00a2\u05c2\3\2\2\2\u00a4\u05ca")
        buf.write(u"\3\2\2\2\u00a6\u05dc\3\2\2\2\u00a8\u05ed\3\2\2\2\u00aa")
        buf.write(u"\u05fd\3\2\2\2\u00ac\u05ff\3\2\2\2\u00ae\u0602\3\2\2")
        buf.write(u"\2\u00b0\u0606\3\2\2\2\u00b2\u060b\3\2\2\2\u00b4\u060d")
        buf.write(u"\3\2\2\2\u00b6\u0617\3\2\2\2\u00b8\u061c\3\2\2\2\u00ba")
        buf.write(u"\u061e\3\2\2\2\u00bc\u0620\3\2\2\2\u00be\u0622\3\2\2")
        buf.write(u"\2\u00c0\u0624\3\2\2\2\u00c2\u0626\3\2\2\2\u00c4\u0633")
        buf.write(u"\3\2\2\2\u00c6\u0637\3\2\2\2\u00c8\u0639\3\2\2\2\u00ca")
        buf.write(u"\u063e\3\2\2\2\u00cc\u0643\3\2\2\2\u00ce\u0645\3\2\2")
        buf.write(u"\2\u00d0\u0653\3\2\2\2\u00d2\u0661\3\2\2\2\u00d4\u0663")
        buf.write(u"\3\2\2\2\u00d6\u066f\3\2\2\2\u00d8\u067b\3\2\2\2\u00da")
        buf.write(u"\u067d\3\2\2\2\u00dc\u0681\3\2\2\2\u00de\u068c\3\2\2")
        buf.write(u"\2\u00e0\u0690\3\2\2\2\u00e2\u06a2\3\2\2\2\u00e4\u06aa")
        buf.write(u"\3\2\2\2\u00e6\u06b6\3\2\2\2\u00e8\u06b8\3\2\2\2\u00ea")
        buf.write(u"\u06ba\3\2\2\2\u00ec\u06cd\3\2\2\2\u00ee\u06cf\3\2\2")
        buf.write(u"\2\u00f0\u06d6\3\2\2\2\u00f2\u06dd\3\2\2\2\u00f4\u06e6")
        buf.write(u"\3\2\2\2\u00f6\u06ef\3\2\2\2\u00f8\u06f8\3\2\2\2\u00fa")
        buf.write(u"\u070f\3\2\2\2\u00fc\u071f\3\2\2\2\u00fe\u0721\3\2\2")
        buf.write(u"\2\u0100\u072d\3\2\2\2\u0102\u072f\3\2\2\2\u0104\u0731")
        buf.write(u"\3\2\2\2\u0106\u0737\3\2\2\2\u0108\u073e\3\2\2\2\u010a")
        buf.write(u"\u0741\3\2\2\2\u010c\u074a\3\2\2\2\u010e\u0752\3\2\2")
        buf.write(u"\2\u0110\u075e\3\2\2\2\u0112\u0766\3\2\2\2\u0114\u0773")
        buf.write(u"\3\2\2\2\u0116\u0775\3\2\2\2\u0118\u0779\3\2\2\2\u011a")
        buf.write(u"\u0787\3\2\2\2\u011c\u0789\3\2\2\2\u011e\u078e\3\2\2")
        buf.write(u"\2\u0120\u0793\3\2\2\2\u0122\u079b\3\2\2\2\u0124\u07ac")
        buf.write(u"\3\2\2\2\u0126\u07ae\3\2\2\2\u0128\u07b1\3\2\2\2\u012a")
        buf.write(u"\u07b4\3\2\2\2\u012c\u07b7\3\2\2\2\u012e\u07ba\3\2\2")
        buf.write(u"\2\u0130\u07bd\3\2\2\2\u0132\u07bf\3\2\2\2\u0134\u07c1")
        buf.write(u"\3\2\2\2\u0136\u07c3\3\2\2\2\u0138\u07c5\3\2\2\2\u013a")
        buf.write(u"\u07ce\3\2\2\2\u013c\u07d0\3\2\2\2\u013e\u07e1\3\2\2")
        buf.write(u"\2\u0140\u07e3\3\2\2\2\u0142\u07e5\3\2\2\2\u0144\u07ed")
        buf.write(u"\3\2\2\2\u0146\u07ef\3\2\2\2\u0148\u07f6\3\2\2\2\u014a")
        buf.write(u"\u0801\3\2\2\2\u014c\u0805\3\2\2\2\u014e\u0809\3\2\2")
        buf.write(u"\2\u0150\u0810\3\2\2\2\u0152\u0812\3\2\2\2\u0154\u0817")
        buf.write(u"\3\2\2\2\u0156\u0819\3\2\2\2\u0158\u0827\3\2\2\2\u015a")
        buf.write(u"\u082f\3\2\2\2\u015c\u0831\3\2\2\2\u015e\u083e\3\2\2")
        buf.write(u"\2\u0160\u0840\3\2\2\2\u0162\u084b\3\2\2\2\u0164\u085b")
        buf.write(u"\3\2\2\2\u0166\u0862\3\2\2\2\u0168\u0871\3\2\2\2\u016a")
        buf.write(u"\u0873\3\2\2\2\u016c\u087c\3\2\2\2\u016e\u087e\3\2\2")
        buf.write(u"\2\u0170\u088d\3\2\2\2\u0172\u088f\3\2\2\2\u0174\u0891")
        buf.write(u"\3\2\2\2\u0176\u0897\3\2\2\2\u0178\u0899\3\2\2\2\u017a")
        buf.write(u"\u08a0\3\2\2\2\u017c\u08ab\3\2\2\2\u017e\u08af\3\2\2")
        buf.write(u"\2\u0180\u08b3\3\2\2\2\u0182\u08be\3\2\2\2\u0184\u08cd")
        buf.write(u"\3\2\2\2\u0186\u08cf\3\2\2\2\u0188\u08d8\3\2\2\2\u018a")
        buf.write(u"\u08da\3\2\2\2\u018c\u08e9\3\2\2\2\u018e\u08eb\3\2\2")
        buf.write(u"\2\u0190\u08ed\3\2\2\2\u0192\u08f3\3\2\2\2\u0194\u08f5")
        buf.write(u"\3\2\2\2\u0196\u08fc\3\2\2\2\u0198\u0907\3\2\2\2\u019a")
        buf.write(u"\u090b\3\2\2\2\u019c\u0912\3\2\2\2\u019e\u0921\3\2\2")
        buf.write(u"\2\u01a0\u0923\3\2\2\2\u01a2\u01a3\7Z\2\2\u01a3\u01a4")
        buf.write(u"\5\u00be`\2\u01a4\u01a5\7J\2\2\u01a5\u01a8\7b\2\2\u01a6")
        buf.write(u"\u01a9\7T\2\2\u01a7\u01a9\5\u00be`\2\u01a8\u01a6\3\2")
        buf.write(u"\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01af\3\2\2\2\u01aa\u01ab")
        buf.write(u"\5$\23\2\u01ab\u01ac\7\23\2\2\u01ac\u01ad\7H\2\2\u01ad")
        buf.write(u"\u01b0\3\2\2\2\u01ae\u01b0\7\u0099\2\2\u01af\u01aa\3")
        buf.write(u"\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write(u"\u01b2\5\u012e\u0098\2\u01b2\u01b3\7\21\2\2\u01b3\u01b4")
        buf.write(u"\5\u0086D\2\u01b4\u01b5\5\u0098M\2\u01b5\u01b6\5\u0088")
        buf.write(u"E\2\u01b6\3\3\2\2\2\u01b7\u01b8\7Z\2\2\u01b8\u01b9\5")
        buf.write(u"\u00be`\2\u01b9\u01ba\7J\2\2\u01ba\u01bb\7b\2\2\u01bb")
        buf.write(u"\u01bc\5\u00aaV\2\u01bc\u01bd\7\u0099\2\2\u01bd\u01be")
        buf.write(u"\5\u012e\u0098\2\u01be\u01bf\7\21\2\2\u01bf\u01c0\5\u0086")
        buf.write(u"D\2\u01c0\u01c1\5\u0096L\2\u01c1\u01c2\5\u0088E\2\u01c2")
        buf.write(u"\5\3\2\2\2\u01c3\u01c4\5\u00c0a\2\u01c4\u01c5\7\u0099")
        buf.write(u"\2\2\u01c5\u01c6\5X-\2\u01c6\u01c7\7J\2\2\u01c7\u01c8")
        buf.write(u"\5\u012c\u0097\2\u01c8\7\3\2\2\2\u01c9\u01ca\5\u00c0")
        buf.write(u"a\2\u01ca\u01cd\5x=\2\u01cb\u01cc\7H\2\2\u01cc\u01ce")
        buf.write(u"\5z>\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write(u"\t\3\2\2\2\u01cf\u01d0\7Z\2\2\u01d0\u01d1\5\u00bc_\2")
        buf.write(u"\u01d1\u01d3\7J\2\2\u01d2\u01d4\7\u0090\2\2\u01d3\u01d2")
        buf.write(u"\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write(u"\u01d6\5\u00a6T\2\u01d6\u01d8\7M\2\2\u01d7\u01d9\5\u009c")
        buf.write(u"O\2\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01e3")
        buf.write(u"\3\2\2\2\u01da\u01e0\7\u0099\2\2\u01db\u01de\5\u00e2")
        buf.write(u"r\2\u01dc\u01dd\7H\2\2\u01dd\u01df\5\u00ba^\2\u01de\u01dc")
        buf.write(u"\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0")
        buf.write(u"\u01db\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\3\2\2")
        buf.write(u"\2\u01e2\u01e4\7p\2\2\u01e3\u01da\3\2\2\2\u01e3\u01e4")
        buf.write(u"\3\2\2\2\u01e4\13\3\2\2\2\u01e5\u01e6\7Z\2\2\u01e6\u01e7")
        buf.write(u"\5\u00be`\2\u01e7\u01e9\7J\2\2\u01e8\u01ea\7\u0090\2")
        buf.write(u"\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ed")
        buf.write(u"\3\2\2\2\u01eb\u01ee\7T\2\2\u01ec\u01ee\5\20\t\2\u01ed")
        buf.write(u"\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u0201\3\2\2")
        buf.write(u"\2\u01ef\u01f8\5$\23\2\u01f0\u01f1\7\23\2\2\u01f1\u01f2")
        buf.write(u"\7H\2\2\u01f2\u01f3\7u\2\2\u01f3\u01f4\7\21\2\2\u01f4")
        buf.write(u"\u01f5\5\u0086D\2\u01f5\u01f6\5\u00d0i\2\u01f6\u01f7")
        buf.write(u"\5\u0088E\2\u01f7\u01f9\3\2\2\2\u01f8\u01f0\3\2\2\2\u01f8")
        buf.write(u"\u01f9\3\2\2\2\u01f9\u0202\3\2\2\2\u01fa\u01fb\7\u0099")
        buf.write(u"\2\2\u01fb\u01fc\7u\2\2\u01fc\u01fd\7\21\2\2\u01fd\u01fe")
        buf.write(u"\5\u0086D\2\u01fe\u01ff\5\u00d0i\2\u01ff\u0200\5\u0088")
        buf.write(u"E\2\u0200\u0202\3\2\2\2\u0201\u01ef\3\2\2\2\u0201\u01fa")
        buf.write(u"\3\2\2\2\u0201\u0202\3\2\2\2\u0202\r\3\2\2\2\u0203\u0204")
        buf.write(u"\7Z\2\2\u0204\u0205\5\u00be`\2\u0205\u0206\7J\2\2\u0206")
        buf.write(u"\u0219\7\u008e\2\2\u0207\u0210\5$\23\2\u0208\u0209\7")
        buf.write(u"\23\2\2\u0209\u020a\7H\2\2\u020a\u020b\7u\2\2\u020b\u020c")
        buf.write(u"\7\21\2\2\u020c\u020d\5\u0086D\2\u020d\u020e\5\u00d0")
        buf.write(u"i\2\u020e\u020f\5\u0088E\2\u020f\u0211\3\2\2\2\u0210")
        buf.write(u"\u0208\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u021a\3\2\2")
        buf.write(u"\2\u0212\u0213\7\u0099\2\2\u0213\u0214\7u\2\2\u0214\u0215")
        buf.write(u"\7\21\2\2\u0215\u0216\5\u0086D\2\u0216\u0217\5\u00d0")
        buf.write(u"i\2\u0217\u0218\5\u0088E\2\u0218\u021a\3\2\2\2\u0219")
        buf.write(u"\u0207\3\2\2\2\u0219\u0212\3\2\2\2\u0219\u021a\3\2\2")
        buf.write(u"\2\u021a\17\3\2\2\2\u021b\u0221\5\u00b4[\2\u021c\u021d")
        buf.write(u"\5\u00b4[\2\u021d\u021e\7H\2\2\u021e\u021f\5\u00be`\2")
        buf.write(u"\u021f\u0221\3\2\2\2\u0220\u021b\3\2\2\2\u0220\u021c")
        buf.write(u"\3\2\2\2\u0221\21\3\2\2\2\u0222\u0223\7Z\2\2\u0223\u0224")
        buf.write(u"\5\u0124\u0093\2\u0224\u0225\7J\2\2\u0225\u0226\7\u0080")
        buf.write(u"\2\2\u0226\u0227\7\u0087\2\2\u0227\u022a\5\u00c6d\2\u0228")
        buf.write(u"\u0229\7\u008a\2\2\u0229\u022b\5\u00a6T\2\u022a\u0228")
        buf.write(u"\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write(u"\u022d\7^\2\2\u022d\u022e\7\21\2\2\u022e\u022f\5\u0086")
        buf.write(u"D\2\u022f\u0230\5\u00f2z\2\u0230\u0231\5\u0088E\2\u0231")
        buf.write(u"\23\3\2\2\2\u0232\u0233\7Z\2\2\u0233\u0234\5\u00ba^\2")
        buf.write(u"\u0234\u0235\7J\2\2\u0235\u0236\7\u008d\2\2\u0236\u0237")
        buf.write(u"\7^\2\2\u0237\u0238\7\21\2\2\u0238\u0239\5\u0086D\2\u0239")
        buf.write(u"\u023a\5\u00f2z\2\u023a\u023b\5\u0088E\2\u023b\25\3\2")
        buf.write(u"\2\2\u023c\u023d\7Z\2\2\u023d\u023e\5\u00ba^\2\u023e")
        buf.write(u"\u0240\7J\2\2\u023f\u0241\7x\2\2\u0240\u023f\3\2\2\2")
        buf.write(u"\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243")
        buf.write(u"\7\u008d\2\2\u0243\u0244\7^\2\2\u0244\u0245\7\21\2\2")
        buf.write(u"\u0245\u0246\5\u0086D\2\u0246\u0247\5\u00eav\2\u0247")
        buf.write(u"\u0248\5\u0088E\2\u0248\27\3\2\2\2\u0249\u024a\7Z\2\2")
        buf.write(u"\u024a\u024b\5\u00ba^\2\u024b\u024c\7J\2\2\u024c\u024d")
        buf.write(u"\7m\2\2\u024d\u024e\7^\2\2\u024e\u024f\7\21\2\2\u024f")
        buf.write(u"\u0250\5\u0086D\2\u0250\u0251\5\u00f2z\2\u0251\u0252")
        buf.write(u"\5\u0088E\2\u0252\31\3\2\2\2\u0253\u0254\7Z\2\2\u0254")
        buf.write(u"\u0255\5\u00ba^\2\u0255\u0257\7J\2\2\u0256\u0258\7x\2")
        buf.write(u"\2\u0257\u0256\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259")
        buf.write(u"\3\2\2\2\u0259\u025a\7m\2\2\u025a\u025b\7^\2\2\u025b")
        buf.write(u"\u025c\7\21\2\2\u025c\u025d\5\u0086D\2\u025d\u025e\5")
        buf.write(u"\u00eav\2\u025e\u025f\5\u0088E\2\u025f\33\3\2\2\2\u0260")
        buf.write(u"\u0261\7Z\2\2\u0261\u0262\5\u00be`\2\u0262\u0264\7J\2")
        buf.write(u"\2\u0263\u0265\7\u0090\2\2\u0264\u0263\3\2\2\2\u0264")
        buf.write(u"\u0265\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0267\7x\2\2")
        buf.write(u"\u0267\u026f\7T\2\2\u0268\u0269\5$\23\2\u0269\u026a\7")
        buf.write(u"\23\2\2\u026a\u026b\7H\2\2\u026b\u026c\7O\2\2\u026c\u0270")
        buf.write(u"\3\2\2\2\u026d\u026e\7\u0099\2\2\u026e\u0270\7O\2\2\u026f")
        buf.write(u"\u0268\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\3\2\2")
        buf.write(u"\2\u0271\u0272\7\21\2\2\u0272\u0273\5\u0086D\2\u0273")
        buf.write(u"\u0274\5 \21\2\u0274\u027d\5\u0088E\2\u0275\u0276\5\u0084")
        buf.write(u"C\2\u0276\u0277\7H\2\2\u0277\u0278\7u\2\2\u0278\u0279")
        buf.write(u"\7\21\2\2\u0279\u027a\5\u0086D\2\u027a\u027b\5\u00d4")
        buf.write(u"k\2\u027b\u027c\5\u0088E\2\u027c\u027e\3\2\2\2\u027d")
        buf.write(u"\u0275\3\2\2\2\u027d\u027e\3\2\2\2\u027e\35\3\2\2\2\u027f")
        buf.write(u"\u0280\7Z\2\2\u0280\u0281\5\u00be`\2\u0281\u0282\7J\2")
        buf.write(u"\2\u0282\u0283\7x\2\2\u0283\u028b\7\u0088\2\2\u0284\u0285")
        buf.write(u"\5$\23\2\u0285\u0286\7\23\2\2\u0286\u0287\7H\2\2\u0287")
        buf.write(u"\u0288\7O\2\2\u0288\u028c\3\2\2\2\u0289\u028a\7\u0099")
        buf.write(u"\2\2\u028a\u028c\7O\2\2\u028b\u0284\3\2\2\2\u028b\u0289")
        buf.write(u"\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028e\7\21\2\2\u028e")
        buf.write(u"\u028f\5\u0086D\2\u028f\u0290\5 \21\2\u0290\u0299\5\u0088")
        buf.write(u"E\2\u0291\u0292\5\u0084C\2\u0292\u0293\7H\2\2\u0293\u0294")
        buf.write(u"\7u\2\2\u0294\u0295\7\21\2\2\u0295\u0296\5\u0086D\2\u0296")
        buf.write(u"\u0297\5\u00d4k\2\u0297\u0298\5\u0088E\2\u0298\u029a")
        buf.write(u"\3\2\2\2\u0299\u0291\3\2\2\2\u0299\u029a\3\2\2\2\u029a")
        buf.write(u"\37\3\2\2\2\u029b\u029c\7Z\2\2\u029c\u029d\7T\2\2\u029d")
        buf.write(u"\u029e\7O\2\2\u029e\u029f\7J\2\2\u029f\u02a0\7\21\2\2")
        buf.write(u"\u02a0\u02a1\5\u0086D\2\u02a1\u02a2\5\"\22\2\u02a2\u02a3")
        buf.write(u"\5\u0088E\2\u02a3!\3\2\2\2\u02a4\u02a5\b\22\1\2\u02a5")
        buf.write(u"\u02a6\5\u00d8m\2\u02a6\u02ad\3\2\2\2\u02a7\u02a8\f\3")
        buf.write(u"\2\2\u02a8\u02a9\5\u0084C\2\u02a9\u02aa\5\u00d8m\2\u02aa")
        buf.write(u"\u02ac\3\2\2\2\u02ab\u02a7\3\2\2\2\u02ac\u02af\3\2\2")
        buf.write(u"\2\u02ad\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae#\3\2")
        buf.write(u"\2\2\u02af\u02ad\3\2\2\2\u02b0\u02b1\7\u0099\2\2\u02b1")
        buf.write(u"\u02b2\7M\2\2\u02b2\u02bb\5\u00bc_\2\u02b3\u02b4\7\u0099")
        buf.write(u"\2\2\u02b4\u02b5\7N\2\2\u02b5\u02b8\5\u00e4s\2\u02b6")
        buf.write(u"\u02b7\7H\2\2\u02b7\u02b9\5\u00bc_\2\u02b8\u02b6\3\2")
        buf.write(u"\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02bb\3\2\2\2\u02ba\u02b0")
        buf.write(u"\3\2\2\2\u02ba\u02b3\3\2\2\2\u02bb%\3\2\2\2\u02bc\u02bd")
        buf.write(u"\7Z\2\2\u02bd\u02be\5\u00b6\\\2\u02be\u02bf\7J\2\2\u02bf")
        buf.write(u"\u02c0\7E\2\2\u02c0\u02c3\7t\2\2\u02c1\u02c2\7\u0087")
        buf.write(u"\2\2\u02c2\u02c4\5\60\31\2\u02c3\u02c1\3\2\2\2\u02c3")
        buf.write(u"\u02c4\3\2\2\2\u02c4\u02c7\3\2\2\2\u02c5\u02c6\7\u008a")
        buf.write(u"\2\2\u02c6\u02c8\5\u00a6T\2\u02c7\u02c5\3\2\2\2\u02c7")
        buf.write(u"\u02c8\3\2\2\2\u02c8\'\3\2\2\2\u02c9\u02ca\7Z\2\2\u02ca")
        buf.write(u"\u02cb\5\u00b6\\\2\u02cb\u02cc\7J\2\2\u02cc\u02cf\7t")
        buf.write(u"\2\2\u02cd\u02ce\7\u0087\2\2\u02ce\u02d0\5\60\31\2\u02cf")
        buf.write(u"\u02cd\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0\u02d3\3\2\2")
        buf.write(u"\2\u02d1\u02d2\7\u008a\2\2\u02d2\u02d4\5\u00a6T\2\u02d3")
        buf.write(u"\u02d1\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02d5\3\2\2")
        buf.write(u"\2\u02d5\u02d6\7^\2\2\u02d6\u02d7\7\21\2\2\u02d7\u02d8")
        buf.write(u"\5\u0086D\2\u02d8\u02d9\5\u00f2z\2\u02d9\u02da\5\u0088")
        buf.write(u"E\2\u02da)\3\2\2\2\u02db\u02dc\7Z\2\2\u02dc\u02dd\5\u00b6")
        buf.write(u"\\\2\u02dd\u02df\7J\2\2\u02de\u02e0\7x\2\2\u02df\u02de")
        buf.write(u"\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1")
        buf.write(u"\u02e4\7t\2\2\u02e2\u02e3\7\u0087\2\2\u02e3\u02e5\5\60")
        buf.write(u"\31\2\u02e4\u02e2\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02e8")
        buf.write(u"\3\2\2\2\u02e6\u02e7\7\u008a\2\2\u02e7\u02e9\5\u00cc")
        buf.write(u"g\2\u02e8\u02e6\3\2\2\2\u02e8\u02e9\3\2\2\2\u02e9\u02ea")
        buf.write(u"\3\2\2\2\u02ea\u02eb\7^\2\2\u02eb\u02ec\7\21\2\2\u02ec")
        buf.write(u"\u02ed\5\u0086D\2\u02ed\u02ee\5\u00eav\2\u02ee\u02ef")
        buf.write(u"\5\u0088E\2\u02ef+\3\2\2\2\u02f0\u02f1\7Z\2\2\u02f1\u02f2")
        buf.write(u"\7\u00a7\2\2\u02f2\u02f3\7J\2\2\u02f3\u02f4\7\u0093\2")
        buf.write(u"\2\u02f4\u02f5\7t\2\2\u02f5\u02f6\7^\2\2\u02f6\u02f7")
        buf.write(u"\7\21\2\2\u02f7\u02f8\5\u0086D\2\u02f8\u02f9\5\u00f2")
        buf.write(u"z\2\u02f9\u02fa\5\u0088E\2\u02fa\u02fb\5\u0084C\2\u02fb")
        buf.write(u"\u02fc\7H\2\2\u02fc\u0303\7\u0098\2\2\u02fd\u02fe\7\21")
        buf.write(u"\2\2\u02fe\u02ff\5\u0086D\2\u02ff\u0300\5\u00f4{\2\u0300")
        buf.write(u"\u0301\5\u0088E\2\u0301\u0304\3\2\2\2\u0302\u0304\5\u00c0")
        buf.write(u"a\2\u0303\u02fd\3\2\2\2\u0303\u0302\3\2\2\2\u0304-\3")
        buf.write(u"\2\2\2\u0305\u0306\5X-\2\u0306/\3\2\2\2\u0307\u030a\5")
        buf.write(u"\u00c2b\2\u0308\u0309\7H\2\2\u0309\u030b\5\u00c4c\2\u030a")
        buf.write(u"\u0308\3\2\2\2\u030a\u030b\3\2\2\2\u030b\61\3\2\2\2\u030c")
        buf.write(u"\u030d\5\u00ccg\2\u030d\u030f\5\u00ba^\2\u030e\u0310")
        buf.write(u"\5$\23\2\u030f\u030e\3\2\2\2\u030f\u0310\3\2\2\2\u0310")
        buf.write(u"\u0313\3\2\2\2\u0311\u0312\7-\2\2\u0312\u0314\5\u0106")
        buf.write(u"\u0084\2\u0313\u0311\3\2\2\2\u0313\u0314\3\2\2\2\u0314")
        buf.write(u"\63\3\2\2\2\u0315\u0329\5|?\2\u0316\u0329\5:\36\2\u0317")
        buf.write(u"\u0329\5\u0080A\2\u0318\u0329\58\35\2\u0319\u0329\5\66")
        buf.write(u"\34\2\u031a\u0329\5T+\2\u031b\u0329\5V,\2\u031c\u0329")
        buf.write(u"\5J&\2\u031d\u0329\5@!\2\u031e\u0329\5D#\2\u031f\u0329")
        buf.write(u"\5H%\2\u0320\u0329\5F$\2\u0321\u0329\5N(\2\u0322\u0329")
        buf.write(u"\5P)\2\u0323\u0329\5l\67\2\u0324\u0329\5<\37\2\u0325")
        buf.write(u"\u0329\5> \2\u0326\u0329\5(\25\2\u0327\u0329\5\u00e8")
        buf.write(u"u\2\u0328\u0315\3\2\2\2\u0328\u0316\3\2\2\2\u0328\u0317")
        buf.write(u"\3\2\2\2\u0328\u0318\3\2\2\2\u0328\u0319\3\2\2\2\u0328")
        buf.write(u"\u031a\3\2\2\2\u0328\u031b\3\2\2\2\u0328\u031c\3\2\2")
        buf.write(u"\2\u0328\u031d\3\2\2\2\u0328\u031e\3\2\2\2\u0328\u031f")
        buf.write(u"\3\2\2\2\u0328\u0320\3\2\2\2\u0328\u0321\3\2\2\2\u0328")
        buf.write(u"\u0322\3\2\2\2\u0328\u0323\3\2\2\2\u0328\u0324\3\2\2")
        buf.write(u"\2\u0328\u0325\3\2\2\2\u0328\u0326\3\2\2\2\u0328\u0327")
        buf.write(u"\3\2\2\2\u0329\65\3\2\2\2\u032a\u032b\7j\2\2\u032b\67")
        buf.write(u"\3\2\2\2\u032c\u032d\7[\2\2\u032d\u0337\5\u00a2R\2\u032e")
        buf.write(u"\u032f\7\u0091\2\2\u032f\u0337\5\u00a2R\2\u0330\u0331")
        buf.write(u"\7[\2\2\u0331\u0332\5\u00a2R\2\u0332\u0333\7H\2\2\u0333")
        buf.write(u"\u0334\7\u0091\2\2\u0334\u0335\5\u00a2R\2\u0335\u0337")
        buf.write(u"\3\2\2\2\u0336\u032c\3\2\2\2\u0336\u032e\3\2\2\2\u0336")
        buf.write(u"\u0330\3\2\2\2\u03379\3\2\2\2\u0338\u033a\5Z.\2\u0339")
        buf.write(u"\u033b\5v<\2\u033a\u0339\3\2\2\2\u033a\u033b\3\2\2\2")
        buf.write(u"\u033b\u033e\3\2\2\2\u033c\u033e\5^\60\2\u033d\u0338")
        buf.write(u"\3\2\2\2\u033d\u033c\3\2\2\2\u033e;\3\2\2\2\u033f\u0340")
        buf.write(u"\7\u0099\2\2\u0340\u0341\5\u0116\u008c\2\u0341\u0342")
        buf.write(u"\7\23\2\2\u0342\u0343\7]\2\2\u0343\u0344\7\21\2\2\u0344")
        buf.write(u"\u0345\5\u0086D\2\u0345\u0346\5\u00f2z\2\u0346\u0347")
        buf.write(u"\5\u0088E\2\u0347=\3\2\2\2\u0348\u0349\7\u0099\2\2\u0349")
        buf.write(u"\u034a\5\u00be`\2\u034a\u034b\7\23\2\2\u034b\u034c\7")
        buf.write(u"]\2\2\u034c\u034d\7\21\2\2\u034d\u034e\5\u0086D\2\u034e")
        buf.write(u"\u034f\5\u00f2z\2\u034f\u0350\5\u0088E\2\u0350?\3\2\2")
        buf.write(u"\2\u0351\u0352\7\u0092\2\2\u0352\u0353\7}\2\2\u0353\u0354")
        buf.write(u"\5X-\2\u0354\u0355\7\21\2\2\u0355\u0356\5\u0086D\2\u0356")
        buf.write(u"\u035e\5\u00f6|\2\u0357\u0358\5\u0084C\2\u0358\u0359")
        buf.write(u"\7\u0083\2\2\u0359\u035a\7\21\2\2\u035a\u035b\5\u0086")
        buf.write(u"D\2\u035b\u035c\5\u00f2z\2\u035c\u035d\5\u0088E\2\u035d")
        buf.write(u"\u035f\3\2\2\2\u035e\u0357\3\2\2\2\u035e\u035f\3\2\2")
        buf.write(u"\2\u035f\u0360\3\2\2\2\u0360\u0361\5\u0088E\2\u0361A")
        buf.write(u"\3\2\2\2\u0362\u0363\7\u009a\2\2\u0363\u0364\5\u00fc")
        buf.write(u"\177\2\u0364\u0365\7\21\2\2\u0365\u0366\5\u0086D\2\u0366")
        buf.write(u"\u0367\5\u00f2z\2\u0367\u0368\5\u0088E\2\u0368\u0372")
        buf.write(u"\3\2\2\2\u0369\u036a\7\u009a\2\2\u036a\u036b\7o\2\2\u036b")
        buf.write(u"\u036c\5\u00fa~\2\u036c\u036d\7\21\2\2\u036d\u036e\5")
        buf.write(u"\u0086D\2\u036e\u036f\5\u00f2z\2\u036f\u0370\5\u0088")
        buf.write(u"E\2\u0370\u0372\3\2\2\2\u0371\u0362\3\2\2\2\u0371\u0369")
        buf.write(u"\3\2\2\2\u0372C\3\2\2\2\u0373\u0374\7k\2\2\u0374\u0375")
        buf.write(u"\7_\2\2\u0375\u0378\5\u00ba^\2\u0376\u0377\7\23\2\2\u0377")
        buf.write(u"\u0379\5\u00ba^\2\u0378\u0376\3\2\2\2\u0378\u0379\3\2")
        buf.write(u"\2\2\u0379\u037a\3\2\2\2\u037a\u037b\7o\2\2\u037b\u037c")
        buf.write(u"\5X-\2\u037c\u037d\7\21\2\2\u037d\u037e\5\u0086D\2\u037e")
        buf.write(u"\u037f\5\u00f2z\2\u037f\u0380\5\u0088E\2\u0380E\3\2\2")
        buf.write(u"\2\u0381\u0382\7]\2\2\u0382\u0383\7\21\2\2\u0383\u0384")
        buf.write(u"\5\u0086D\2\u0384\u0385\5\u00f2z\2\u0385\u0386\5\u0088")
        buf.write(u"E\2\u0386\u0387\5\u0084C\2\u0387\u0388\7\u009c\2\2\u0388")
        buf.write(u"\u0389\5X-\2\u0389G\3\2\2\2\u038a\u038b\7\u009c\2\2\u038b")
        buf.write(u"\u038c\5X-\2\u038c\u038d\7\21\2\2\u038d\u038e\5\u0086")
        buf.write(u"D\2\u038e\u038f\5\u00f2z\2\u038f\u0390\5\u0088E\2\u0390")
        buf.write(u"I\3\2\2\2\u0391\u0392\7n\2\2\u0392\u0393\5X-\2\u0393")
        buf.write(u"\u0394\7\21\2\2\u0394\u0395\5\u0086D\2\u0395\u0396\5")
        buf.write(u"\u00f2z\2\u0396\u039a\5\u0088E\2\u0397\u0398\5\u0084")
        buf.write(u"C\2\u0398\u0399\5L\'\2\u0399\u039b\3\2\2\2\u039a\u0397")
        buf.write(u"\3\2\2\2\u039a\u039b\3\2\2\2\u039b\u03a3\3\2\2\2\u039c")
        buf.write(u"\u039d\5\u0084C\2\u039d\u039e\7`\2\2\u039e\u039f\7\21")
        buf.write(u"\2\2\u039f\u03a0\5\u0086D\2\u03a0\u03a1\5\u00f2z\2\u03a1")
        buf.write(u"\u03a2\5\u0088E\2\u03a2\u03a4\3\2\2\2\u03a3\u039c\3\2")
        buf.write(u"\2\2\u03a3\u03a4\3\2\2\2\u03a4K\3\2\2\2\u03a5\u03a6\b")
        buf.write(u"\'\1\2\u03a6\u03a7\7`\2\2\u03a7\u03a8\7n\2\2\u03a8\u03a9")
        buf.write(u"\5X-\2\u03a9\u03aa\7\21\2\2\u03aa\u03ab\5\u0086D\2\u03ab")
        buf.write(u"\u03ac\5\u00f2z\2\u03ac\u03ad\5\u0088E\2\u03ad\u03ba")
        buf.write(u"\3\2\2\2\u03ae\u03af\f\3\2\2\u03af\u03b0\5\u0084C\2\u03b0")
        buf.write(u"\u03b1\7`\2\2\u03b1\u03b2\7n\2\2\u03b2\u03b3\5X-\2\u03b3")
        buf.write(u"\u03b4\7\21\2\2\u03b4\u03b5\5\u0086D\2\u03b5\u03b6\5")
        buf.write(u"\u00f2z\2\u03b6\u03b7\5\u0088E\2\u03b7\u03b9\3\2\2\2")
        buf.write(u"\u03b8\u03ae\3\2\2\2\u03b9\u03bc\3\2\2\2\u03ba\u03b8")
        buf.write(u"\3\2\2\2\u03ba\u03bb\3\2\2\2\u03bbM\3\2\2\2\u03bc\u03ba")
        buf.write(u"\3\2\2\2\u03bd\u03be\7\u0085\2\2\u03be\u03bf\5X-\2\u03bf")
        buf.write(u"O\3\2\2\2\u03c0\u03c1\7\u0092\2\2\u03c1\u03c2\7}\2\2")
        buf.write(u"\u03c2\u03c3\5\u00ba^\2\u03c3\u03c4\7^\2\2\u03c4\u03c5")
        buf.write(u"\7\21\2\2\u03c5\u03c6\5\u0086D\2\u03c6\u03c7\5\u00f2")
        buf.write(u"z\2\u03c7\u03c8\5\u0088E\2\u03c8\u03ca\5\u0082B\2\u03c9")
        buf.write(u"\u03cb\5\u00f8}\2\u03ca\u03c9\3\2\2\2\u03ca\u03cb\3\2")
        buf.write(u"\2\2\u03cb\u03d7\3\2\2\2\u03cc\u03d0\7\u0083\2\2\u03cd")
        buf.write(u"\u03ce\7\u009a\2\2\u03ce\u03d0\7I\2\2\u03cf\u03cc\3\2")
        buf.write(u"\2\2\u03cf\u03cd\3\2\2\2\u03d0\u03d1\3\2\2\2\u03d1\u03d2")
        buf.write(u"\7\21\2\2\u03d2\u03d3\5\u0086D\2\u03d3\u03d4\5\u00f2")
        buf.write(u"z\2\u03d4\u03d5\5\u0088E\2\u03d5\u03d6\5\u0082B\2\u03d6")
        buf.write(u"\u03d8\3\2\2\2\u03d7\u03cf\3\2\2\2\u03d7\u03d8\3\2\2")
        buf.write(u"\2\u03d8\u03e0\3\2\2\2\u03d9\u03da\7G\2\2\u03da\u03db")
        buf.write(u"\7\21\2\2\u03db\u03dc\5\u0086D\2\u03dc\u03dd\5\u00f2")
        buf.write(u"z\2\u03dd\u03de\5\u0088E\2\u03de\u03df\5\u0082B\2\u03df")
        buf.write(u"\u03e1\3\2\2\2\u03e0\u03d9\3\2\2\2\u03e0\u03e1\3\2\2")
        buf.write(u"\2\u03e1\u03e2\3\2\2\2\u03e2\u03e3\5\u0082B\2\u03e3Q")
        buf.write(u"\3\2\2\2\u03e4\u03e5\7\u009a\2\2\u03e5\u03e6\5\u00c0")
        buf.write(u"a\2\u03e6\u03e7\7\21\2\2\u03e7\u03e8\5\u0086D\2\u03e8")
        buf.write(u"\u03e9\5\u00f2z\2\u03e9\u03ea\5\u0088E\2\u03ea\u03eb")
        buf.write(u"\5\u0082B\2\u03eb\u03f8\3\2\2\2\u03ec\u03ed\7\u009a\2")
        buf.write(u"\2\u03ed\u03ee\7o\2\2\u03ee\u03ef\7\30\2\2\u03ef\u03f0")
        buf.write(u"\5\u009aN\2\u03f0\u03f1\7\31\2\2\u03f1\u03f2\7\21\2\2")
        buf.write(u"\u03f2\u03f3\5\u0086D\2\u03f3\u03f4\5\u00f2z\2\u03f4")
        buf.write(u"\u03f5\5\u0088E\2\u03f5\u03f6\5\u0082B\2\u03f6\u03f8")
        buf.write(u"\3\2\2\2\u03f7\u03e4\3\2\2\2\u03f7\u03ec\3\2\2\2\u03f8")
        buf.write(u"S\3\2\2\2\u03f9\u03fa\7P\2\2\u03faU\3\2\2\2\u03fb\u03fd")
        buf.write(u"\7\u0089\2\2\u03fc\u03fe\5X-\2\u03fd\u03fc\3\2\2\2\u03fd")
        buf.write(u"\u03fe\3\2\2\2\u03feW\3\2\2\2\u03ff\u0400\b-\1\2\u0400")
        buf.write(u"\u0401\7#\2\2\u0401\u041c\5X-,\u0402\u0403\7z\2\2\u0403")
        buf.write(u"\u041c\5X-+\u0404\u0405\7>\2\2\u0405\u0406\7\21\2\2\u0406")
        buf.write(u"\u041c\5X-\20\u0407\u041c\5b\62\2\u0408\u041c\5Z.\2\u0409")
        buf.write(u"\u040a\5Z.\2\u040a\u040b\5v<\2\u040b\u041c\3\2\2\2\u040c")
        buf.write(u"\u040d\7d\2\2\u040d\u040e\7\21\2\2\u040e\u041c\5\u00ba")
        buf.write(u"^\2\u040f\u0410\7=\2\2\u0410\u0411\7\21\2\2\u0411\u041c")
        buf.write(u"\5\u00b6\\\2\u0412\u041c\5h\65\2\u0413\u041c\5f\64\2")
        buf.write(u"\u0414\u041c\5j\66\2\u0415\u041c\5r:\2\u0416\u041c\5")
        buf.write(u"\u011c\u008f\2\u0417\u041c\5\u011e\u0090\2\u0418\u041c")
        buf.write(u"\5t;\2\u0419\u041c\5n8\2\u041a\u041c\5^\60\2\u041b\u03ff")
        buf.write(u"\3\2\2\2\u041b\u0402\3\2\2\2\u041b\u0404\3\2\2\2\u041b")
        buf.write(u"\u0407\3\2\2\2\u041b\u0408\3\2\2\2\u041b\u0409\3\2\2")
        buf.write(u"\2\u041b\u040c\3\2\2\2\u041b\u040f\3\2\2\2\u041b\u0412")
        buf.write(u"\3\2\2\2\u041b\u0413\3\2\2\2\u041b\u0414\3\2\2\2\u041b")
        buf.write(u"\u0415\3\2\2\2\u041b\u0416\3\2\2\2\u041b\u0417\3\2\2")
        buf.write(u"\2\u041b\u0418\3\2\2\2\u041b\u0419\3\2\2\2\u041b\u041a")
        buf.write(u"\3\2\2\2\u041c\u0486\3\2\2\2\u041d\u041e\f*\2\2\u041e")
        buf.write(u"\u041f\5\u0132\u009a\2\u041f\u0420\5X-+\u0420\u0485\3")
        buf.write(u"\2\2\2\u0421\u0422\f)\2\2\u0422\u0423\5\u0134\u009b\2")
        buf.write(u"\u0423\u0424\5X-*\u0424\u0485\3\2\2\2\u0425\u0426\f(")
        buf.write(u"\2\2\u0426\u0427\5\u0138\u009d\2\u0427\u0428\5X-)\u0428")
        buf.write(u"\u0485\3\2\2\2\u0429\u042a\f\'\2\2\u042a\u042b\5\u0136")
        buf.write(u"\u009c\2\u042b\u042c\5X-(\u042c\u0485\3\2\2\2\u042d\u042e")
        buf.write(u"\f&\2\2\u042e\u042f\t\2\2\2\u042f\u0485\5X-\'\u0430\u0431")
        buf.write(u"\f%\2\2\u0431\u0432\7*\2\2\u0432\u0485\5X-&\u0433\u0434")
        buf.write(u"\f$\2\2\u0434\u0435\7+\2\2\u0435\u0485\5X-%\u0436\u0437")
        buf.write(u"\f#\2\2\u0437\u0438\7(\2\2\u0438\u0485\5X-$\u0439\u043a")
        buf.write(u"\f\"\2\2\u043a\u043b\7)\2\2\u043b\u0485\5X-#\u043c\u043d")
        buf.write(u"\f\37\2\2\u043d\u043e\7-\2\2\u043e\u0485\5X- \u043f\u0440")
        buf.write(u"\f\36\2\2\u0440\u0441\7,\2\2\u0441\u0485\5X-\37\u0442")
        buf.write(u"\u0443\f\35\2\2\u0443\u0444\7\61\2\2\u0444\u0485\5X-")
        buf.write(u"\36\u0445\u0446\f\34\2\2\u0446\u0447\7\u0081\2\2\u0447")
        buf.write(u"\u0485\5X-\35\u0448\u0449\f\33\2\2\u0449\u044a\7H\2\2")
        buf.write(u"\u044a\u0485\5X-\34\u044b\u044c\f\32\2\2\u044c\u044d")
        buf.write(u"\7n\2\2\u044d\u044e\5X-\2\u044e\u044f\7`\2\2\u044f\u0450")
        buf.write(u"\5X-\33\u0450\u0485\3\2\2\2\u0451\u0452\f\30\2\2\u0452")
        buf.write(u"\u0453\7o\2\2\u0453\u0485\5X-\31\u0454\u0455\f\27\2\2")
        buf.write(u"\u0455\u0456\7W\2\2\u0456\u0485\5X-\30\u0457\u0458\f")
        buf.write(u"\26\2\2\u0458\u0459\7W\2\2\u0459\u045a\7F\2\2\u045a\u0485")
        buf.write(u"\5X-\27\u045b\u045c\f\25\2\2\u045c\u045d\7W\2\2\u045d")
        buf.write(u"\u045e\7I\2\2\u045e\u0485\5X-\26\u045f\u0460\f\24\2\2")
        buf.write(u"\u0460\u0461\7z\2\2\u0461\u0462\7o\2\2\u0462\u0485\5")
        buf.write(u"X-\25\u0463\u0464\f\23\2\2\u0464\u0465\7z\2\2\u0465\u0466")
        buf.write(u"\7W\2\2\u0466\u0485\5X-\24\u0467\u0468\f\22\2\2\u0468")
        buf.write(u"\u0469\7z\2\2\u0469\u046a\7W\2\2\u046a\u046b\7F\2\2\u046b")
        buf.write(u"\u0485\5X-\23\u046c\u046d\f\21\2\2\u046d\u046e\7z\2\2")
        buf.write(u"\u046e\u046f\7W\2\2\u046f\u0470\7I\2\2\u0470\u0485\5")
        buf.write(u"X-\22\u0471\u0472\f\3\2\2\u0472\u0473\7k\2\2\u0473\u0474")
        buf.write(u"\7_\2\2\u0474\u0475\5\u00ba^\2\u0475\u0476\7o\2\2\u0476")
        buf.write(u"\u0477\5X-\4\u0477\u0485\3\2\2\2\u0478\u0479\f!\2\2\u0479")
        buf.write(u"\u047a\7r\2\2\u047a\u047b\7z\2\2\u047b\u0485\5\u011a")
        buf.write(u"\u008e\2\u047c\u047d\f \2\2\u047d\u047e\7r\2\2\u047e")
        buf.write(u"\u0485\5\u011a\u008e\2\u047f\u0480\f\31\2\2\u0480\u0481")
        buf.write(u"\7J\2\2\u0481\u0485\5\u00ccg\2\u0482\u0483\f\n\2\2\u0483")
        buf.write(u"\u0485\5p9\2\u0484\u041d\3\2\2\2\u0484\u0421\3\2\2\2")
        buf.write(u"\u0484\u0425\3\2\2\2\u0484\u0429\3\2\2\2\u0484\u042d")
        buf.write(u"\3\2\2\2\u0484\u0430\3\2\2\2\u0484\u0433\3\2\2\2\u0484")
        buf.write(u"\u0436\3\2\2\2\u0484\u0439\3\2\2\2\u0484\u043c\3\2\2")
        buf.write(u"\2\u0484\u043f\3\2\2\2\u0484\u0442\3\2\2\2\u0484\u0445")
        buf.write(u"\3\2\2\2\u0484\u0448\3\2\2\2\u0484\u044b\3\2\2\2\u0484")
        buf.write(u"\u0451\3\2\2\2\u0484\u0454\3\2\2\2\u0484\u0457\3\2\2")
        buf.write(u"\2\u0484\u045b\3\2\2\2\u0484\u045f\3\2\2\2\u0484\u0463")
        buf.write(u"\3\2\2\2\u0484\u0467\3\2\2\2\u0484\u046c\3\2\2\2\u0484")
        buf.write(u"\u0471\3\2\2\2\u0484\u0478\3\2\2\2\u0484\u047c\3\2\2")
        buf.write(u"\2\u0484\u047f\3\2\2\2\u0484\u0482\3\2\2\2\u0485\u0488")
        buf.write(u"\3\2\2\2\u0486\u0484\3\2\2\2\u0486\u0487\3\2\2\2\u0487")
        buf.write(u"Y\3\2\2\2\u0488\u0486\3\2\2\2\u0489\u048a\b.\1\2\u048a")
        buf.write(u"\u048b\5\u00b8]\2\u048b\u0490\3\2\2\2\u048c\u048d\f\3")
        buf.write(u"\2\2\u048d\u048f\5\\/\2\u048e\u048c\3\2\2\2\u048f\u0492")
        buf.write(u"\3\2\2\2\u0490\u048e\3\2\2\2\u0490\u0491\3\2\2\2\u0491")
        buf.write(u"[\3\2\2\2\u0492\u0490\3\2\2\2\u0493\u0494\6/!\3\u0494")
        buf.write(u"\u0495\7\25\2\2\u0495\u0496\5\u00b8]\2\u0496]\3\2\2\2")
        buf.write(u"\u0497\u0498\7q\2\2\u0498\u0499\7\21\2\2\u0499\u049a")
        buf.write(u"\5\u00ba^\2\u049a\u049b\5`\61\2\u049b_\3\2\2\2\u049c")
        buf.write(u"\u049d\6\61\"\3\u049da\3\2\2\2\u049e\u049f\b\62\1\2\u049f")
        buf.write(u"\u04a0\5\u0100\u0081\2\u04a0\u04a5\3\2\2\2\u04a1\u04a2")
        buf.write(u"\f\3\2\2\u04a2\u04a4\5d\63\2\u04a3\u04a1\3\2\2\2\u04a4")
        buf.write(u"\u04a7\3\2\2\2\u04a5\u04a3\3\2\2\2\u04a5\u04a6\3\2\2")
        buf.write(u"\2\u04a6c\3\2\2\2\u04a7\u04a5\3\2\2\2\u04a8\u04a9\6\63")
        buf.write(u"$\3\u04a9\u04aa\7\25\2\2\u04aa\u04b6\5\u00ba^\2\u04ab")
        buf.write(u"\u04ac\6\63%\3\u04ac\u04ad\7\30\2\2\u04ad\u04ae\5\u0114")
        buf.write(u"\u008b\2\u04ae\u04af\7\31\2\2\u04af\u04b6\3\2\2\2\u04b0")
        buf.write(u"\u04b1\6\63&\3\u04b1\u04b2\7\30\2\2\u04b2\u04b3\5X-\2")
        buf.write(u"\u04b3\u04b4\7\31\2\2\u04b4\u04b6\3\2\2\2\u04b5\u04a8")
        buf.write(u"\3\2\2\2\u04b5\u04ab\3\2\2\2\u04b5\u04b0\3\2\2\2\u04b6")
        buf.write(u"e\3\2\2\2\u04b7\u04ba\7?\2\2\u04b8\u04b9\7l\2\2\u04b9")
        buf.write(u"\u04bb\5X-\2\u04ba\u04b8\3\2\2\2\u04ba\u04bb\3\2\2\2")
        buf.write(u"\u04bbg\3\2\2\2\u04bc\u04bd\7@\2\2\u04bd\u04be\7l\2\2")
        buf.write(u"\u04be\u04bf\5X-\2\u04bfi\3\2\2\2\u04c0\u04c1\5\u00ae")
        buf.write(u"X\2\u04c1\u04c2\7l\2\2\u04c2\u04cb\5X-\2\u04c3\u04c5")
        buf.write(u"\7\23\2\2\u04c4\u04c3\3\2\2\2\u04c4\u04c5\3\2\2\2\u04c5")
        buf.write(u"\u04c6\3\2\2\2\u04c6\u04c9\5x=\2\u04c7\u04c8\7H\2\2\u04c8")
        buf.write(u"\u04ca\5z>\2\u04c9\u04c7\3\2\2\2\u04c9\u04ca\3\2\2\2")
        buf.write(u"\u04ca\u04cc\3\2\2\2\u04cb\u04c4\3\2\2\2\u04cb\u04cc")
        buf.write(u"\3\2\2\2\u04cc\u04d6\3\2\2\2\u04cd\u04d3\5\u00aeX\2\u04ce")
        buf.write(u"\u04d1\5x=\2\u04cf\u04d0\7H\2\2\u04d0\u04d2\5z>\2\u04d1")
        buf.write(u"\u04cf\3\2\2\2\u04d1\u04d2\3\2\2\2\u04d2\u04d4\3\2\2")
        buf.write(u"\2\u04d3\u04ce\3\2\2\2\u04d3\u04d4\3\2\2\2\u04d4\u04d6")
        buf.write(u"\3\2\2\2\u04d5\u04c0\3\2\2\2\u04d5\u04cd\3\2\2\2\u04d6")
        buf.write(u"k\3\2\2\2\u04d7\u04d8\7\u009d\2\2\u04d8\u04d9\5X-\2\u04d9")
        buf.write(u"\u04da\7\u0096\2\2\u04da\u04db\5X-\2\u04dbm\3\2\2\2\u04dc")
        buf.write(u"\u04dd\5Z.\2\u04dd\u04de\7#\2\2\u04de\u04df\5X-\2\u04df")
        buf.write(u"o\3\2\2\2\u04e0\u04e1\7h\2\2\u04e1\u04e2\7\u0099\2\2")
        buf.write(u"\u04e2\u04e3\5\u00ba^\2\u04e3\u04e4\7\u009b\2\2\u04e4")
        buf.write(u"\u04e5\5X-\2\u04e5q\3\2\2\2\u04e6\u04e7\7g\2\2\u04e7")
        buf.write(u"\u04e9\7~\2\2\u04e8\u04ea\5\u00aeX\2\u04e9\u04e8\3\2")
        buf.write(u"\2\2\u04e9\u04ea\3\2\2\2\u04ea\u04eb\3\2\2\2\u04eb\u04ec")
        buf.write(u"\7\u009b\2\2\u04ec\u050b\5X-\2\u04ed\u04ff\7g\2\2\u04ee")
        buf.write(u"\u04f0\7F\2\2\u04ef\u04f1\5\u00aeX\2\u04f0\u04ef\3\2")
        buf.write(u"\2\2\u04f0\u04f1\3\2\2\2\u04f1\u0500\3\2\2\2\u04f2\u04f4")
        buf.write(u"\5\u00aeX\2\u04f3\u04f5\7\u008b\2\2\u04f4\u04f3\3\2\2")
        buf.write(u"\2\u04f4\u04f5\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6\u04f7")
        buf.write(u"\5X-\2\u04f7\u04f8\7\u0096\2\2\u04f8\u04f9\5X-\2\u04f9")
        buf.write(u"\u0500\3\2\2\2\u04fa\u04fb\7\u008b\2\2\u04fb\u04fc\5")
        buf.write(u"X-\2\u04fc\u04fd\7\u0096\2\2\u04fd\u04fe\5X-\2\u04fe")
        buf.write(u"\u0500\3\2\2\2\u04ff\u04ee\3\2\2\2\u04ff\u04f2\3\2\2")
        buf.write(u"\2\u04ff\u04fa\3\2\2\2\u0500\u0503\3\2\2\2\u0501\u0502")
        buf.write(u"\7\u009b\2\2\u0502\u0504\5X-\2\u0503\u0501\3\2\2\2\u0503")
        buf.write(u"\u0504\3\2\2\2\u0504\u0508\3\2\2\2\u0505\u0506\7\u0082")
        buf.write(u"\2\2\u0506\u0507\7Q\2\2\u0507\u0509\5\u0120\u0091\2\u0508")
        buf.write(u"\u0505\3\2\2\2\u0508\u0509\3\2\2\2\u0509\u050b\3\2\2")
        buf.write(u"\2\u050a\u04e6\3\2\2\2\u050a\u04ed\3\2\2\2\u050bs\3\2")
        buf.write(u"\2\2\u050c\u050e\7\u008f\2\2\u050d\u050f\7\\\2\2\u050e")
        buf.write(u"\u050d\3\2\2\2\u050e\u050f\3\2\2\2\u050f\u0510\3\2\2")
        buf.write(u"\2\u0510\u0516\5b\62\2\u0511\u0512\7\u0099\2\2\u0512")
        buf.write(u"\u0513\5b\62\2\u0513\u0514\7J\2\2\u0514\u0515\5\u0128")
        buf.write(u"\u0095\2\u0515\u0517\3\2\2\2\u0516\u0511\3\2\2\2\u0516")
        buf.write(u"\u0517\3\2\2\2\u0517u\3\2\2\2\u0518\u0519\6<\'\3\u0519")
        buf.write(u"\u051f\5X-\2\u051a\u051d\5x=\2\u051b\u051c\7H\2\2\u051c")
        buf.write(u"\u051e\5z>\2\u051d\u051b\3\2\2\2\u051d\u051e\3\2\2\2")
        buf.write(u"\u051e\u0520\3\2\2\2\u051f\u051a\3\2\2\2\u051f\u0520")
        buf.write(u"\3\2\2\2\u0520\u0527\3\2\2\2\u0521\u0524\5x=\2\u0522")
        buf.write(u"\u0523\7H\2\2\u0523\u0525\5z>\2\u0524\u0522\3\2\2\2\u0524")
        buf.write(u"\u0525\3\2\2\2\u0525\u0527\3\2\2\2\u0526\u0518\3\2\2")
        buf.write(u"\2\u0526\u0521\3\2\2\2\u0527w\3\2\2\2\u0528\u0529\b=")
        buf.write(u"\1\2\u0529\u052a\7\u0099\2\2\u052a\u052b\5z>\2\u052b")
        buf.write(u"\u0531\3\2\2\2\u052c\u052d\f\3\2\2\u052d\u052e\7\23\2")
        buf.write(u"\2\u052e\u0530\5z>\2\u052f\u052c\3\2\2\2\u0530\u0533")
        buf.write(u"\3\2\2\2\u0531\u052f\3\2\2\2\u0531\u0532\3\2\2\2\u0532")
        buf.write(u"y\3\2\2\2\u0533\u0531\3\2\2\2\u0534\u0535\5X-\2\u0535")
        buf.write(u"\u0536\7J\2\2\u0536\u0537\5\u00ba^\2\u0537{\3\2\2\2\u0538")
        buf.write(u"\u0539\5\u0118\u008d\2\u0539\u053a\5\u0130\u0099\2\u053a")
        buf.write(u"\u053b\5X-\2\u053b}\3\2\2\2\u053c\u053d\6@)\3\u053d\u053e")
        buf.write(u"\7\25\2\2\u053e\u0545\5\u00ba^\2\u053f\u0540\6@*\3\u0540")
        buf.write(u"\u0541\7\30\2\2\u0541\u0542\5X-\2\u0542\u0543\7\31\2")
        buf.write(u"\2\u0543\u0545\3\2\2\2\u0544\u053c\3\2\2\2\u0544\u053f")
        buf.write(u"\3\2\2\2\u0545\177\3\2\2\2\u0546\u0547\5\u00e2r\2\u0547")
        buf.write(u"\u0548\5\u0130\u0099\2\u0548\u0549\5X-\2\u0549\u0081")
        buf.write(u"\3\2\2\2\u054a\u054c\7\7\2\2\u054b\u054a\3\2\2\2\u054c")
        buf.write(u"\u054f\3\2\2\2\u054d\u054b\3\2\2\2\u054d\u054e\3\2\2")
        buf.write(u"\2\u054e\u0083\3\2\2\2\u054f\u054d\3\2\2\2\u0550\u0552")
        buf.write(u"\7\7\2\2\u0551\u0550\3\2\2\2\u0552\u0553\3\2\2\2\u0553")
        buf.write(u"\u0551\3\2\2\2\u0553\u0554\3\2\2\2\u0554\u0085\3\2\2")
        buf.write(u"\2\u0555\u0557\7\7\2\2\u0556\u0555\3\2\2\2\u0557\u0558")
        buf.write(u"\3\2\2\2\u0558\u0556\3\2\2\2\u0558\u0559\3\2\2\2\u0559")
        buf.write(u"\u055a\3\2\2\2\u055a\u055b\7\3\2\2\u055b\u0087\3\2\2")
        buf.write(u"\2\u055c\u055e\7\7\2\2\u055d\u055c\3\2\2\2\u055e\u0561")
        buf.write(u"\3\2\2\2\u055f\u055d\3\2\2\2\u055f\u0560\3\2\2\2\u0560")
        buf.write(u"\u0562\3\2\2\2\u0561\u055f\3\2\2\2\u0562\u0563\7\4\2")
        buf.write(u"\2\u0563\u0089\3\2\2\2\u0564\u0565\7{\2\2\u0565\u008b")
        buf.write(u"\3\2\2\2\u0566\u0568\5\u008eH\2\u0567\u0566\3\2\2\2\u0567")
        buf.write(u"\u0568\3\2\2\2\u0568\u0569\3\2\2\2\u0569\u056a\5\u0082")
        buf.write(u"B\2\u056a\u056b\7\2\2\3\u056b\u008d\3\2\2\2\u056c\u0572")
        buf.write(u"\5\u0090I\2\u056d\u056e\5\u0084C\2\u056e\u056f\5\u0090")
        buf.write(u"I\2\u056f\u0571\3\2\2\2\u0570\u056d\3\2\2\2\u0571\u0574")
        buf.write(u"\3\2\2\2\u0572\u0570\3\2\2\2\u0572\u0573\3\2\2\2\u0573")
        buf.write(u"\u008f\3\2\2\2\u0574\u0572\3\2\2\2\u0575\u0576\5\u00e8")
        buf.write(u"u\2\u0576\u0577\5\u0084C\2\u0577\u0579\3\2\2\2\u0578")
        buf.write(u"\u0575\3\2\2\2\u0579\u057c\3\2\2\2\u057a\u0578\3\2\2")
        buf.write(u"\2\u057a\u057b\3\2\2\2\u057b\u0582\3\2\2\2\u057c\u057a")
        buf.write(u"\3\2\2\2\u057d\u0583\5\n\6\2\u057e\u0583\5\u00b2Z\2\u057f")
        buf.write(u"\u0583\5\u0092J\2\u0580\u0583\5\u0094K\2\u0581\u0583")
        buf.write(u"\5\u00e6t\2\u0582\u057d\3\2\2\2\u0582\u057e\3\2\2\2\u0582")
        buf.write(u"\u057f\3\2\2\2\u0582\u0580\3\2\2\2\u0582\u0581\3\2\2")
        buf.write(u"\2\u0583\u0091\3\2\2\2\u0584\u0585\5\36\20\2\u0585\u0093")
        buf.write(u"\3\2\2\2\u0586\u0589\5\2\2\2\u0587\u0589\5\4\3\2\u0588")
        buf.write(u"\u0586\3\2\2\2\u0588\u0587\3\2\2\2\u0589\u0095\3\2\2")
        buf.write(u"\2\u058a\u0590\5\6\4\2\u058b\u058c\5\u0084C\2\u058c\u058d")
        buf.write(u"\5\6\4\2\u058d\u058f\3\2\2\2\u058e\u058b\3\2\2\2\u058f")
        buf.write(u"\u0592\3\2\2\2\u0590\u058e\3\2\2\2\u0590\u0591\3\2\2")
        buf.write(u"\2\u0591\u0097\3\2\2\2\u0592\u0590\3\2\2\2\u0593\u0599")
        buf.write(u"\5\b\5\2\u0594\u0595\5\u0084C\2\u0595\u0596\5\b\5\2\u0596")
        buf.write(u"\u0598\3\2\2\2\u0597\u0594\3\2\2\2\u0598\u059b\3\2\2")
        buf.write(u"\2\u0599\u0597\3\2\2\2\u0599\u059a\3\2\2\2\u059a\u0099")
        buf.write(u"\3\2\2\2\u059b\u0599\3\2\2\2\u059c\u05a1\5\u00c0a\2\u059d")
        buf.write(u"\u059e\7\23\2\2\u059e\u05a0\5\u00c0a\2\u059f\u059d\3")
        buf.write(u"\2\2\2\u05a0\u05a3\3\2\2\2\u05a1\u059f\3\2\2\2\u05a1")
        buf.write(u"\u05a2\3\2\2\2\u05a2\u009b\3\2\2\2\u05a3\u05a1\3\2\2")
        buf.write(u"\2\u05a4\u05a5\7o\2\2\u05a5\u05af\5\u009eP\2\u05a6\u05a7")
        buf.write(u"\7o\2\2\u05a7\u05af\5\u00a0Q\2\u05a8\u05a9\7o\2\2\u05a9")
        buf.write(u"\u05af\5\u00a4S\2\u05aa\u05ab\7s\2\2\u05ab\u05af\7\u00a7")
        buf.write(u"\2\2\u05ac\u05ad\7s\2\2\u05ad\u05af\5X-\2\u05ae\u05a4")
        buf.write(u"\3\2\2\2\u05ae\u05a6\3\2\2\2\u05ae\u05a8\3\2\2\2\u05ae")
        buf.write(u"\u05aa\3\2\2\2\u05ae\u05ac\3\2\2\2\u05af\u009d\3\2\2")
        buf.write(u"\2\u05b0\u05b2\7w\2\2\u05b1\u05b0\3\2\2\2\u05b1\u05b2")
        buf.write(u"\3\2\2\2\u05b2\u05b3\3\2\2\2\u05b3\u05b5\7\30\2\2\u05b4")
        buf.write(u"\u05b6\5\u00a2R\2\u05b5\u05b4\3\2\2\2\u05b5\u05b6\3\2")
        buf.write(u"\2\2\u05b6\u05b7\3\2\2\2\u05b7\u05b8\7\31\2\2\u05b8\u009f")
        buf.write(u"\3\2\2\2\u05b9\u05bb\7w\2\2\u05ba\u05b9\3\2\2\2\u05ba")
        buf.write(u"\u05bb\3\2\2\2\u05bb\u05bc\3\2\2\2\u05bc\u05be\7*\2\2")
        buf.write(u"\u05bd\u05bf\5\u00a2R\2\u05be\u05bd\3\2\2\2\u05be\u05bf")
        buf.write(u"\3\2\2\2\u05bf\u05c0\3\2\2\2\u05c0\u05c1\7(\2\2\u05c1")
        buf.write(u"\u00a1\3\2\2\2\u05c2\u05c7\5X-\2\u05c3\u05c4\7\23\2\2")
        buf.write(u"\u05c4\u05c6\5X-\2\u05c5\u05c3\3\2\2\2\u05c6\u05c9\3")
        buf.write(u"\2\2\2\u05c7\u05c5\3\2\2\2\u05c7\u05c8\3\2\2\2\u05c8")
        buf.write(u"\u00a3\3\2\2\2\u05c9\u05c7\3\2\2\2\u05ca\u05cb\7\30\2")
        buf.write(u"\2\u05cb\u05cc\5X-\2\u05cc\u05cd\7\24\2\2\u05cd\u05ce")
        buf.write(u"\5X-\2\u05ce\u05cf\7\31\2\2\u05cf\u00a5\3\2\2\2\u05d0")
        buf.write(u"\u05d1\bT\1\2\u05d1\u05dd\5\u00a8U\2\u05d2\u05d3\7D\2")
        buf.write(u"\2\u05d3\u05d4\7*\2\2\u05d4\u05d5\5\u00a6T\2\u05d5\u05d6")
        buf.write(u"\7(\2\2\u05d6\u05dd\3\2\2\2\u05d7\u05d8\7C\2\2\u05d8")
        buf.write(u"\u05d9\7*\2\2\u05d9\u05da\5\u00a6T\2\u05da\u05db\7(\2")
        buf.write(u"\2\u05db\u05dd\3\2\2\2\u05dc\u05d0\3\2\2\2\u05dc\u05d2")
        buf.write(u"\3\2\2\2\u05dc\u05d7\3\2\2\2\u05dd\u05e8\3\2\2\2\u05de")
        buf.write(u"\u05df\f\7\2\2\u05df\u05e7\7,\2\2\u05e0\u05e1\f\6\2\2")
        buf.write(u"\u05e1\u05e2\7\30\2\2\u05e2\u05e7\7\31\2\2\u05e3\u05e4")
        buf.write(u"\f\5\2\2\u05e4\u05e5\7\32\2\2\u05e5\u05e7\7\33\2\2\u05e6")
        buf.write(u"\u05de\3\2\2\2\u05e6\u05e0\3\2\2\2\u05e6\u05e3\3\2\2")
        buf.write(u"\2\u05e7\u05ea\3\2\2\2\u05e8\u05e6\3\2\2\2\u05e8\u05e9")
        buf.write(u"\3\2\2\2\u05e9\u00a7\3\2\2\2\u05ea\u05e8\3\2\2\2\u05eb")
        buf.write(u"\u05ee\5\u00aaV\2\u05ec\u05ee\5\u00acW\2\u05ed\u05eb")
        buf.write(u"\3\2\2\2\u05ed\u05ec\3\2\2\2\u05ee\u00a9\3\2\2\2\u05ef")
        buf.write(u"\u05fe\7\64\2\2\u05f0\u05fe\7\65\2\2\u05f1\u05fe\7\66")
        buf.write(u"\2\2\u05f2\u05fe\7A\2\2\u05f3\u05fe\7\67\2\2\u05f4\u05fe")
        buf.write(u"\78\2\2\u05f5\u05fe\7?\2\2\u05f6\u05fe\79\2\2\u05f7\u05fe")
        buf.write(u"\7;\2\2\u05f8\u05fe\7:\2\2\u05f9\u05fe\7<\2\2\u05fa\u05fe")
        buf.write(u"\7>\2\2\u05fb\u05fe\7@\2\2\u05fc\u05fe\7B\2\2\u05fd\u05ef")
        buf.write(u"\3\2\2\2\u05fd\u05f0\3\2\2\2\u05fd\u05f1\3\2\2\2\u05fd")
        buf.write(u"\u05f2\3\2\2\2\u05fd\u05f3\3\2\2\2\u05fd\u05f4\3\2\2")
        buf.write(u"\2\u05fd\u05f5\3\2\2\2\u05fd\u05f6\3\2\2\2\u05fd\u05f7")
        buf.write(u"\3\2\2\2\u05fd\u05f8\3\2\2\2\u05fd\u05f9\3\2\2\2\u05fd")
        buf.write(u"\u05fa\3\2\2\2\u05fd\u05fb\3\2\2\2\u05fd\u05fc\3\2\2")
        buf.write(u"\2\u05fe\u00ab\3\2\2\2\u05ff\u0600\7\u00a3\2\2\u0600")
        buf.write(u"\u00ad\3\2\2\2\u0601\u0603\7w\2\2\u0602\u0601\3\2\2\2")
        buf.write(u"\u0602\u0603\3\2\2\2\u0603\u0604\3\2\2\2\u0604\u0605")
        buf.write(u"\5\u00acW\2\u0605\u00af\3\2\2\2\u0606\u0607\7>\2\2\u0607")
        buf.write(u"\u00b1\3\2\2\2\u0608\u060c\5\f\7\2\u0609\u060c\5\34\17")
        buf.write(u"\2\u060a\u060c\5\16\b\2\u060b\u0608\3\2\2\2\u060b\u0609")
        buf.write(u"\3\2\2\2\u060b\u060a\3\2\2\2\u060c\u00b3\3\2\2\2\u060d")
        buf.write(u"\u0612\5\u00be`\2\u060e\u060f\7\23\2\2\u060f\u0611\5")
        buf.write(u"\u00be`\2\u0610\u060e\3\2\2\2\u0611\u0614\3\2\2\2\u0612")
        buf.write(u"\u0610\3\2\2\2\u0612\u0613\3\2\2\2\u0613\u00b5\3\2\2")
        buf.write(u"\2\u0614\u0612\3\2\2\2\u0615\u0618\5\u00ba^\2\u0616\u0618")
        buf.write(u"\5\u00be`\2\u0617\u0615\3\2\2\2\u0617\u0616\3\2\2\2\u0618")
        buf.write(u"\u00b7\3\2\2\2\u0619\u061d\5\u00ba^\2\u061a\u061d\5\u00be")
        buf.write(u"`\2\u061b\u061d\5\u00c0a\2\u061c\u0619\3\2\2\2\u061c")
        buf.write(u"\u061a\3\2\2\2\u061c\u061b\3\2\2\2\u061d\u00b9\3\2\2")
        buf.write(u"\2\u061e\u061f\7\u00a4\2\2\u061f\u00bb\3\2\2\2\u0620")
        buf.write(u"\u0621\t\3\2\2\u0621\u00bd\3\2\2\2\u0622\u0623\7\u00a3")
        buf.write(u"\2\2\u0623\u00bf\3\2\2\2\u0624\u0625\7\u00a2\2\2\u0625")
        buf.write(u"\u00c1\3\2\2\2\u0626\u062b\5\u00c4c\2\u0627\u0628\7\23")
        buf.write(u"\2\2\u0628\u062a\5\u00c4c\2\u0629\u0627\3\2\2\2\u062a")
        buf.write(u"\u062d\3\2\2\2\u062b\u0629\3\2\2\2\u062b\u062c\3\2\2")
        buf.write(u"\2\u062c\u00c3\3\2\2\2\u062d\u062b\3\2\2\2\u062e\u0634")
        buf.write(u"\5\u00caf\2\u062f\u0631\7w\2\2\u0630\u062f\3\2\2\2\u0630")
        buf.write(u"\u0631\3\2\2\2\u0631\u0632\3\2\2\2\u0632\u0634\5\u00c6")
        buf.write(u"d\2\u0633\u062e\3\2\2\2\u0633\u0630\3\2\2\2\u0634\u00c5")
        buf.write(u"\3\2\2\2\u0635\u0638\5\u00c8e\2\u0636\u0638\5\62\32\2")
        buf.write(u"\u0637\u0635\3\2\2\2\u0637\u0636\3\2\2\2\u0638\u00c7")
        buf.write(u"\3\2\2\2\u0639\u063c\5\u00ba^\2\u063a\u063b\7-\2\2\u063b")
        buf.write(u"\u063d\5\u0106\u0084\2\u063c\u063a\3\2\2\2\u063c\u063d")
        buf.write(u"\3\2\2\2\u063d\u00c9\3\2\2\2\u063e\u063f\5\u00b0Y\2\u063f")
        buf.write(u"\u0640\5\u00ba^\2\u0640\u00cb\3\2\2\2\u0641\u0644\5\u00a6")
        buf.write(u"T\2\u0642\u0644\5\u00ceh\2\u0643\u0641\3\2\2\2\u0643")
        buf.write(u"\u0642\3\2\2\2\u0644\u00cd\3\2\2\2\u0645\u0646\bh\1\2")
        buf.write(u"\u0646\u0647\7I\2\2\u0647\u0650\3\2\2\2\u0648\u0649\f")
        buf.write(u"\4\2\2\u0649\u064a\7\30\2\2\u064a\u064f\7\31\2\2\u064b")
        buf.write(u"\u064c\f\3\2\2\u064c\u064d\7\32\2\2\u064d\u064f\7\33")
        buf.write(u"\2\2\u064e\u0648\3\2\2\2\u064e\u064b\3\2\2\2\u064f\u0652")
        buf.write(u"\3\2\2\2\u0650\u064e\3\2\2\2\u0650\u0651\3\2\2\2\u0651")
        buf.write(u"\u00cf\3\2\2\2\u0652\u0650\3\2\2\2\u0653\u0659\5\u00d2")
        buf.write(u"j\2\u0654\u0655\5\u0084C\2\u0655\u0656\5\u00d2j\2\u0656")
        buf.write(u"\u0658\3\2\2\2\u0657\u0654\3\2\2\2\u0658\u065b\3\2\2")
        buf.write(u"\2\u0659\u0657\3\2\2\2\u0659\u065a\3\2\2\2\u065a\u00d1")
        buf.write(u"\3\2\2\2\u065b\u0659\3\2\2\2\u065c\u0662\5\24\13\2\u065d")
        buf.write(u"\u0662\5\30\r\2\u065e\u0662\5(\25\2\u065f\u0662\5&\24")
        buf.write(u"\2\u0660\u0662\5\22\n\2\u0661\u065c\3\2\2\2\u0661\u065d")
        buf.write(u"\3\2\2\2\u0661\u065e\3\2\2\2\u0661\u065f\3\2\2\2\u0661")
        buf.write(u"\u0660\3\2\2\2\u0662\u00d3\3\2\2\2\u0663\u0669\5\u00d6")
        buf.write(u"l\2\u0664\u0665\5\u0084C\2\u0665\u0666\5\u00d6l\2\u0666")
        buf.write(u"\u0668\3\2\2\2\u0667\u0664\3\2\2\2\u0668\u066b\3\2\2")
        buf.write(u"\2\u0669\u0667\3\2\2\2\u0669\u066a\3\2\2\2\u066a\u00d5")
        buf.write(u"\3\2\2\2\u066b\u0669\3\2\2\2\u066c\u0670\5\32\16\2\u066d")
        buf.write(u"\u0670\5\26\f\2\u066e\u0670\5*\26\2\u066f\u066c\3\2\2")
        buf.write(u"\2\u066f\u066d\3\2\2\2\u066f\u066e\3\2\2\2\u0670\u00d7")
        buf.write(u"\3\2\2\2\u0671\u0672\7\13\2\2\u0672\u067c\5\u0182\u00c2")
        buf.write(u"\2\u0673\u0674\7\f\2\2\u0674\u067c\5\u019c\u00cf\2\u0675")
        buf.write(u"\u0676\7\r\2\2\u0676\u067c\5\u00dan\2\u0677\u0678\7\16")
        buf.write(u"\2\2\u0678\u067c\5\u00dan\2\u0679\u067a\7\17\2\2\u067a")
        buf.write(u"\u067c\5\u00dep\2\u067b\u0671\3\2\2\2\u067b\u0673\3\2")
        buf.write(u"\2\2\u067b\u0675\3\2\2\2\u067b\u0677\3\2\2\2\u067b\u0679")
        buf.write(u"\3\2\2\2\u067c\u00d9\3\2\2\2\u067d\u067f\5\u00b8]\2\u067e")
        buf.write(u"\u0680\5\u00dco\2\u067f\u067e\3\2\2\2\u067f\u0680\3\2")
        buf.write(u"\2\2\u0680\u00db\3\2\2\2\u0681\u0682\7l\2\2\u0682\u0683")
        buf.write(u"\5\u012a\u0096\2\u0683\u0684\7\21\2\2\u0684\u0689\5\u00b8")
        buf.write(u"]\2\u0685\u0686\7\25\2\2\u0686\u0688\5\u00b8]\2\u0687")
        buf.write(u"\u0685\3\2\2\2\u0688\u068b\3\2\2\2\u0689\u0687\3\2\2")
        buf.write(u"\2\u0689\u068a\3\2\2\2\u068a\u00dd\3\2\2\2\u068b\u0689")
        buf.write(u"\3\2\2\2\u068c\u068e\5\u00b8]\2\u068d\u068f\5\u00e0q")
        buf.write(u"\2\u068e\u068d\3\2\2\2\u068e\u068f\3\2\2\2\u068f\u00df")
        buf.write(u"\3\2\2\2\u0690\u0691\7l\2\2\u0691\u0692\5\u012a\u0096")
        buf.write(u"\2\u0692\u0694\7\21\2\2\u0693\u0695\7%\2\2\u0694\u0693")
        buf.write(u"\3\2\2\2\u0694\u0695\3\2\2\2\u0695\u0696\3\2\2\2\u0696")
        buf.write(u"\u069b\5\u0152\u00aa\2\u0697\u0698\7%\2\2\u0698\u069a")
        buf.write(u"\5\u0152\u00aa\2\u0699\u0697\3\2\2\2\u069a\u069d\3\2")
        buf.write(u"\2\2\u069b\u0699\3\2\2\2\u069b\u069c\3\2\2\2\u069c\u06a0")
        buf.write(u"\3\2\2\2\u069d\u069b\3\2\2\2\u069e\u069f\7\25\2\2\u069f")
        buf.write(u"\u06a1\5\u0152\u00aa\2\u06a0\u069e\3\2\2\2\u06a0\u06a1")
        buf.write(u"\3\2\2\2\u06a1\u00e1\3\2\2\2\u06a2\u06a7\5\u00ba^\2\u06a3")
        buf.write(u"\u06a4\7\23\2\2\u06a4\u06a6\5\u00ba^\2\u06a5\u06a3\3")
        buf.write(u"\2\2\2\u06a6\u06a9\3\2\2\2\u06a7\u06a5\3\2\2\2\u06a7")
        buf.write(u"\u06a8\3\2\2\2\u06a8\u00e3\3\2\2\2\u06a9\u06a7\3\2\2")
        buf.write(u"\2\u06aa\u06af\5\u00bc_\2\u06ab\u06ac\7\23\2\2\u06ac")
        buf.write(u"\u06ae\5\u00bc_\2\u06ad\u06ab\3\2\2\2\u06ae\u06b1\3\2")
        buf.write(u"\2\2\u06af\u06ad\3\2\2\2\u06af\u06b0\3\2\2\2\u06b0\u00e5")
        buf.write(u"\3\2\2\2\u06b1\u06af\3\2\2\2\u06b2\u06b7\5&\24\2\u06b3")
        buf.write(u"\u06b7\5(\25\2\u06b4\u06b7\5*\26\2\u06b5\u06b7\5,\27")
        buf.write(u"\2\u06b6\u06b2\3\2\2\2\u06b6\u06b3\3\2\2\2\u06b6\u06b4")
        buf.write(u"\3\2\2\2\u06b6\u06b5\3\2\2\2\u06b7\u00e7\3\2\2\2\u06b8")
        buf.write(u"\u06b9\7\n\2\2\u06b9\u00e9\3\2\2\2\u06ba\u06c0\5\u00ec")
        buf.write(u"w\2\u06bb\u06bc\5\u0084C\2\u06bc\u06bd\5\u00ecw\2\u06bd")
        buf.write(u"\u06bf\3\2\2\2\u06be\u06bb\3\2\2\2\u06bf\u06c2\3\2\2")
        buf.write(u"\2\u06c0\u06be\3\2\2\2\u06c0\u06c1\3\2\2\2\u06c1\u00eb")
        buf.write(u"\3\2\2\2\u06c2\u06c0\3\2\2\2\u06c3\u06c4\7\13\2\2\u06c4")
        buf.write(u"\u06ce\5\u016c\u00b7\2\u06c5\u06c6\7\f\2\2\u06c6\u06ce")
        buf.write(u"\5\u0188\u00c5\2\u06c7\u06c8\7\r\2\2\u06c8\u06ce\5\u00ee")
        buf.write(u"x\2\u06c9\u06ca\7\16\2\2\u06ca\u06ce\5\u00eex\2\u06cb")
        buf.write(u"\u06cc\7\17\2\2\u06cc\u06ce\5\u00f0y\2\u06cd\u06c3\3")
        buf.write(u"\2\2\2\u06cd\u06c5\3\2\2\2\u06cd\u06c7\3\2\2\2\u06cd")
        buf.write(u"\u06c9\3\2\2\2\u06cd\u06cb\3\2\2\2\u06ce\u00ed\3\2\2")
        buf.write(u"\2\u06cf\u06d1\5\u0154\u00ab\2\u06d0\u06d2\7\22\2\2\u06d1")
        buf.write(u"\u06d0\3\2\2\2\u06d1\u06d2\3\2\2\2\u06d2\u06d4\3\2\2")
        buf.write(u"\2\u06d3\u06d5\5\u00dco\2\u06d4\u06d3\3\2\2\2\u06d4\u06d5")
        buf.write(u"\3\2\2\2\u06d5\u00ef\3\2\2\2\u06d6\u06d8\5\u013a\u009e")
        buf.write(u"\2\u06d7\u06d9\7\22\2\2\u06d8\u06d7\3\2\2\2\u06d8\u06d9")
        buf.write(u"\3\2\2\2\u06d9\u06db\3\2\2\2\u06da\u06dc\5\u00e0q\2\u06db")
        buf.write(u"\u06da\3\2\2\2\u06db\u06dc\3\2\2\2\u06dc\u00f1\3\2\2")
        buf.write(u"\2\u06dd\u06e3\5\64\33\2\u06de\u06df\5\u0084C\2\u06df")
        buf.write(u"\u06e0\5\64\33\2\u06e0\u06e2\3\2\2\2\u06e1\u06de\3\2")
        buf.write(u"\2\2\u06e2\u06e5\3\2\2\2\u06e3\u06e1\3\2\2\2\u06e3\u06e4")
        buf.write(u"\3\2\2\2\u06e4\u00f3\3\2\2\2\u06e5\u06e3\3\2\2\2\u06e6")
        buf.write(u"\u06ec\5.\30\2\u06e7\u06e8\5\u0084C\2\u06e8\u06e9\5.")
        buf.write(u"\30\2\u06e9\u06eb\3\2\2\2\u06ea\u06e7\3\2\2\2\u06eb\u06ee")
        buf.write(u"\3\2\2\2\u06ec\u06ea\3\2\2\2\u06ec\u06ed\3\2\2\2\u06ed")
        buf.write(u"\u00f5\3\2\2\2\u06ee\u06ec\3\2\2\2\u06ef\u06f5\5B\"\2")
        buf.write(u"\u06f0\u06f1\5\u0084C\2\u06f1\u06f2\5B\"\2\u06f2\u06f4")
        buf.write(u"\3\2\2\2\u06f3\u06f0\3\2\2\2\u06f4\u06f7\3\2\2\2\u06f5")
        buf.write(u"\u06f3\3\2\2\2\u06f5\u06f6\3\2\2\2\u06f6\u00f7\3\2\2")
        buf.write(u"\2\u06f7\u06f5\3\2\2\2\u06f8\u06fe\5R*\2\u06f9\u06fa")
        buf.write(u"\5\u0084C\2\u06fa\u06fb\5R*\2\u06fb\u06fd\3\2\2\2\u06fc")
        buf.write(u"\u06f9\3\2\2\2\u06fd\u0700\3\2\2\2\u06fe\u06fc\3\2\2")
        buf.write(u"\2\u06fe\u06ff\3\2\2\2\u06ff\u00f9\3\2\2\2\u0700\u06fe")
        buf.write(u"\3\2\2\2\u0701\u0702\7\30\2\2\u0702\u0703\5\u00fc\177")
        buf.write(u"\2\u0703\u0704\7\24\2\2\u0704\u0705\5\u00fc\177\2\u0705")
        buf.write(u"\u0706\7\31\2\2\u0706\u0710\3\2\2\2\u0707\u0708\7\30")
        buf.write(u"\2\2\u0708\u0709\5\u00fe\u0080\2\u0709\u070a\7\31\2\2")
        buf.write(u"\u070a\u0710\3\2\2\2\u070b\u070c\7*\2\2\u070c\u070d\5")
        buf.write(u"\u00fe\u0080\2\u070d\u070e\7(\2\2\u070e\u0710\3\2\2\2")
        buf.write(u"\u070f\u0701\3\2\2\2\u070f\u0707\3\2\2\2\u070f\u070b")
        buf.write(u"\3\2\2\2\u0710\u00fb\3\2\2\2\u0711\u0720\7\u00a0\2\2")
        buf.write(u"\u0712\u0720\7\u00a1\2\2\u0713\u0720\7\u00a9\2\2\u0714")
        buf.write(u"\u0720\7\u00aa\2\2\u0715\u0720\7\u009f\2\2\u0716\u0720")
        buf.write(u"\7\u00ae\2\2\u0717\u0720\7\u00ad\2\2\u0718\u0720\7\u00a7")
        buf.write(u"\2\2\u0719\u0720\7\u00ab\2\2\u071a\u0720\7\u00ac\2\2")
        buf.write(u"\u071b\u0720\7\u009e\2\2\u071c\u0720\7\u00af\2\2\u071d")
        buf.write(u"\u0720\7\u00a8\2\2\u071e\u0720\5\u008aF\2\u071f\u0711")
        buf.write(u"\3\2\2\2\u071f\u0712\3\2\2\2\u071f\u0713\3\2\2\2\u071f")
        buf.write(u"\u0714\3\2\2\2\u071f\u0715\3\2\2\2\u071f\u0716\3\2\2")
        buf.write(u"\2\u071f\u0717\3\2\2\2\u071f\u0718\3\2\2\2\u071f\u0719")
        buf.write(u"\3\2\2\2\u071f\u071a\3\2\2\2\u071f\u071b\3\2\2\2\u071f")
        buf.write(u"\u071c\3\2\2\2\u071f\u071d\3\2\2\2\u071f\u071e\3\2\2")
        buf.write(u"\2\u0720\u00fd\3\2\2\2\u0721\u0726\5\u00fc\177\2\u0722")
        buf.write(u"\u0723\7\23\2\2\u0723\u0725\5\u00fc\177\2\u0724\u0722")
        buf.write(u"\3\2\2\2\u0725\u0728\3\2\2\2\u0726\u0724\3\2\2\2\u0726")
        buf.write(u"\u0727\3\2\2\2\u0727\u00ff\3\2\2\2\u0728\u0726\3\2\2")
        buf.write(u"\2\u0729\u072e\5\u0104\u0083\2\u072a\u072e\5\u0106\u0084")
        buf.write(u"\2\u072b\u072e\5\u00b8]\2\u072c\u072e\5\u0102\u0082\2")
        buf.write(u"\u072d\u0729\3\2\2\2\u072d\u072a\3\2\2\2\u072d\u072b")
        buf.write(u"\3\2\2\2\u072d\u072c\3\2\2\2\u072e\u0101\3\2\2\2\u072f")
        buf.write(u"\u0730\t\4\2\2\u0730\u0103\3\2\2\2\u0731\u0732\7\26\2")
        buf.write(u"\2\u0732\u0733\5X-\2\u0733\u0734\7\27\2\2\u0734\u0105")
        buf.write(u"\3\2\2\2\u0735\u0738\5\u00fc\177\2\u0736\u0738\5\u0108")
        buf.write(u"\u0085\2\u0737\u0735\3\2\2\2\u0737\u0736\3\2\2\2\u0738")
        buf.write(u"\u0107\3\2\2\2\u0739\u073f\5\u00a4S\2\u073a\u073f\5\u009e")
        buf.write(u"P\2\u073b\u073f\5\u00a0Q\2\u073c\u073f\5\u010c\u0087")
        buf.write(u"\2\u073d\u073f\5\u010a\u0086\2\u073e\u0739\3\2\2\2\u073e")
        buf.write(u"\u073a\3\2\2\2\u073e\u073b\3\2\2\2\u073e\u073c\3\2\2")
        buf.write(u"\2\u073e\u073d\3\2\2\2\u073f\u0109\3\2\2\2\u0740\u0742")
        buf.write(u"\7w\2\2\u0741\u0740\3\2\2\2\u0741\u0742\3\2\2\2\u0742")
        buf.write(u"\u0743\3\2\2\2\u0743\u0745\7\26\2\2\u0744\u0746\5\u010e")
        buf.write(u"\u0088\2\u0745\u0744\3\2\2\2\u0745\u0746\3\2\2\2\u0746")
        buf.write(u"\u0747\3\2\2\2\u0747\u0748\7\27\2\2\u0748\u010b\3\2\2")
        buf.write(u"\2\u0749\u074b\7w\2\2\u074a\u0749\3\2\2\2\u074a\u074b")
        buf.write(u"\3\2\2\2\u074b\u074c\3\2\2\2\u074c\u074e\7\32\2\2\u074d")
        buf.write(u"\u074f\5\u0110\u0089\2\u074e\u074d\3\2\2\2\u074e\u074f")
        buf.write(u"\3\2\2\2\u074f\u0750\3\2\2\2\u0750\u0751\7\33\2\2\u0751")
        buf.write(u"\u010d\3\2\2\2\u0752\u0753\5X-\2\u0753\u075c\7\23\2\2")
        buf.write(u"\u0754\u0759\5X-\2\u0755\u0756\7\23\2\2\u0756\u0758\5")
        buf.write(u"X-\2\u0757\u0755\3\2\2\2\u0758\u075b\3\2\2\2\u0759\u0757")
        buf.write(u"\3\2\2\2\u0759\u075a\3\2\2\2\u075a\u075d\3\2\2\2\u075b")
        buf.write(u"\u0759\3\2\2\2\u075c\u0754\3\2\2\2\u075c\u075d\3\2\2")
        buf.write(u"\2\u075d\u010f\3\2\2\2\u075e\u0763\5\u0112\u008a\2\u075f")
        buf.write(u"\u0760\7\23\2\2\u0760\u0762\5\u0112\u008a\2\u0761\u075f")
        buf.write(u"\3\2\2\2\u0762\u0765\3\2\2\2\u0763\u0761\3\2\2\2\u0763")
        buf.write(u"\u0764\3\2\2\2\u0764\u0111\3\2\2\2\u0765\u0763\3\2\2")
        buf.write(u"\2\u0766\u0767\5X-\2\u0767\u0768\7\21\2\2\u0768\u0769")
        buf.write(u"\5X-\2\u0769\u0113\3\2\2\2\u076a\u076b\5X-\2\u076b\u076c")
        buf.write(u"\7\21\2\2\u076c\u076d\5X-\2\u076d\u0774\3\2\2\2\u076e")
        buf.write(u"\u076f\5X-\2\u076f\u0770\7\21\2\2\u0770\u0774\3\2\2\2")
        buf.write(u"\u0771\u0772\7\21\2\2\u0772\u0774\5X-\2\u0773\u076a\3")
        buf.write(u"\2\2\2\u0773\u076e\3\2\2\2\u0773\u0771\3\2\2\2\u0774")
        buf.write(u"\u0115\3\2\2\2\u0775\u0776\5\u00ba^\2\u0776\u0777\5\u0130")
        buf.write(u"\u0099\2\u0777\u0778\5X-\2\u0778\u0117\3\2\2\2\u0779")
        buf.write(u"\u077a\b\u008d\1\2\u077a\u077b\5\u00ba^\2\u077b\u0780")
        buf.write(u"\3\2\2\2\u077c\u077d\f\3\2\2\u077d\u077f\5~@\2\u077e")
        buf.write(u"\u077c\3\2\2\2\u077f\u0782\3\2\2\2\u0780\u077e\3\2\2")
        buf.write(u"\2\u0780\u0781\3\2\2\2\u0781\u0119\3\2\2\2\u0782\u0780")
        buf.write(u"\3\2\2\2\u0783\u0784\6\u008e\61\3\u0784\u0785\7\u00a4")
        buf.write(u"\2\2\u0785\u0788\5\u00ccg\2\u0786\u0788\5X-\2\u0787\u0783")
        buf.write(u"\3\2\2\2\u0787\u0786\3\2\2\2\u0788\u011b\3\2\2\2\u0789")
        buf.write(u"\u078a\7\u0086\2\2\u078a\u078b\7F\2\2\u078b\u078c\7l")
        buf.write(u"\2\2\u078c\u078d\5X-\2\u078d\u011d\3\2\2\2\u078e\u078f")
        buf.write(u"\7\u0086\2\2\u078f\u0790\7~\2\2\u0790\u0791\7l\2\2\u0791")
        buf.write(u"\u0792\5X-\2\u0792\u011f\3\2\2\2\u0793\u0798\5\u0122")
        buf.write(u"\u0092\2\u0794\u0795\7\23\2\2\u0795\u0797\5\u0122\u0092")
        buf.write(u"\2\u0796\u0794\3\2\2\2\u0797\u079a\3\2\2\2\u0798\u0796")
        buf.write(u"\3\2\2\2\u0798\u0799\3\2\2\2\u0799\u0121\3\2\2\2\u079a")
        buf.write(u"\u0798\3\2\2\2\u079b\u07a0\5\u00ba^\2\u079c\u079d\7\25")
        buf.write(u"\2\2\u079d\u079f\5\u00ba^\2\u079e\u079c\3\2\2\2\u079f")
        buf.write(u"\u07a2\3\2\2\2\u07a0\u079e\3\2\2\2\u07a0\u07a1\3\2\2")
        buf.write(u"\2\u07a1\u07a4\3\2\2\2\u07a2\u07a0\3\2\2\2\u07a3\u07a5")
        buf.write(u"\t\5\2\2\u07a4\u07a3\3\2\2\2\u07a4\u07a5\3\2\2\2\u07a5")
        buf.write(u"\u0123\3\2\2\2\u07a6\u07ad\7\"\2\2\u07a7\u07ad\7#\2\2")
        buf.write(u"\u07a8\u07ad\5\u0132\u009a\2\u07a9\u07ad\5\u0134\u009b")
        buf.write(u"\2\u07aa\u07ad\5\u0136\u009c\2\u07ab\u07ad\5\u0138\u009d")
        buf.write(u"\2\u07ac\u07a6\3\2\2\2\u07ac\u07a7\3\2\2\2\u07ac\u07a8")
        buf.write(u"\3\2\2\2\u07ac\u07a9\3\2\2\2\u07ac\u07aa\3\2\2\2\u07ac")
        buf.write(u"\u07ab\3\2\2\2\u07ad\u0125\3\2\2\2\u07ae\u07af\7\u00a4")
        buf.write(u"\2\2\u07af\u07b0\6\u0094\62\3\u07b0\u0127\3\2\2\2\u07b1")
        buf.write(u"\u07b2\7\u00a4\2\2\u07b2\u07b3\6\u0095\63\3\u07b3\u0129")
        buf.write(u"\3\2\2\2\u07b4\u07b5\7\u00a4\2\2\u07b5\u07b6\6\u0096")
        buf.write(u"\64\3\u07b6\u012b\3\2\2\2\u07b7\u07b8\7\u00a4\2\2\u07b8")
        buf.write(u"\u07b9\6\u0097\65\3\u07b9\u012d\3\2\2\2\u07ba\u07bb\7")
        buf.write(u"\u00a4\2\2\u07bb\u07bc\6\u0098\66\3\u07bc\u012f\3\2\2")
        buf.write(u"\2\u07bd\u07be\7-\2\2\u07be\u0131\3\2\2\2\u07bf\u07c0")
        buf.write(u"\7$\2\2\u07c0\u0133\3\2\2\2\u07c1\u07c2\7%\2\2\u07c2")
        buf.write(u"\u0135\3\2\2\2\u07c3\u07c4\7&\2\2\u07c4\u0137\3\2\2\2")
        buf.write(u"\u07c5\u07c6\t\6\2\2\u07c6\u0139\3\2\2\2\u07c7\u07c8")
        buf.write(u"\7\u0089\2\2\u07c8\u07c9\5\u013c\u009f\2\u07c9\u07ca")
        buf.write(u"\7\22\2\2\u07ca\u07cf\3\2\2\2\u07cb\u07cc\5\u013c\u009f")
        buf.write(u"\2\u07cc\u07cd\7\22\2\2\u07cd\u07cf\3\2\2\2\u07ce\u07c7")
        buf.write(u"\3\2\2\2\u07ce\u07cb\3\2\2\2\u07cf\u013b\3\2\2\2\u07d0")
        buf.write(u"\u07d1\b\u009f\1\2\u07d1\u07d2\5\u013e\u00a0\2\u07d2")
        buf.write(u"\u07d7\3\2\2\2\u07d3\u07d4\f\3\2\2\u07d4\u07d6\5\u0144")
        buf.write(u"\u00a3\2\u07d5\u07d3\3\2\2\2\u07d6\u07d9\3\2\2\2\u07d7")
        buf.write(u"\u07d5\3\2\2\2\u07d7\u07d8\3\2\2\2\u07d8\u013d\3\2\2")
        buf.write(u"\2\u07d9\u07d7\3\2\2\2\u07da\u07e2\5\u0140\u00a1\2\u07db")
        buf.write(u"\u07e2\5\u0142\u00a2\2\u07dc\u07e2\5\u014c\u00a7\2\u07dd")
        buf.write(u"\u07e2\5\u014e\u00a8\2\u07de\u07e2\5\u0150\u00a9\2\u07df")
        buf.write(u"\u07e2\5\u0146\u00a4\2\u07e0\u07e2\5\u014a\u00a6\2\u07e1")
        buf.write(u"\u07da\3\2\2\2\u07e1\u07db\3\2\2\2\u07e1\u07dc\3\2\2")
        buf.write(u"\2\u07e1\u07dd\3\2\2\2\u07e1\u07de\3\2\2\2\u07e1\u07df")
        buf.write(u"\3\2\2\2\u07e1\u07e0\3\2\2\2\u07e2\u013f\3\2\2\2\u07e3")
        buf.write(u"\u07e4\5\u0102\u0082\2\u07e4\u0141\3\2\2\2\u07e5\u07e6")
        buf.write(u"\5\u0126\u0094\2\u07e6\u07e7\5\u0146\u00a4\2\u07e7\u0143")
        buf.write(u"\3\2\2\2\u07e8\u07e9\7\25\2\2\u07e9\u07ee\5\u0146\u00a4")
        buf.write(u"\2\u07ea\u07eb\7\25\2\2\u07eb\u07ee\5\u0152\u00aa\2\u07ec")
        buf.write(u"\u07ee\5\u014a\u00a6\2\u07ed\u07e8\3\2\2\2\u07ed\u07ea")
        buf.write(u"\3\2\2\2\u07ed\u07ec\3\2\2\2\u07ee\u0145\3\2\2\2\u07ef")
        buf.write(u"\u07f0\5\u0152\u00aa\2\u07f0\u07f2\7\26\2\2\u07f1\u07f3")
        buf.write(u"\5\u0148\u00a5\2\u07f2\u07f1\3\2\2\2\u07f2\u07f3\3\2")
        buf.write(u"\2\2\u07f3\u07f4\3\2\2\2\u07f4\u07f5\7\27\2\2\u07f5\u0147")
        buf.write(u"\3\2\2\2\u07f6\u07f7\b\u00a5\1\2\u07f7\u07f8\5\u013c")
        buf.write(u"\u009f\2\u07f8\u07fe\3\2\2\2\u07f9\u07fa\f\3\2\2\u07fa")
        buf.write(u"\u07fb\7\23\2\2\u07fb\u07fd\5\u013c\u009f\2\u07fc\u07f9")
        buf.write(u"\3\2\2\2\u07fd\u0800\3\2\2\2\u07fe\u07fc\3\2\2\2\u07fe")
        buf.write(u"\u07ff\3\2\2\2\u07ff\u0149\3\2\2\2\u0800\u07fe\3\2\2")
        buf.write(u"\2\u0801\u0802\7\30\2\2\u0802\u0803\5\u013c\u009f\2\u0803")
        buf.write(u"\u0804\7\31\2\2\u0804\u014b\3\2\2\2\u0805\u0806\7\26")
        buf.write(u"\2\2\u0806\u0807\5\u013c\u009f\2\u0807\u0808\7\27\2\2")
        buf.write(u"\u0808\u014d\3\2\2\2\u0809\u080a\5\u0152\u00aa\2\u080a")
        buf.write(u"\u014f\3\2\2\2\u080b\u0811\7\u00a9\2\2\u080c\u0811\7")
        buf.write(u"\u00ab\2\2\u080d\u0811\7\u00a7\2\2\u080e\u0811\7\u009e")
        buf.write(u"\2\2\u080f\u0811\7\u009f\2\2\u0810\u080b\3\2\2\2\u0810")
        buf.write(u"\u080c\3\2\2\2\u0810\u080d\3\2\2\2\u0810\u080e\3\2\2")
        buf.write(u"\2\u0810\u080f\3\2\2\2\u0811\u0151\3\2\2\2\u0812\u0813")
        buf.write(u"\t\7\2\2\u0813\u0153\3\2\2\2\u0814\u0815\7\u0089\2\2")
        buf.write(u"\u0815\u0818\5\u0156\u00ac\2\u0816\u0818\5\u0156\u00ac")
        buf.write(u"\2\u0817\u0814\3\2\2\2\u0817\u0816\3\2\2\2\u0818\u0155")
        buf.write(u"\3\2\2\2\u0819\u081a\b\u00ac\1\2\u081a\u081b\5\u0158")
        buf.write(u"\u00ad\2\u081b\u0820\3\2\2\2\u081c\u081d\f\3\2\2\u081d")
        buf.write(u"\u081f\5\u015a\u00ae\2\u081e\u081c\3\2\2\2\u081f\u0822")
        buf.write(u"\3\2\2\2\u0820\u081e\3\2\2\2\u0820\u0821\3\2\2\2\u0821")
        buf.write(u"\u0157\3\2\2\2\u0822\u0820\3\2\2\2\u0823\u0828\5\u0164")
        buf.write(u"\u00b3\2\u0824\u0828\5\u0166\u00b4\2\u0825\u0828\5\u0168")
        buf.write(u"\u00b5\2\u0826\u0828\5\u015c\u00af\2\u0827\u0823\3\2")
        buf.write(u"\2\2\u0827\u0824\3\2\2\2\u0827\u0825\3\2\2\2\u0827\u0826")
        buf.write(u"\3\2\2\2\u0828\u0159\3\2\2\2\u0829\u082a\7\25\2\2\u082a")
        buf.write(u"\u0830\5\u015c\u00af\2\u082b\u082c\7\30\2\2\u082c\u082d")
        buf.write(u"\5\u0156\u00ac\2\u082d\u082e\7\31\2\2\u082e\u0830\3\2")
        buf.write(u"\2\2\u082f\u0829\3\2\2\2\u082f\u082b\3\2\2\2\u0830\u015b")
        buf.write(u"\3\2\2\2\u0831\u0832\5\u016a\u00b6\2\u0832\u0834\7\26")
        buf.write(u"\2\2\u0833\u0835\5\u015e\u00b0\2\u0834\u0833\3\2\2\2")
        buf.write(u"\u0834\u0835\3\2\2\2\u0835\u0836\3\2\2\2\u0836\u0837")
        buf.write(u"\7\27\2\2\u0837\u015d\3\2\2\2\u0838\u083f\5\u0160\u00b1")
        buf.write(u"\2\u0839\u083f\5\u0162\u00b2\2\u083a\u083b\5\u0160\u00b1")
        buf.write(u"\2\u083b\u083c\7\23\2\2\u083c\u083d\5\u0162\u00b2\2\u083d")
        buf.write(u"\u083f\3\2\2\2\u083e\u0838\3\2\2\2\u083e\u0839\3\2\2")
        buf.write(u"\2\u083e\u083a\3\2\2\2\u083f\u015f\3\2\2\2\u0840\u0841")
        buf.write(u"\b\u00b1\1\2\u0841\u0842\5\u0156\u00ac\2\u0842\u0848")
        buf.write(u"\3\2\2\2\u0843\u0844\f\3\2\2\u0844\u0845\7\23\2\2\u0845")
        buf.write(u"\u0847\5\u0156\u00ac\2\u0846\u0843\3\2\2\2\u0847\u084a")
        buf.write(u"\3\2\2\2\u0848\u0846\3\2\2\2\u0848\u0849\3\2\2\2\u0849")
        buf.write(u"\u0161\3\2\2\2\u084a\u0848\3\2\2\2\u084b\u084c\b\u00b2")
        buf.write(u"\1\2\u084c\u084d\5\u016a\u00b6\2\u084d\u084e\7-\2\2\u084e")
        buf.write(u"\u084f\5\u0156\u00ac\2\u084f\u0858\3\2\2\2\u0850\u0851")
        buf.write(u"\f\3\2\2\u0851\u0852\7\23\2\2\u0852\u0853\5\u016a\u00b6")
        buf.write(u"\2\u0853\u0854\7-\2\2\u0854\u0855\5\u0156\u00ac\2\u0855")
        buf.write(u"\u0857\3\2\2\2\u0856\u0850\3\2\2\2\u0857\u085a\3\2\2")
        buf.write(u"\2\u0858\u0856\3\2\2\2\u0858\u0859\3\2\2\2\u0859\u0163")
        buf.write(u"\3\2\2\2\u085a\u0858\3\2\2\2\u085b\u085c\7\26\2\2\u085c")
        buf.write(u"\u085d\5\u0156\u00ac\2\u085d\u085e\7\27\2\2\u085e\u0165")
        buf.write(u"\3\2\2\2\u085f\u0860\b\u00b4\1\2\u0860\u0863\7\u00a6")
        buf.write(u"\2\2\u0861\u0863\5\u016a\u00b6\2\u0862\u085f\3\2\2\2")
        buf.write(u"\u0862\u0861\3\2\2\2\u0863\u0869\3\2\2\2\u0864\u0865")
        buf.write(u"\f\3\2\2\u0865\u0866\7\25\2\2\u0866\u0868\5\u016a\u00b6")
        buf.write(u"\2\u0867\u0864\3\2\2\2\u0868\u086b\3\2\2\2\u0869\u0867")
        buf.write(u"\3\2\2\2\u0869\u086a\3\2\2\2\u086a\u0167\3\2\2\2\u086b")
        buf.write(u"\u0869\3\2\2\2\u086c\u0872\7\u00a9\2\2\u086d\u0872\7")
        buf.write(u"\u00ab\2\2\u086e\u0872\7\u00a7\2\2\u086f\u0872\7\u009e")
        buf.write(u"\2\2\u0870\u0872\7\u009f\2\2\u0871\u086c\3\2\2\2\u0871")
        buf.write(u"\u086d\3\2\2\2\u0871\u086e\3\2\2\2\u0871\u086f\3\2\2")
        buf.write(u"\2\u0871\u0870\3\2\2\2\u0872\u0169\3\2\2\2\u0873\u0874")
        buf.write(u"\t\b\2\2\u0874\u016b\3\2\2\2\u0875\u0876\7\u0089\2\2")
        buf.write(u"\u0876\u0877\5\u016e\u00b8\2\u0877\u0878\7\22\2\2\u0878")
        buf.write(u"\u087d\3\2\2\2\u0879\u087a\5\u016e\u00b8\2\u087a\u087b")
        buf.write(u"\7\22\2\2\u087b\u087d\3\2\2\2\u087c\u0875\3\2\2\2\u087c")
        buf.write(u"\u0879\3\2\2\2\u087d\u016d\3\2\2\2\u087e\u087f\b\u00b8")
        buf.write(u"\1\2\u087f\u0880\5\u0170\u00b9\2\u0880\u0885\3\2\2\2")
        buf.write(u"\u0881\u0882\f\3\2\2\u0882\u0884\5\u0176\u00bc\2\u0883")
        buf.write(u"\u0881\3\2\2\2\u0884\u0887\3\2\2\2\u0885\u0883\3\2\2")
        buf.write(u"\2\u0885\u0886\3\2\2\2\u0886\u016f\3\2\2\2\u0887\u0885")
        buf.write(u"\3\2\2\2\u0888\u088e\5\u0172\u00ba\2\u0889\u088e\5\u0174")
        buf.write(u"\u00bb\2\u088a\u088e\5\u017e\u00c0\2\u088b\u088e\5\u0180")
        buf.write(u"\u00c1\2\u088c\u088e\5\u0184\u00c3\2\u088d\u0888\3\2")
        buf.write(u"\2\2\u088d\u0889\3\2\2\2\u088d\u088a\3\2\2\2\u088d\u088b")
        buf.write(u"\3\2\2\2\u088d\u088c\3\2\2\2\u088e\u0171\3\2\2\2\u088f")
        buf.write(u"\u0890\5\u0102\u0082\2\u0890\u0173\3\2\2\2\u0891\u0892")
        buf.write(u"\5\u0126\u0094\2\u0892\u0893\5\u0178\u00bd\2\u0893\u0175")
        buf.write(u"\3\2\2\2\u0894\u0895\7\25\2\2\u0895\u0898\5\u0178\u00bd")
        buf.write(u"\2\u0896\u0898\5\u017c\u00bf\2\u0897\u0894\3\2\2\2\u0897")
        buf.write(u"\u0896\3\2\2\2\u0898\u0177\3\2\2\2\u0899\u089a\5\u0186")
        buf.write(u"\u00c4\2\u089a\u089c\7\26\2\2\u089b\u089d\5\u017a\u00be")
        buf.write(u"\2\u089c\u089b\3\2\2\2\u089c\u089d\3\2\2\2\u089d\u089e")
        buf.write(u"\3\2\2\2\u089e\u089f\7\27\2\2\u089f\u0179\3\2\2\2\u08a0")
        buf.write(u"\u08a1\b\u00be\1\2\u08a1\u08a2\5\u016e\u00b8\2\u08a2")
        buf.write(u"\u08a8\3\2\2\2\u08a3\u08a4\f\3\2\2\u08a4\u08a5\7\23\2")
        buf.write(u"\2\u08a5\u08a7\5\u016e\u00b8\2\u08a6\u08a3\3\2\2\2\u08a7")
        buf.write(u"\u08aa\3\2\2\2\u08a8\u08a6\3\2\2\2\u08a8\u08a9\3\2\2")
        buf.write(u"\2\u08a9\u017b\3\2\2\2\u08aa\u08a8\3\2\2\2\u08ab\u08ac")
        buf.write(u"\7\30\2\2\u08ac\u08ad\5\u016e\u00b8\2\u08ad\u08ae\7\31")
        buf.write(u"\2\2\u08ae\u017d\3\2\2\2\u08af\u08b0\7\26\2\2\u08b0\u08b1")
        buf.write(u"\5\u016e\u00b8\2\u08b1\u08b2\7\27\2\2\u08b2\u017f\3\2")
        buf.write(u"\2\2\u08b3\u08b4\b\u00c1\1\2\u08b4\u08b5\5\u0186\u00c4")
        buf.write(u"\2\u08b5\u08bb\3\2\2\2\u08b6\u08b7\f\3\2\2\u08b7\u08b8")
        buf.write(u"\7\25\2\2\u08b8\u08ba\5\u0186\u00c4\2\u08b9\u08b6\3\2")
        buf.write(u"\2\2\u08ba\u08bd\3\2\2\2\u08bb\u08b9\3\2\2\2\u08bb\u08bc")
        buf.write(u"\3\2\2\2\u08bc\u0181\3\2\2\2\u08bd\u08bb\3\2\2\2\u08be")
        buf.write(u"\u08bf\b\u00c2\1\2\u08bf\u08c0\5\u0180\u00c1\2\u08c0")
        buf.write(u"\u08c5\3\2\2\2\u08c1\u08c2\f\3\2\2\u08c2\u08c4\7\u00a6")
        buf.write(u"\2\2\u08c3\u08c1\3\2\2\2\u08c4\u08c7\3\2\2\2\u08c5\u08c3")
        buf.write(u"\3\2\2\2\u08c5\u08c6\3\2\2\2\u08c6\u0183\3\2\2\2\u08c7")
        buf.write(u"\u08c5\3\2\2\2\u08c8\u08ce\7\u00a9\2\2\u08c9\u08ce\7")
        buf.write(u"\u00ab\2\2\u08ca\u08ce\7\u00a7\2\2\u08cb\u08ce\7\u009e")
        buf.write(u"\2\2\u08cc\u08ce\7\u009f\2\2\u08cd\u08c8\3\2\2\2\u08cd")
        buf.write(u"\u08c9\3\2\2\2\u08cd\u08ca\3\2\2\2\u08cd\u08cb\3\2\2")
        buf.write(u"\2\u08cd\u08cc\3\2\2\2\u08ce\u0185\3\2\2\2\u08cf\u08d0")
        buf.write(u"\t\t\2\2\u08d0\u0187\3\2\2\2\u08d1\u08d2\7\u0089\2\2")
        buf.write(u"\u08d2\u08d3\5\u018a\u00c6\2\u08d3\u08d4\7\22\2\2\u08d4")
        buf.write(u"\u08d9\3\2\2\2\u08d5\u08d6\5\u018a\u00c6\2\u08d6\u08d7")
        buf.write(u"\7\22\2\2\u08d7\u08d9\3\2\2\2\u08d8\u08d1\3\2\2\2\u08d8")
        buf.write(u"\u08d5\3\2\2\2\u08d9\u0189\3\2\2\2\u08da\u08db\b\u00c6")
        buf.write(u"\1\2\u08db\u08dc\5\u018c\u00c7\2\u08dc\u08e1\3\2\2\2")
        buf.write(u"\u08dd\u08de\f\3\2\2\u08de\u08e0\5\u0192\u00ca\2\u08df")
        buf.write(u"\u08dd\3\2\2\2\u08e0\u08e3\3\2\2\2\u08e1\u08df\3\2\2")
        buf.write(u"\2\u08e1\u08e2\3\2\2\2\u08e2\u018b\3\2\2\2\u08e3\u08e1")
        buf.write(u"\3\2\2\2\u08e4\u08ea\5\u018e\u00c8\2\u08e5\u08ea\5\u0190")
        buf.write(u"\u00c9\2\u08e6\u08ea\5\u019a\u00ce\2\u08e7\u08ea\5\u019c")
        buf.write(u"\u00cf\2\u08e8\u08ea\5\u019e\u00d0\2\u08e9\u08e4\3\2")
        buf.write(u"\2\2\u08e9\u08e5\3\2\2\2\u08e9\u08e6\3\2\2\2\u08e9\u08e7")
        buf.write(u"\3\2\2\2\u08e9\u08e8\3\2\2\2\u08ea\u018d\3\2\2\2\u08eb")
        buf.write(u"\u08ec\5\u0102\u0082\2\u08ec\u018f\3\2\2\2\u08ed\u08ee")
        buf.write(u"\5\u0126\u0094\2\u08ee\u08ef\5\u0194\u00cb\2\u08ef\u0191")
        buf.write(u"\3\2\2\2\u08f0\u08f1\7\25\2\2\u08f1\u08f4\5\u0194\u00cb")
        buf.write(u"\2\u08f2\u08f4\5\u0198\u00cd\2\u08f3\u08f0\3\2\2\2\u08f3")
        buf.write(u"\u08f2\3\2\2\2\u08f4\u0193\3\2\2\2\u08f5\u08f6\5\u01a0")
        buf.write(u"\u00d1\2\u08f6\u08f8\7\26\2\2\u08f7\u08f9\5\u0196\u00cc")
        buf.write(u"\2\u08f8\u08f7\3\2\2\2\u08f8\u08f9\3\2\2\2\u08f9\u08fa")
        buf.write(u"\3\2\2\2\u08fa\u08fb\7\27\2\2\u08fb\u0195\3\2\2\2\u08fc")
        buf.write(u"\u08fd\b\u00cc\1\2\u08fd\u08fe\5\u018a\u00c6\2\u08fe")
        buf.write(u"\u0904\3\2\2\2\u08ff\u0900\f\3\2\2\u0900\u0901\7\23\2")
        buf.write(u"\2\u0901\u0903\5\u018a\u00c6\2\u0902\u08ff\3\2\2\2\u0903")
        buf.write(u"\u0906\3\2\2\2\u0904\u0902\3\2\2\2\u0904\u0905\3\2\2")
        buf.write(u"\2\u0905\u0197\3\2\2\2\u0906\u0904\3\2\2\2\u0907\u0908")
        buf.write(u"\7\30\2\2\u0908\u0909\5\u018a\u00c6\2\u0909\u090a\7\31")
        buf.write(u"\2\2\u090a\u0199\3\2\2\2\u090b\u090c\7\26\2\2\u090c\u090d")
        buf.write(u"\5\u018a\u00c6\2\u090d\u090e\7\27\2\2\u090e\u019b\3\2")
        buf.write(u"\2\2\u090f\u0910\b\u00cf\1\2\u0910\u0913\7\u00a6\2\2")
        buf.write(u"\u0911\u0913\5\u01a0\u00d1\2\u0912\u090f\3\2\2\2\u0912")
        buf.write(u"\u0911\3\2\2\2\u0913\u0919\3\2\2\2\u0914\u0915\f\3\2")
        buf.write(u"\2\u0915\u0916\7\25\2\2\u0916\u0918\5\u01a0\u00d1\2\u0917")
        buf.write(u"\u0914\3\2\2\2\u0918\u091b\3\2\2\2\u0919\u0917\3\2\2")
        buf.write(u"\2\u0919\u091a\3\2\2\2\u091a\u019d\3\2\2\2\u091b\u0919")
        buf.write(u"\3\2\2\2\u091c\u0922\7\u00a9\2\2\u091d\u0922\7\u00ab")
        buf.write(u"\2\2\u091e\u0922\7\u00a7\2\2\u091f\u0922\7\u009e\2\2")
        buf.write(u"\u0920\u0922\7\u009f\2\2\u0921\u091c\3\2\2\2\u0921\u091d")
        buf.write(u"\3\2\2\2\u0921\u091e\3\2\2\2\u0921\u091f\3\2\2\2\u0921")
        buf.write(u"\u0920\3\2\2\2\u0922\u019f\3\2\2\2\u0923\u0924\t\n\2")
        buf.write(u"\2\u0924\u01a1\3\2\2\2\u00c7\u01a8\u01af\u01cd\u01d3")
        buf.write(u"\u01d8\u01de\u01e0\u01e3\u01e9\u01ed\u01f8\u0201\u0210")
        buf.write(u"\u0219\u0220\u022a\u0240\u0257\u0264\u026f\u027d\u028b")
        buf.write(u"\u0299\u02ad\u02b8\u02ba\u02c3\u02c7\u02cf\u02d3\u02df")
        buf.write(u"\u02e4\u02e8\u0303\u030a\u030f\u0313\u0328\u0336\u033a")
        buf.write(u"\u033d\u035e\u0371\u0378\u039a\u03a3\u03ba\u03ca\u03cf")
        buf.write(u"\u03d7\u03e0\u03f7\u03fd\u041b\u0484\u0486\u0490\u04a5")
        buf.write(u"\u04b5\u04ba\u04c4\u04c9\u04cb\u04d1\u04d3\u04d5\u04e9")
        buf.write(u"\u04f0\u04f4\u04ff\u0503\u0508\u050a\u050e\u0516\u051d")
        buf.write(u"\u051f\u0524\u0526\u0531\u0544\u054d\u0553\u0558\u055f")
        buf.write(u"\u0567\u0572\u057a\u0582\u0588\u0590\u0599\u05a1\u05ae")
        buf.write(u"\u05b1\u05b5\u05ba\u05be\u05c7\u05dc\u05e6\u05e8\u05ed")
        buf.write(u"\u05fd\u0602\u060b\u0612\u0617\u061c\u062b\u0630\u0633")
        buf.write(u"\u0637\u063c\u0643\u064e\u0650\u0659\u0661\u0669\u066f")
        buf.write(u"\u067b\u067f\u0689\u068e\u0694\u069b\u06a0\u06a7\u06af")
        buf.write(u"\u06b6\u06c0\u06cd\u06d1\u06d4\u06d8\u06db\u06e3\u06ec")
        buf.write(u"\u06f5\u06fe\u070f\u071f\u0726\u072d\u0737\u073e\u0741")
        buf.write(u"\u0745\u074a\u074e\u0759\u075c\u0763\u0773\u0780\u0787")
        buf.write(u"\u0798\u07a0\u07a4\u07ac\u07ce\u07d7\u07e1\u07ed\u07f2")
        buf.write(u"\u07fe\u0810\u0817\u0820\u0827\u082f\u0834\u083e\u0848")
        buf.write(u"\u0858\u0862\u0869\u0871\u087c\u0885\u088d\u0897\u089c")
        buf.write(u"\u08a8\u08bb\u08c5\u08cd\u08d8\u08e1\u08e9\u08f3\u08f8")
        buf.write(u"\u0904\u0912\u0919\u0921")
        return buf.getvalue()
		

class EParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"<INVALID>", 
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
                     u"'Period'", u"'Method'", u"'Code'", u"'Document'", 
                     u"'Blob'", u"'Image'", u"'UUID'", u"'Iterator'", u"'Cursor'", 
                     u"'abstract'", u"'all'", u"'always'", u"'and'", u"'any'", 
                     u"'as'", u"<INVALID>", u"'attr'", u"'attribute'", u"'attributes'", 
                     u"'bindings'", u"'break'", u"'by'", u"'case'", u"'catch'", 
                     u"'category'", u"'class'", u"'close'", u"'contains'", 
                     u"'def'", u"'default'", u"'define'", u"'delete'", u"<INVALID>", 
                     u"'do'", u"'doing'", u"'each'", u"'else'", u"'enum'", 
                     u"'enumerated'", u"'except'", u"'execute'", u"'expecting'", 
                     u"'extends'", u"'fetch'", u"'filtered'", u"'finally'", 
                     u"'flush'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'index'", u"'invoke'", u"'is'", u"'matching'", 
                     u"'method'", u"'methods'", u"'modulo'", u"'mutable'", 
                     u"'native'", u"'None'", u"'not'", u"<INVALID>", u"'null'", 
                     u"'on'", u"'one'", u"'open'", u"'operator'", u"'or'", 
                     u"'order'", u"'otherwise'", u"'pass'", u"'raise'", 
                     u"'read'", u"'receiving'", u"'resource'", u"'return'", 
                     u"'returning'", u"'rows'", u"'self'", u"'setter'", 
                     u"'singleton'", u"'sorted'", u"'storable'", u"'store'", 
                     u"'switch'", u"'test'", u"'this'", u"'throw'", u"'to'", 
                     u"'try'", u"'verifying'", u"'with'", u"'when'", u"'where'", 
                     u"'while'", u"'write'", u"<INVALID>", u"<INVALID>", 
                     u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"INDENT", u"DEDENT", u"LF_TAB", u"LF_MORE", 
                      u"LF", u"TAB", u"WS", u"COMMENT", u"JAVA", u"CSHARP", 
                      u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", 
                      u"SEMI", u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", 
                      u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", u"QMARK", 
                      u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", 
                      u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", 
                      u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", u"ITERATOR", 
                      u"CURSOR", u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", 
                      u"ANY", u"AS", u"ASC", u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", 
                      u"BINDINGS", u"BREAK", u"BY", u"CASE", u"CATCH", u"CATEGORY", 
                      u"CLASS", u"CLOSE", u"CONTAINS", u"DEF", u"DEFAULT", 
                      u"DEFINE", u"DELETE", u"DESC", u"DO", u"DOING", u"EACH", 
                      u"ELSE", u"ENUM", u"ENUMERATED", u"EXCEPT", u"EXECUTE", 
                      u"EXPECTING", u"EXTENDS", u"FETCH", u"FILTERED", u"FINALLY", 
                      u"FLUSH", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INDEX", u"INVOKE", u"IS", u"MATCHING", u"METHOD", 
                      u"METHODS", u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", 
                      u"NOT", u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", 
                      u"OPERATOR", u"OR", u"ORDER", u"OTHERWISE", u"PASS", 
                      u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", u"RETURN", 
                      u"RETURNING", u"ROWS", u"SELF", u"SETTER", u"SINGLETON", 
                      u"SORTED", u"STORABLE", u"STORE", u"SWITCH", u"TEST", 
                      u"THIS", u"THROW", u"TO", u"TRY", u"VERIFYING", u"WITH", 
                      u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"UUID_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_concrete_category_declaration = 5
    RULE_singleton_category_declaration = 6
    RULE_derived_list = 7
    RULE_operator_method_declaration = 8
    RULE_setter_method_declaration = 9
    RULE_native_setter_declaration = 10
    RULE_getter_method_declaration = 11
    RULE_native_getter_declaration = 12
    RULE_native_category_declaration = 13
    RULE_native_resource_declaration = 14
    RULE_native_category_bindings = 15
    RULE_native_category_binding_list = 16
    RULE_attribute_list = 17
    RULE_abstract_method_declaration = 18
    RULE_concrete_method_declaration = 19
    RULE_native_method_declaration = 20
    RULE_test_method_declaration = 21
    RULE_assertion = 22
    RULE_full_argument_list = 23
    RULE_typed_argument = 24
    RULE_statement = 25
    RULE_flush_statement = 26
    RULE_store_statement = 27
    RULE_method_call_statement = 28
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
    RULE_expression = 43
    RULE_unresolved_expression = 44
    RULE_unresolved_selector = 45
    RULE_invocation_expression = 46
    RULE_invocation_trailer = 47
    RULE_instance_expression = 48
    RULE_instance_selector = 49
    RULE_document_expression = 50
    RULE_blob_expression = 51
    RULE_constructor_expression = 52
    RULE_write_statement = 53
    RULE_ambiguous_expression = 54
    RULE_filtered_list_suffix = 55
    RULE_fetch_store_expression = 56
    RULE_sorted_expression = 57
    RULE_argument_assignment_list = 58
    RULE_with_argument_assignment_list = 59
    RULE_argument_assignment = 60
    RULE_assign_instance_statement = 61
    RULE_child_instance = 62
    RULE_assign_tuple_statement = 63
    RULE_lfs = 64
    RULE_lfp = 65
    RULE_indent = 66
    RULE_dedent = 67
    RULE_null_literal = 68
    RULE_declaration_list = 69
    RULE_declarations = 70
    RULE_declaration = 71
    RULE_resource_declaration = 72
    RULE_enum_declaration = 73
    RULE_native_symbol_list = 74
    RULE_category_symbol_list = 75
    RULE_symbol_list = 76
    RULE_attribute_constraint = 77
    RULE_list_literal = 78
    RULE_set_literal = 79
    RULE_expression_list = 80
    RULE_range_literal = 81
    RULE_typedef = 82
    RULE_primary_type = 83
    RULE_native_type = 84
    RULE_category_type = 85
    RULE_mutable_category_type = 86
    RULE_code_type = 87
    RULE_category_declaration = 88
    RULE_type_identifier_list = 89
    RULE_method_identifier = 90
    RULE_identifier = 91
    RULE_variable_identifier = 92
    RULE_attribute_identifier = 93
    RULE_type_identifier = 94
    RULE_symbol_identifier = 95
    RULE_argument_list = 96
    RULE_argument = 97
    RULE_operator_argument = 98
    RULE_named_argument = 99
    RULE_code_argument = 100
    RULE_category_or_any_type = 101
    RULE_any_type = 102
    RULE_member_method_declaration_list = 103
    RULE_member_method_declaration = 104
    RULE_native_member_method_declaration_list = 105
    RULE_native_member_method_declaration = 106
    RULE_native_category_binding = 107
    RULE_python_category_binding = 108
    RULE_python_module = 109
    RULE_javascript_category_binding = 110
    RULE_javascript_module = 111
    RULE_variable_identifier_list = 112
    RULE_attribute_identifier_list = 113
    RULE_method_declaration = 114
    RULE_comment_statement = 115
    RULE_native_statement_list = 116
    RULE_native_statement = 117
    RULE_python_native_statement = 118
    RULE_javascript_native_statement = 119
    RULE_statement_list = 120
    RULE_assertion_list = 121
    RULE_switch_case_statement_list = 122
    RULE_catch_statement_list = 123
    RULE_literal_collection = 124
    RULE_atomic_literal = 125
    RULE_literal_list_literal = 126
    RULE_selectable_expression = 127
    RULE_this_expression = 128
    RULE_parenthesis_expression = 129
    RULE_literal_expression = 130
    RULE_collection_literal = 131
    RULE_tuple_literal = 132
    RULE_dict_literal = 133
    RULE_expression_tuple = 134
    RULE_dict_entry_list = 135
    RULE_dict_entry = 136
    RULE_slice_arguments = 137
    RULE_assign_variable_statement = 138
    RULE_assignable_instance = 139
    RULE_is_expression = 140
    RULE_read_all_expression = 141
    RULE_read_one_expression = 142
    RULE_order_by_list = 143
    RULE_order_by = 144
    RULE_operator = 145
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
    RULE_javascript_statement = 156
    RULE_javascript_expression = 157
    RULE_javascript_primary_expression = 158
    RULE_javascript_this_expression = 159
    RULE_javascript_new_expression = 160
    RULE_javascript_selector_expression = 161
    RULE_javascript_method_expression = 162
    RULE_javascript_arguments = 163
    RULE_javascript_item_expression = 164
    RULE_javascript_parenthesis_expression = 165
    RULE_javascript_identifier_expression = 166
    RULE_javascript_literal_expression = 167
    RULE_javascript_identifier = 168
    RULE_python_statement = 169
    RULE_python_expression = 170
    RULE_python_primary_expression = 171
    RULE_python_selector_expression = 172
    RULE_python_method_expression = 173
    RULE_python_argument_list = 174
    RULE_python_ordinal_argument_list = 175
    RULE_python_named_argument_list = 176
    RULE_python_parenthesis_expression = 177
    RULE_python_identifier_expression = 178
    RULE_python_literal_expression = 179
    RULE_python_identifier = 180
    RULE_java_statement = 181
    RULE_java_expression = 182
    RULE_java_primary_expression = 183
    RULE_java_this_expression = 184
    RULE_java_new_expression = 185
    RULE_java_selector_expression = 186
    RULE_java_method_expression = 187
    RULE_java_arguments = 188
    RULE_java_item_expression = 189
    RULE_java_parenthesis_expression = 190
    RULE_java_identifier_expression = 191
    RULE_java_class_identifier_expression = 192
    RULE_java_literal_expression = 193
    RULE_java_identifier = 194
    RULE_csharp_statement = 195
    RULE_csharp_expression = 196
    RULE_csharp_primary_expression = 197
    RULE_csharp_this_expression = 198
    RULE_csharp_new_expression = 199
    RULE_csharp_selector_expression = 200
    RULE_csharp_method_expression = 201
    RULE_csharp_arguments = 202
    RULE_csharp_item_expression = 203
    RULE_csharp_parenthesis_expression = 204
    RULE_csharp_identifier_expression = 205
    RULE_csharp_literal_expression = 206
    RULE_csharp_identifier = 207

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"full_argument_list", 
                   u"typed_argument", u"statement", u"flush_statement", 
                   u"store_statement", u"method_call_statement", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"break_statement", 
                   u"return_statement", u"expression", u"unresolved_expression", 
                   u"unresolved_selector", u"invocation_expression", u"invocation_trailer", 
                   u"instance_expression", u"instance_selector", u"document_expression", 
                   u"blob_expression", u"constructor_expression", u"write_statement", 
                   u"ambiguous_expression", u"filtered_list_suffix", u"fetch_store_expression", 
                   u"sorted_expression", u"argument_assignment_list", u"with_argument_assignment_list", 
                   u"argument_assignment", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"lfs", 
                   u"lfp", u"indent", u"dedent", u"null_literal", u"declaration_list", 
                   u"declarations", u"declaration", u"resource_declaration", 
                   u"enum_declaration", u"native_symbol_list", u"category_symbol_list", 
                   u"symbol_list", u"attribute_constraint", u"list_literal", 
                   u"set_literal", u"expression_list", u"range_literal", 
                   u"typedef", u"primary_type", u"native_type", u"category_type", 
                   u"mutable_category_type", u"code_type", u"category_declaration", 
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
                   u"order_by_list", u"order_by", u"operator", u"new_token", 
                   u"key_token", u"module_token", u"value_token", u"symbols_token", 
                   u"assign", u"multiply", u"divide", u"idivide", u"modulo", 
                   u"javascript_statement", u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_new_expression", 
                   u"javascript_selector_expression", u"javascript_method_expression", 
                   u"javascript_arguments", u"javascript_item_expression", 
                   u"javascript_parenthesis_expression", u"javascript_identifier_expression", 
                   u"javascript_literal_expression", u"javascript_identifier", 
                   u"python_statement", u"python_expression", u"python_primary_expression", 
                   u"python_selector_expression", u"python_method_expression", 
                   u"python_argument_list", u"python_ordinal_argument_list", 
                   u"python_named_argument_list", u"python_parenthesis_expression", 
                   u"python_identifier_expression", u"python_literal_expression", 
                   u"python_identifier", u"java_statement", u"java_expression", 
                   u"java_primary_expression", u"java_this_expression", 
                   u"java_new_expression", u"java_selector_expression", 
                   u"java_method_expression", u"java_arguments", u"java_item_expression", 
                   u"java_parenthesis_expression", u"java_identifier_expression", 
                   u"java_class_identifier_expression", u"java_literal_expression", 
                   u"java_identifier", u"csharp_statement", u"csharp_expression", 
                   u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_new_expression", u"csharp_selector_expression", 
                   u"csharp_method_expression", u"csharp_arguments", u"csharp_item_expression", 
                   u"csharp_parenthesis_expression", u"csharp_identifier_expression", 
                   u"csharp_literal_expression", u"csharp_identifier" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    LF_TAB=3
    LF_MORE=4
    LF=5
    TAB=6
    WS=7
    COMMENT=8
    JAVA=9
    CSHARP=10
    PYTHON2=11
    PYTHON3=12
    JAVASCRIPT=13
    SWIFT=14
    COLON=15
    SEMI=16
    COMMA=17
    RANGE=18
    DOT=19
    LPAR=20
    RPAR=21
    LBRAK=22
    RBRAK=23
    LCURL=24
    RCURL=25
    QMARK=26
    XMARK=27
    AMP=28
    AMP2=29
    PIPE=30
    PIPE2=31
    PLUS=32
    MINUS=33
    STAR=34
    SLASH=35
    BSLASH=36
    PERCENT=37
    GT=38
    GTE=39
    LT=40
    LTE=41
    LTGT=42
    EQ=43
    XEQ=44
    EQ2=45
    TEQ=46
    TILDE=47
    LARROW=48
    RARROW=49
    BOOLEAN=50
    CHARACTER=51
    TEXT=52
    INTEGER=53
    DECIMAL=54
    DATE=55
    TIME=56
    DATETIME=57
    PERIOD=58
    METHOD_T=59
    CODE=60
    DOCUMENT=61
    BLOB=62
    IMAGE=63
    UUID=64
    ITERATOR=65
    CURSOR=66
    ABSTRACT=67
    ALL=68
    ALWAYS=69
    AND=70
    ANY=71
    AS=72
    ASC=73
    ATTR=74
    ATTRIBUTE=75
    ATTRIBUTES=76
    BINDINGS=77
    BREAK=78
    BY=79
    CASE=80
    CATCH=81
    CATEGORY=82
    CLASS=83
    CLOSE=84
    CONTAINS=85
    DEF=86
    DEFAULT=87
    DEFINE=88
    DELETE=89
    DESC=90
    DO=91
    DOING=92
    EACH=93
    ELSE=94
    ENUM=95
    ENUMERATED=96
    EXCEPT=97
    EXECUTE=98
    EXPECTING=99
    EXTENDS=100
    FETCH=101
    FILTERED=102
    FINALLY=103
    FLUSH=104
    FOR=105
    FROM=106
    GETTER=107
    IF=108
    IN=109
    INDEX=110
    INVOKE=111
    IS=112
    MATCHING=113
    METHOD=114
    METHODS=115
    MODULO=116
    MUTABLE=117
    NATIVE=118
    NONE=119
    NOT=120
    NOTHING=121
    NULL=122
    ON=123
    ONE=124
    OPEN=125
    OPERATOR=126
    OR=127
    ORDER=128
    OTHERWISE=129
    PASS=130
    RAISE=131
    READ=132
    RECEIVING=133
    RESOURCE=134
    RETURN=135
    RETURNING=136
    ROWS=137
    SELF=138
    SETTER=139
    SINGLETON=140
    SORTED=141
    STORABLE=142
    STORE=143
    SWITCH=144
    TEST=145
    THIS=146
    THROW=147
    TO=148
    TRY=149
    VERIFYING=150
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

    def __init__(self, input):
        super(EParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.symbols = None # Category_symbol_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(EParser.Category_symbol_listContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = EParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(EParser.DEFINE)
            self.state = 417 
            localctx.name = self.type_identifier()
            self.state = 418
            self.match(EParser.AS)
            self.state = 419
            self.match(EParser.ENUMERATED)
            self.state = 422
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 420
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 421 
                localctx.derived = self.type_identifier()

            else:
                raise NoViableAltException(self)

            self.state = 429
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 424 
                localctx.attrs = self.attribute_list()
                self.state = 425
                self.match(EParser.COMMA)
                self.state = 426
                self.match(EParser.AND)
                pass

            elif la_ == 2:
                self.state = 428
                self.match(EParser.WITH)
                pass


            self.state = 431 
            self.symbols_token()
            self.state = 432
            self.match(EParser.COLON)
            self.state = 433 
            self.indent()
            self.state = 434 
            localctx.symbols = self.category_symbol_list()
            self.state = 435 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_native_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(EParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(EParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = EParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(EParser.DEFINE)
            self.state = 438 
            localctx.name = self.type_identifier()
            self.state = 439
            self.match(EParser.AS)
            self.state = 440
            self.match(EParser.ENUMERATED)
            self.state = 441 
            localctx.typ = self.native_type()
            self.state = 442
            self.match(EParser.WITH)
            self.state = 443 
            self.symbols_token()
            self.state = 444
            self.match(EParser.COLON)
            self.state = 445 
            self.indent()
            self.state = 446 
            localctx.symbols = self.native_symbol_list()
            self.state = 447 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def value_token(self):
            return self.getTypedRuleContext(EParser.Value_tokenContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_symbol

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = EParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449 
            localctx.name = self.symbol_identifier()
            self.state = 450
            self.match(EParser.WITH)
            self.state = 451 
            localctx.exp = self.expression(0)
            self.state = 452
            self.match(EParser.AS)
            self.state = 453 
            self.value_token()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_category_symbol

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = EParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455 
            localctx.name = self.symbol_identifier()
            self.state = 456 
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 459
            _la = self._input.LA(1)
            if _la==EParser.AND:
                self.state = 457
                self.match(EParser.AND)
                self.state = 458 
                localctx.arg = self.argument_assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Variable_identifier_listContext
            self.index = None # Variable_identifierContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)

        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def INDEX(self):
            return self.getToken(EParser.INDEX, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(EParser.Attribute_constraintContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = EParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(EParser.DEFINE)
            self.state = 462 
            localctx.name = self.attribute_identifier()
            self.state = 463
            self.match(EParser.AS)
            self.state = 465
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 464
                self.match(EParser.STORABLE)


            self.state = 467 
            localctx.typ = self.typedef(0)
            self.state = 468
            self.match(EParser.ATTRIBUTE)
            self.state = 470
            _la = self._input.LA(1)
            if _la==EParser.IN or _la==EParser.MATCHING:
                self.state = 469 
                localctx.match = self.attribute_constraint()


            self.state = 481
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 472
                self.match(EParser.WITH)
                self.state = 478
                _la = self._input.LA(1)
                if _la==EParser.VARIABLE_IDENTIFIER:
                    self.state = 473 
                    localctx.indices = self.variable_identifier_list()
                    self.state = 476
                    _la = self._input.LA(1)
                    if _la==EParser.AND:
                        self.state = 474
                        self.match(EParser.AND)
                        self.state = 475 
                        localctx.index = self.variable_identifier()




                self.state = 480
                self.match(EParser.INDEX)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(EParser.Derived_listContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = EParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(EParser.DEFINE)
            self.state = 484 
            localctx.name = self.type_identifier()
            self.state = 485
            self.match(EParser.AS)
            self.state = 487
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 486
                self.match(EParser.STORABLE)


            self.state = 491
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 489
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 490 
                localctx.derived = self.derived_list()

            else:
                raise NoViableAltException(self)

            self.state = 511
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 493 
                localctx.attrs = self.attribute_list()
                self.state = 502
                _la = self._input.LA(1)
                if _la==EParser.COMMA:
                    self.state = 494
                    self.match(EParser.COMMA)
                    self.state = 495
                    self.match(EParser.AND)
                    self.state = 496
                    self.match(EParser.METHODS)
                    self.state = 497
                    self.match(EParser.COLON)
                    self.state = 498 
                    self.indent()
                    self.state = 499 
                    localctx.methods = self.member_method_declaration_list()
                    self.state = 500 
                    self.dedent()



            elif la_ == 2:
                self.state = 504
                self.match(EParser.WITH)
                self.state = 505
                self.match(EParser.METHODS)
                self.state = 506
                self.match(EParser.COLON)
                self.state = 507 
                self.indent()
                self.state = 508 
                localctx.methods = self.member_method_declaration_list()
                self.state = 509 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Singleton_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SINGLETON(self):
            return self.getToken(EParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = EParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(EParser.DEFINE)
            self.state = 514 
            localctx.name = self.type_identifier()
            self.state = 515
            self.match(EParser.AS)
            self.state = 516
            self.match(EParser.SINGLETON)
            self.state = 535
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 517 
                localctx.attrs = self.attribute_list()
                self.state = 526
                _la = self._input.LA(1)
                if _la==EParser.COMMA:
                    self.state = 518
                    self.match(EParser.COMMA)
                    self.state = 519
                    self.match(EParser.AND)
                    self.state = 520
                    self.match(EParser.METHODS)
                    self.state = 521
                    self.match(EParser.COLON)
                    self.state = 522 
                    self.indent()
                    self.state = 523 
                    localctx.methods = self.member_method_declaration_list()
                    self.state = 524 
                    self.dedent()



            elif la_ == 2:
                self.state = 528
                self.match(EParser.WITH)
                self.state = 529
                self.match(EParser.METHODS)
                self.state = 530
                self.match(EParser.COLON)
                self.state = 531 
                self.indent()
                self.state = 532 
                localctx.methods = self.member_method_declaration_list()
                self.state = 533 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_derived_list

     
        def copyFrom(self, ctx):
            super(EParser.Derived_listContext, self).copyFrom(ctx)



    class DerivedListItemContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDerivedListItem(self)


    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Derived_listContext)
            super(EParser.DerivedListContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.copyFrom(ctx)

        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDerivedList(self)



    def derived_list(self):

        localctx = EParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.state = 542
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 537 
                localctx.items = self.type_identifier_list()
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 538 
                localctx.items = self.type_identifier_list()
                self.state = 539
                self.match(EParser.AND)
                self.state = 540 
                localctx.item = self.type_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def OPERATOR(self):
            return self.getToken(EParser.OPERATOR, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(EParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(EParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = EParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(EParser.DEFINE)
            self.state = 545 
            localctx.op = self.operator()
            self.state = 546
            self.match(EParser.AS)
            self.state = 547
            self.match(EParser.OPERATOR)
            self.state = 548
            self.match(EParser.RECEIVING)
            self.state = 549 
            localctx.arg = self.operator_argument()
            self.state = 552
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 550
                self.match(EParser.RETURNING)
                self.state = 551 
                localctx.typ = self.typedef(0)


            self.state = 554
            self.match(EParser.DOING)
            self.state = 555
            self.match(EParser.COLON)
            self.state = 556 
            self.indent()
            self.state = 557 
            localctx.stmts = self.statement_list()
            self.state = 558 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SETTER(self):
            return self.getToken(EParser.SETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = EParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(EParser.DEFINE)
            self.state = 561 
            localctx.name = self.variable_identifier()
            self.state = 562
            self.match(EParser.AS)
            self.state = 563
            self.match(EParser.SETTER)
            self.state = 564
            self.match(EParser.DOING)
            self.state = 565
            self.match(EParser.COLON)
            self.state = 566 
            self.indent()
            self.state = 567 
            localctx.stmts = self.statement_list()
            self.state = 568 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_setter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def SETTER(self):
            return self.getToken(EParser.SETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def getRuleIndex(self):
            return EParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = EParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(EParser.DEFINE)
            self.state = 571 
            localctx.name = self.variable_identifier()
            self.state = 572
            self.match(EParser.AS)
            self.state = 574
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 573
                self.match(EParser.NATIVE)


            self.state = 576
            self.match(EParser.SETTER)
            self.state = 577
            self.match(EParser.DOING)
            self.state = 578
            self.match(EParser.COLON)
            self.state = 579 
            self.indent()
            self.state = 580 
            localctx.stmts = self.native_statement_list()
            self.state = 581 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def GETTER(self):
            return self.getToken(EParser.GETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = EParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(EParser.DEFINE)
            self.state = 584 
            localctx.name = self.variable_identifier()
            self.state = 585
            self.match(EParser.AS)
            self.state = 586
            self.match(EParser.GETTER)
            self.state = 587
            self.match(EParser.DOING)
            self.state = 588
            self.match(EParser.COLON)
            self.state = 589 
            self.indent()
            self.state = 590 
            localctx.stmts = self.statement_list()
            self.state = 591 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_getter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def GETTER(self):
            return self.getToken(EParser.GETTER, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def getRuleIndex(self):
            return EParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = EParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(EParser.DEFINE)
            self.state = 594 
            localctx.name = self.variable_identifier()
            self.state = 595
            self.match(EParser.AS)
            self.state = 597
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 596
                self.match(EParser.NATIVE)


            self.state = 599
            self.match(EParser.GETTER)
            self.state = 600
            self.match(EParser.DOING)
            self.state = 601
            self.match(EParser.COLON)
            self.state = 602 
            self.indent()
            self.state = 603 
            localctx.stmts = self.native_statement_list()
            self.state = 604 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingsContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(EParser.AND)
            else:
                return self.getToken(EParser.AND, i)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = EParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(EParser.DEFINE)
            self.state = 607 
            localctx.name = self.type_identifier()
            self.state = 608
            self.match(EParser.AS)
            self.state = 610
            _la = self._input.LA(1)
            if _la==EParser.STORABLE:
                self.state = 609
                self.match(EParser.STORABLE)


            self.state = 612
            self.match(EParser.NATIVE)
            self.state = 613
            self.match(EParser.CATEGORY)
            self.state = 621
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 614 
                localctx.attrs = self.attribute_list()
                self.state = 615
                self.match(EParser.COMMA)
                self.state = 616
                self.match(EParser.AND)
                self.state = 617
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 619
                self.match(EParser.WITH)
                self.state = 620
                self.match(EParser.BINDINGS)
                pass


            self.state = 623
            self.match(EParser.COLON)
            self.state = 624 
            self.indent()
            self.state = 625 
            localctx.bindings = self.native_category_bindings()
            self.state = 626 
            self.dedent()
            self.state = 635
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 627 
                self.lfp()
                self.state = 628
                self.match(EParser.AND)
                self.state = 629
                self.match(EParser.METHODS)
                self.state = 630
                self.match(EParser.COLON)
                self.state = 631 
                self.indent()
                self.state = 632 
                localctx.methods = self.native_member_method_declaration_list()
                self.state = 633 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(EParser.RESOURCE, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingsContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(EParser.AND)
            else:
                return self.getToken(EParser.AND, i)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = EParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.match(EParser.DEFINE)
            self.state = 638 
            localctx.name = self.type_identifier()
            self.state = 639
            self.match(EParser.AS)
            self.state = 640
            self.match(EParser.NATIVE)
            self.state = 641
            self.match(EParser.RESOURCE)
            self.state = 649
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 642 
                localctx.attrs = self.attribute_list()
                self.state = 643
                self.match(EParser.COMMA)
                self.state = 644
                self.match(EParser.AND)
                self.state = 645
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 647
                self.match(EParser.WITH)
                self.state = 648
                self.match(EParser.BINDINGS)
                pass


            self.state = 651
            self.match(EParser.COLON)
            self.state = 652 
            self.indent()
            self.state = 653 
            localctx.bindings = self.native_category_bindings()
            self.state = 654 
            self.dedent()
            self.state = 663
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 655 
                self.lfp()
                self.state = 656
                self.match(EParser.AND)
                self.state = 657
                self.match(EParser.METHODS)
                self.state = 658
                self.match(EParser.COLON)
                self.state = 659 
                self.indent()
                self.state = 660 
                localctx.methods = self.native_member_method_declaration_list()
                self.state = 661 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def BINDINGS(self):
            return self.getToken(EParser.BINDINGS, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def native_category_binding_list(self):
            return self.getTypedRuleContext(EParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = EParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.match(EParser.DEFINE)
            self.state = 666
            self.match(EParser.CATEGORY)
            self.state = 667
            self.match(EParser.BINDINGS)
            self.state = 668
            self.match(EParser.AS)
            self.state = 669
            self.match(EParser.COLON)
            self.state = 670 
            self.indent()
            self.state = 671 
            localctx.items = self.native_category_binding_list(0)
            self.state = 672 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(EParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_binding_listContext)
            super(EParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(EParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 675 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 683
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryBindingListItemContext(self, EParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 677
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 678 
                    self.lfp()
                    self.state = 679 
                    localctx.item = self.native_category_binding() 
                self.state = 685
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_list

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_listContext, self).copyFrom(ctx)



    class AttributeListContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListContext, self).__init__(parser)
            self.item = None # Attribute_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)
        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeList(self)


    class AttributeListItemContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListItemContext, self).__init__(parser)
            self.items = None # Attribute_identifier_listContext
            self.item = None # Attribute_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTES(self):
            return self.getToken(EParser.ATTRIBUTES, 0)
        def attribute_identifier_list(self):
            return self.getTypedRuleContext(EParser.Attribute_identifier_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def attribute_identifier(self):
            return self.getTypedRuleContext(EParser.Attribute_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeListItem(self)



    def attribute_list(self):

        localctx = EParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_attribute_list)
        try:
            self.state = 696
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 686
                self.match(EParser.WITH)
                self.state = 687
                self.match(EParser.ATTRIBUTE)
                self.state = 688 
                localctx.item = self.attribute_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 689
                self.match(EParser.WITH)
                self.state = 690
                self.match(EParser.ATTRIBUTES)
                self.state = 691 
                localctx.items = self.attribute_identifier_list()
                self.state = 694
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 692
                    self.match(EParser.AND)
                    self.state = 693 
                    localctx.item = self.attribute_identifier()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def ABSTRACT(self):
            return self.getToken(EParser.ABSTRACT, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = EParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.match(EParser.DEFINE)
            self.state = 699 
            localctx.name = self.method_identifier()
            self.state = 700
            self.match(EParser.AS)
            self.state = 701
            self.match(EParser.ABSTRACT)
            self.state = 702
            self.match(EParser.METHOD)
            self.state = 705
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 703
                self.match(EParser.RECEIVING)
                self.state = 704 
                localctx.args = self.full_argument_list()


            self.state = 709
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 707
                self.match(EParser.RETURNING)
                self.state = 708 
                localctx.typ = self.typedef(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def getRuleIndex(self):
            return EParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = EParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711
            self.match(EParser.DEFINE)
            self.state = 712 
            localctx.name = self.method_identifier()
            self.state = 713
            self.match(EParser.AS)
            self.state = 714
            self.match(EParser.METHOD)
            self.state = 717
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 715
                self.match(EParser.RECEIVING)
                self.state = 716 
                localctx.args = self.full_argument_list()


            self.state = 721
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 719
                self.match(EParser.RETURNING)
                self.state = 720 
                localctx.typ = self.typedef(0)


            self.state = 723
            self.match(EParser.DOING)
            self.state = 724
            self.match(EParser.COLON)
            self.state = 725 
            self.indent()
            self.state = 726 
            localctx.stmts = self.statement_list()
            self.state = 727 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Full_argument_listContext
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def RETURNING(self):
            return self.getToken(EParser.RETURNING, 0)

        def full_argument_list(self):
            return self.getTypedRuleContext(EParser.Full_argument_listContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = EParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.match(EParser.DEFINE)
            self.state = 730 
            localctx.name = self.method_identifier()
            self.state = 731
            self.match(EParser.AS)
            self.state = 733
            _la = self._input.LA(1)
            if _la==EParser.NATIVE:
                self.state = 732
                self.match(EParser.NATIVE)


            self.state = 735
            self.match(EParser.METHOD)
            self.state = 738
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 736
                self.match(EParser.RECEIVING)
                self.state = 737 
                localctx.args = self.full_argument_list()


            self.state = 742
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 740
                self.match(EParser.RETURNING)
                self.state = 741 
                localctx.typ = self.category_or_any_type()


            self.state = 744
            self.match(EParser.DOING)
            self.state = 745
            self.match(EParser.COLON)
            self.state = 746 
            self.indent()
            self.state = 747 
            localctx.stmts = self.native_statement_list()
            self.state = 748 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def VERIFYING(self):
            return self.getToken(EParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(EParser.Assertion_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = EParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            self.match(EParser.DEFINE)
            self.state = 751
            localctx.name = self.match(EParser.TEXT_LITERAL)
            self.state = 752
            self.match(EParser.AS)
            self.state = 753
            self.match(EParser.TEST)
            self.state = 754
            self.match(EParser.METHOD)
            self.state = 755
            self.match(EParser.DOING)
            self.state = 756
            self.match(EParser.COLON)
            self.state = 757 
            self.indent()
            self.state = 758 
            localctx.stmts = self.statement_list()
            self.state = 759 
            self.dedent()
            self.state = 760 
            self.lfp()
            self.state = 761
            self.match(EParser.AND)
            self.state = 762
            self.match(EParser.VERIFYING)
            self.state = 769
            token = self._input.LA(1)
            if token in [EParser.COLON]:
                self.state = 763
                self.match(EParser.COLON)
                self.state = 764 
                self.indent()
                self.state = 765 
                localctx.exps = self.assertion_list()
                self.state = 766 
                self.dedent()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                self.state = 768 
                localctx.error = self.symbol_identifier()

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
            super(EParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assertion

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = EParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 771 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Full_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Full_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext

        def argument_list(self):
            return self.getTypedRuleContext(EParser.Argument_listContext,0)


        def AND(self):
            return self.getToken(EParser.AND, 0)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_full_argument_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFull_argument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFull_argument_list(self)




    def full_argument_list(self):

        localctx = EParser.Full_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_full_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 773 
            localctx.items = self.argument_list()
            self.state = 776
            _la = self._input.LA(1)
            if _la==EParser.AND:
                self.state = 774
                self.match(EParser.AND)
                self.state = 775 
                localctx.item = self.argument()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.name = None # Variable_identifierContext
            self.attrs = None # Attribute_listContext
            self.value = None # Literal_expressionContext

        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(EParser.Attribute_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_typed_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = EParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778 
            localctx.typ = self.category_or_any_type()
            self.state = 779 
            localctx.name = self.variable_identifier()
            self.state = 781
            _la = self._input.LA(1)
            if _la==EParser.WITH:
                self.state = 780 
                localctx.attrs = self.attribute_list()


            self.state = 785
            _la = self._input.LA(1)
            if _la==EParser.EQ:
                self.state = 783
                self.match(EParser.EQ)
                self.state = 784 
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(EParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(EParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(EParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(EParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(EParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(EParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(EParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(EParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(EParser.Break_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(EParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(EParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(EParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(EParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_call_statementContext
            self.copyFrom(ctx)

        def method_call_statement(self):
            return self.getTypedRuleContext(EParser.Method_call_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(EParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(EParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(EParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(EParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a EParser.StatementContext)
            super(EParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(EParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = EParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 806
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 787 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 788 
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 789 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 790 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = EParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 791 
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = EParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 792 
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 793 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 794 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 795 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 796 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 797 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 798 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 799 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 800 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 801 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 802 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 803 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 804 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = EParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 805 
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
            super(EParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(EParser.FLUSH, 0)

        def getRuleIndex(self):
            return EParser.RULE_flush_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = EParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 808
            self.match(EParser.FLUSH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(EParser.DELETE, 0)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(EParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(EParser.STORE, 0)

        def AND(self):
            return self.getToken(EParser.AND, 0)

        def getRuleIndex(self):
            return EParser.RULE_store_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = EParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_store_statement)
        try:
            self.state = 820
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 810
                self.match(EParser.DELETE)
                self.state = 811 
                localctx.to_del = self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 812
                self.match(EParser.STORE)
                self.state = 813 
                localctx.to_add = self.expression_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 814
                self.match(EParser.DELETE)
                self.state = 815 
                localctx.to_del = self.expression_list()
                self.state = 816
                self.match(EParser.AND)
                self.state = 817
                self.match(EParser.STORE)
                self.state = 818 
                localctx.to_add = self.expression_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_call_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_call_statement

     
        def copyFrom(self, ctx):
            super(EParser.Method_call_statementContext, self).copyFrom(ctx)



    class InvokeStatementContext(Method_call_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_call_statementContext)
            super(EParser.InvokeStatementContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvokeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvokeStatement(self)


    class UnresolvedWithArgsStatementContext(Method_call_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_call_statementContext)
            super(EParser.UnresolvedWithArgsStatementContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedWithArgsStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedWithArgsStatement(self)



    def method_call_statement(self):

        localctx = EParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_call_statement)
        try:
            self.state = 827
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 822 
                localctx.exp = self.unresolved_expression(0)
                self.state = 824
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 823 
                    localctx.args = self.argument_assignment_list()



            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 826 
                localctx.exp = self.invocation_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_resource_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(EParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = EParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(EParser.WITH)
            self.state = 830 
            localctx.stmt = self.assign_variable_statement()
            self.state = 831
            self.match(EParser.COMMA)
            self.state = 832
            self.match(EParser.DO)
            self.state = 833
            self.match(EParser.COLON)
            self.state = 834 
            self.indent()
            self.state = 835 
            localctx.stmts = self.statement_list()
            self.state = 836 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_singleton_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = EParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 838
            self.match(EParser.WITH)
            self.state = 839 
            localctx.typ = self.type_identifier()
            self.state = 840
            self.match(EParser.COMMA)
            self.state = 841
            self.match(EParser.DO)
            self.state = 842
            self.match(EParser.COLON)
            self.state = 843 
            self.indent()
            self.state = 844 
            localctx.stmts = self.statement_list()
            self.state = 845 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(EParser.SWITCH, 0)

        def ON(self):
            return self.getToken(EParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(EParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(EParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_switch_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = EParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 847
            self.match(EParser.SWITCH)
            self.state = 848
            self.match(EParser.ON)
            self.state = 849 
            localctx.exp = self.expression(0)
            self.state = 850
            self.match(EParser.COLON)
            self.state = 851 
            self.indent()
            self.state = 852 
            localctx.cases = self.switch_case_statement_list()
            self.state = 860
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 853 
                self.lfp()
                self.state = 854
                self.match(EParser.OTHERWISE)
                self.state = 855
                self.match(EParser.COLON)
                self.state = 856 
                self.indent()
                self.state = 857 
                localctx.stmts = self.statement_list()
                self.state = 858 
                self.dedent()


            self.state = 862 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(EParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statementContext)
            super(EParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statementContext)
            super(EParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(EParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = EParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_case_statement)
        try:
            self.state = 879
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 864
                self.match(EParser.WHEN)
                self.state = 865 
                localctx.exp = self.atomic_literal()
                self.state = 866
                self.match(EParser.COLON)
                self.state = 867 
                self.indent()
                self.state = 868 
                localctx.stmts = self.statement_list()
                self.state = 869 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 871
                self.match(EParser.WHEN)
                self.state = 872
                self.match(EParser.IN)
                self.state = 873 
                localctx.exp = self.literal_collection()
                self.state = 874
                self.match(EParser.COLON)
                self.state = 875 
                self.indent()
                self.state = 876 
                localctx.stmts = self.statement_list()
                self.state = 877 
                self.dedent()
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
            super(EParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(EParser.FOR, 0)

        def EACH(self):
            return self.getToken(EParser.EACH, 0)

        def IN(self):
            return self.getToken(EParser.IN, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)

        def getRuleIndex(self):
            return EParser.RULE_for_each_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = EParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self.match(EParser.FOR)
            self.state = 882
            self.match(EParser.EACH)
            self.state = 883 
            localctx.name1 = self.variable_identifier()
            self.state = 886
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 884
                self.match(EParser.COMMA)
                self.state = 885 
                localctx.name2 = self.variable_identifier()


            self.state = 888
            self.match(EParser.IN)
            self.state = 889 
            localctx.source = self.expression(0)
            self.state = 890
            self.match(EParser.COLON)
            self.state = 891 
            self.indent()
            self.state = 892 
            localctx.stmts = self.statement_list()
            self.state = 893 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(EParser.DO, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(EParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_do_while_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = EParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 895
            self.match(EParser.DO)
            self.state = 896
            self.match(EParser.COLON)
            self.state = 897 
            self.indent()
            self.state = 898 
            localctx.stmts = self.statement_list()
            self.state = 899 
            self.dedent()
            self.state = 900 
            self.lfp()
            self.state = 901
            self.match(EParser.WHILE)
            self.state = 902 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(EParser.WHILE, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_while_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = EParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 904
            self.match(EParser.WHILE)
            self.state = 905 
            localctx.exp = self.expression(0)
            self.state = 906
            self.match(EParser.COLON)
            self.state = 907 
            self.indent()
            self.state = 908 
            localctx.stmts = self.statement_list()
            self.state = 909 
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(EParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(EParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(EParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_if_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = EParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 911
            self.match(EParser.IF)
            self.state = 912 
            localctx.exp = self.expression(0)
            self.state = 913
            self.match(EParser.COLON)
            self.state = 914 
            self.indent()
            self.state = 915 
            localctx.stmts = self.statement_list()
            self.state = 916 
            self.dedent()
            self.state = 920
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 917 
                self.lfp()
                self.state = 918 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 929
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 922 
                self.lfp()
                self.state = 923
                self.match(EParser.ELSE)
                self.state = 924
                self.match(EParser.COLON)
                self.state = 925 
                self.indent()
                self.state = 926 
                localctx.elseStmts = self.statement_list()
                self.state = 927 
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_if_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Else_if_statement_listContext)
            super(EParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def IF(self):
            return self.getToken(EParser.IF, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Else_if_statement_listContext)
            super(EParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def IF(self):
            return self.getToken(EParser.IF, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(EParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 932
            self.match(EParser.ELSE)
            self.state = 933
            self.match(EParser.IF)
            self.state = 934 
            localctx.exp = self.expression(0)
            self.state = 935
            self.match(EParser.COLON)
            self.state = 936 
            self.indent()
            self.state = 937 
            localctx.stmts = self.statement_list()
            self.state = 938 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 952
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 940
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 941 
                    self.lfp()
                    self.state = 942
                    self.match(EParser.ELSE)
                    self.state = 943
                    self.match(EParser.IF)
                    self.state = 944 
                    localctx.exp = self.expression(0)
                    self.state = 945
                    self.match(EParser.COLON)
                    self.state = 946 
                    self.indent()
                    self.state = 947 
                    localctx.stmts = self.statement_list()
                    self.state = 948 
                    self.dedent() 
                self.state = 954
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(EParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_raise_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = EParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 955
            self.match(EParser.RAISE)
            self.state = 956 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Try_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(EParser.SWITCH, 0)

        def ON(self):
            return self.getToken(EParser.ON, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IndentContext)
            else:
                return self.getTypedRuleContext(EParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DedentContext)
            else:
                return self.getTypedRuleContext(EParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfsContext)
            else:
                return self.getTypedRuleContext(EParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(EParser.Statement_listContext,i)


        def ALWAYS(self):
            return self.getToken(EParser.ALWAYS, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(EParser.Catch_statement_listContext,0)


        def OTHERWISE(self):
            return self.getToken(EParser.OTHERWISE, 0)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def getRuleIndex(self):
            return EParser.RULE_try_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = EParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 958
            self.match(EParser.SWITCH)
            self.state = 959
            self.match(EParser.ON)
            self.state = 960 
            localctx.name = self.variable_identifier()
            self.state = 961
            self.match(EParser.DOING)
            self.state = 962
            self.match(EParser.COLON)
            self.state = 963 
            self.indent()
            self.state = 964 
            localctx.stmts = self.statement_list()
            self.state = 965 
            self.dedent()
            self.state = 966 
            self.lfs()
            self.state = 968
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 967 
                localctx.handlers = self.catch_statement_list()


            self.state = 981
            _la = self._input.LA(1)
            if _la==EParser.OTHERWISE or _la==EParser.WHEN:
                self.state = 973
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 970
                    self.match(EParser.OTHERWISE)

                elif token in [EParser.WHEN]:
                    self.state = 971
                    self.match(EParser.WHEN)
                    self.state = 972
                    self.match(EParser.ANY)

                else:
                    raise NoViableAltException(self)

                self.state = 975
                self.match(EParser.COLON)
                self.state = 976 
                self.indent()
                self.state = 977 
                localctx.anyStmts = self.statement_list()
                self.state = 978 
                self.dedent()
                self.state = 979 
                self.lfs()


            self.state = 990
            _la = self._input.LA(1)
            if _la==EParser.ALWAYS:
                self.state = 983
                self.match(EParser.ALWAYS)
                self.state = 984
                self.match(EParser.COLON)
                self.state = 985 
                self.indent()
                self.state = 986 
                localctx.finalStmts = self.statement_list()
                self.state = 987 
                self.dedent()
                self.state = 988 
                self.lfs()


            self.state = 992 
            self.lfs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(EParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statementContext)
            super(EParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statementContext)
            super(EParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(EParser.WHEN, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(EParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = EParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_catch_statement)
        try:
            self.state = 1013
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 994
                self.match(EParser.WHEN)
                self.state = 995 
                localctx.name = self.symbol_identifier()
                self.state = 996
                self.match(EParser.COLON)
                self.state = 997 
                self.indent()
                self.state = 998 
                localctx.stmts = self.statement_list()
                self.state = 999 
                self.dedent()
                self.state = 1000 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1002
                self.match(EParser.WHEN)
                self.state = 1003
                self.match(EParser.IN)
                self.state = 1004
                self.match(EParser.LBRAK)
                self.state = 1005 
                localctx.exp = self.symbol_list()
                self.state = 1006
                self.match(EParser.RBRAK)
                self.state = 1007
                self.match(EParser.COLON)
                self.state = 1008 
                self.indent()
                self.state = 1009 
                localctx.stmts = self.statement_list()
                self.state = 1010 
                self.dedent()
                self.state = 1011 
                self.lfs()
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
            super(EParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(EParser.BREAK, 0)

        def getRuleIndex(self):
            return EParser.RULE_break_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = EParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1015
            self.match(EParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_return_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = EParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1017
            self.match(EParser.RETURN)
            self.state = 1019
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (EParser.VARIABLE_IDENTIFIER - 162)) | (1 << (EParser.TEXT_LITERAL - 162)) | (1 << (EParser.UUID_LITERAL - 162)) | (1 << (EParser.INTEGER_LITERAL - 162)) | (1 << (EParser.HEXA_LITERAL - 162)) | (1 << (EParser.DECIMAL_LITERAL - 162)) | (1 << (EParser.DATETIME_LITERAL - 162)) | (1 << (EParser.TIME_LITERAL - 162)) | (1 << (EParser.DATE_LITERAL - 162)) | (1 << (EParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1018 
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(EParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntDivideExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(EParser.IF, 0)
        def ELSE(self):
            return self.getToken(EParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTernaryExpression(self)


    class FetchStoreExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FetchStoreExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_store_expressionContext
            self.copyFrom(ctx)

        def fetch_store_expression(self):
            return self.getTypedRuleContext(EParser.Fetch_store_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchStoreExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchStoreExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsAllExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(EParser.LTGT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInExpression(self)


    class DocumentExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(EParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocumentExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(EParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGreaterThanExpression(self)


    class InvocationExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InvocationExpressionContext, self).__init__(parser)
            self.exp = None # Invocation_expressionContext
            self.copyFrom(ctx)

        def invocation_expression(self):
            return self.getTypedRuleContext(EParser.Invocation_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocationExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocationExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(EParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeExpression(self)


    class AmbiguousExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AmbiguousExpressionContext, self).__init__(parser)
            self.exp = None # Ambiguous_expressionContext
            self.copyFrom(ctx)

        def ambiguous_expression(self):
            return self.getTypedRuleContext(EParser.Ambiguous_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAmbiguousExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAmbiguousExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(EParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLessThanOrEqualExpression(self)


    class ReadOneExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadOneExpressionContext, self).__init__(parser)
            self.exp = None # Read_one_expressionContext
            self.copyFrom(ctx)

        def read_one_expression(self):
            return self.getTypedRuleContext(EParser.Read_one_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReadOneExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReadOneExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAndExpression(self)


    class MethodCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodCallExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ClosureExpressionContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def METHOD_T(self):
            return self.getToken(EParser.METHOD_T, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitClosureExpression(self)


    class SortedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(EParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSortedExpression(self)


    class BlobExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.BlobExpressionContext, self).__init__(parser)
            self.exp = None # Blob_expressionContext
            self.copyFrom(ctx)

        def blob_expression(self):
            return self.getTypedRuleContext(EParser.Blob_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlobExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlobExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsAnyExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsExpression(self)


    class FilteredListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FilteredListExpressionContext, self).__init__(parser)
            self.src = None # ExpressionContext
            self.copyFrom(ctx)

        def filtered_list_suffix(self):
            return self.getTypedRuleContext(EParser.Filtered_list_suffixContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFilteredListExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFilteredListExpression(self)


    class ConstructorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(EParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(EParser.TILDE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRoughlyEqualsExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(EParser.EXECUTE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExecuteExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(EParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(EParser.FOR, 0)
        def EACH(self):
            return self.getToken(EParser.EACH, 0)
        def IN(self):
            return self.getToken(EParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIteratorExpression(self)


    class UnresolvedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.UnresolvedExpressionContext, self).__init__(parser)
            self.exp = None # Unresolved_expressionContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(EParser.IS, 0)
        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(EParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(EParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(EParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(EParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAddExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(EParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNotContainsAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInstanceExpression(self)


    class ReadAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadAllExpressionContext, self).__init__(parser)
            self.exp = None # Read_all_expressionContext
            self.copyFrom(ctx)

        def read_all_expression(self):
            return self.getTypedRuleContext(EParser.Read_all_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReadAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReadAllExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(EParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(EParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitContainsAnyExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(EParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1049
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1022
                self.match(EParser.MINUS)
                self.state = 1023 
                localctx.exp = self.expression(42)
                pass

            elif la_ == 2:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1024
                self.match(EParser.NOT)
                self.state = 1025 
                localctx.exp = self.expression(41)
                pass

            elif la_ == 3:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1026
                self.match(EParser.CODE)
                self.state = 1027
                self.match(EParser.COLON)
                self.state = 1028 
                localctx.exp = self.expression(14)
                pass

            elif la_ == 4:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1029 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1030 
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 6:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1031 
                localctx.exp = self.unresolved_expression(0)
                self.state = 1032 
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1034
                self.match(EParser.EXECUTE)
                self.state = 1035
                self.match(EParser.COLON)
                self.state = 1036 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1037
                self.match(EParser.METHOD_T)
                self.state = 1038
                self.match(EParser.COLON)
                self.state = 1039 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.BlobExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1040 
                localctx.exp = self.blob_expression()
                pass

            elif la_ == 10:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1041 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 11:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1042 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 12:
                localctx = EParser.FetchStoreExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1043 
                localctx.exp = self.fetch_store_expression()
                pass

            elif la_ == 13:
                localctx = EParser.ReadAllExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1044 
                localctx.exp = self.read_all_expression()
                pass

            elif la_ == 14:
                localctx = EParser.ReadOneExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1045 
                localctx.exp = self.read_one_expression()
                pass

            elif la_ == 15:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1046 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 16:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1047 
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 17:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1048 
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1154
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1051
                        if not self.precpred(self._ctx, 40):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 40)")
                        self.state = 1052 
                        self.multiply()
                        self.state = 1053 
                        localctx.right = self.expression(41)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1055
                        if not self.precpred(self._ctx, 39):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 39)")
                        self.state = 1056 
                        self.divide()
                        self.state = 1057 
                        localctx.right = self.expression(40)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1059
                        if not self.precpred(self._ctx, 38):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 38)")
                        self.state = 1060 
                        self.modulo()
                        self.state = 1061 
                        localctx.right = self.expression(39)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1063
                        if not self.precpred(self._ctx, 37):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 37)")
                        self.state = 1064 
                        self.idivide()
                        self.state = 1065 
                        localctx.right = self.expression(38)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1067
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 1068
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 1069 
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1070
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 1071
                        self.match(EParser.LT)
                        self.state = 1072 
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1073
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 1074
                        self.match(EParser.LTE)
                        self.state = 1075 
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1076
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 1077
                        self.match(EParser.GT)
                        self.state = 1078 
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1079
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1080
                        self.match(EParser.GTE)
                        self.state = 1081 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1082
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1083
                        self.match(EParser.EQ)
                        self.state = 1084 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1085
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1086
                        self.match(EParser.LTGT)
                        self.state = 1087 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1088
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1089
                        self.match(EParser.TILDE)
                        self.state = 1090 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 13:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1091
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1092
                        self.match(EParser.OR)
                        self.state = 1093 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 14:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1094
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1095
                        self.match(EParser.AND)
                        self.state = 1096 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 15:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1097
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1098
                        self.match(EParser.IF)
                        self.state = 1099 
                        localctx.test = self.expression(0)
                        self.state = 1100
                        self.match(EParser.ELSE)
                        self.state = 1101 
                        localctx.ifFalse = self.expression(25)
                        pass

                    elif la_ == 16:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1103
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1104
                        self.match(EParser.IN)
                        self.state = 1105 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 17:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1106
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1107
                        self.match(EParser.CONTAINS)
                        self.state = 1108 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 18:
                        localctx = EParser.ContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1109
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1110
                        self.match(EParser.CONTAINS)
                        self.state = 1111
                        self.match(EParser.ALL)
                        self.state = 1112 
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 19:
                        localctx = EParser.ContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1113
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1114
                        self.match(EParser.CONTAINS)
                        self.state = 1115
                        self.match(EParser.ANY)
                        self.state = 1116 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1117
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1118
                        self.match(EParser.NOT)
                        self.state = 1119
                        self.match(EParser.IN)
                        self.state = 1120 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1121
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1122
                        self.match(EParser.NOT)
                        self.state = 1123
                        self.match(EParser.CONTAINS)
                        self.state = 1124 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1125
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1126
                        self.match(EParser.NOT)
                        self.state = 1127
                        self.match(EParser.CONTAINS)
                        self.state = 1128
                        self.match(EParser.ALL)
                        self.state = 1129 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 23:
                        localctx = EParser.NotContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1130
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1131
                        self.match(EParser.NOT)
                        self.state = 1132
                        self.match(EParser.CONTAINS)
                        self.state = 1133
                        self.match(EParser.ANY)
                        self.state = 1134 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 24:
                        localctx = EParser.IteratorExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1135
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1136
                        self.match(EParser.FOR)
                        self.state = 1137
                        self.match(EParser.EACH)
                        self.state = 1138 
                        localctx.name = self.variable_identifier()
                        self.state = 1139
                        self.match(EParser.IN)
                        self.state = 1140 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1142
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1143
                        self.match(EParser.IS)
                        self.state = 1144
                        self.match(EParser.NOT)
                        self.state = 1145 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1146
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1147
                        self.match(EParser.IS)
                        self.state = 1148 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1149
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1150
                        self.match(EParser.AS)
                        self.state = 1151 
                        localctx.right = self.category_or_any_type()
                        pass

                    elif la_ == 28:
                        localctx = EParser.FilteredListExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.src = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1152
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1153 
                        self.filtered_list_suffix()
                        pass

             
                self.state = 1158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Unresolved_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Unresolved_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_unresolved_expression

     
        def copyFrom(self, ctx):
            super(EParser.Unresolved_expressionContext, self).copyFrom(ctx)


    class UnresolvedSelectorContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedSelectorContext, self).__init__(parser)
            self.parent = None # Unresolved_expressionContext
            self.selector = None # Unresolved_selectorContext
            self.copyFrom(ctx)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)

        def unresolved_selector(self):
            return self.getTypedRuleContext(EParser.Unresolved_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedSelector(self)


    class UnresolvedIdentifierContext(Unresolved_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Unresolved_expressionContext)
            super(EParser.UnresolvedIdentifierContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolvedIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolvedIdentifier(self)



    def unresolved_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Unresolved_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1160 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1163 
                    localctx.selector = self.unresolved_selector() 
                self.state = 1168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Unresolved_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Unresolved_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext

        def DOT(self):
            return self.getToken(EParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_unresolved_selector

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUnresolved_selector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUnresolved_selector(self)




    def unresolved_selector(self):

        localctx = EParser.Unresolved_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1169
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1170
            self.match(EParser.DOT)
            self.state = 1171 
            localctx.name = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Invocation_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def INVOKE(self):
            return self.getToken(EParser.INVOKE, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def invocation_trailer(self):
            return self.getTypedRuleContext(EParser.Invocation_trailerContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_invocation_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocation_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocation_expression(self)




    def invocation_expression(self):

        localctx = EParser.Invocation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1173
            self.match(EParser.INVOKE)
            self.state = 1174
            self.match(EParser.COLON)
            self.state = 1175 
            localctx.name = self.variable_identifier()
            self.state = 1176 
            self.invocation_trailer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_trailerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Invocation_trailerContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_invocation_trailer

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterInvocation_trailer(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitInvocation_trailer(self)




    def invocation_trailer(self):

        localctx = EParser.Invocation_trailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1178
            if not self.willBe(EParser.LF):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBe(EParser.LF)")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(EParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(EParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(EParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_expressionContext)
            super(EParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(EParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1181 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1183
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1184 
                    localctx.selector = self.instance_selector() 
                self.state = 1189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Instance_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(EParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(EParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a EParser.Instance_selectorContext)
            super(EParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = EParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance_selector)
        try:
            self.state = 1203
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1190
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1191
                self.match(EParser.DOT)
                self.state = 1192 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1193
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1194
                self.match(EParser.LBRAK)
                self.state = 1195 
                localctx.xslice = self.slice_arguments()
                self.state = 1196
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1198
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1199
                self.match(EParser.LBRAK)
                self.state = 1200 
                localctx.exp = self.expression(0)
                self.state = 1201
                self.match(EParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_document_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = EParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self.match(EParser.DOCUMENT)
            self.state = 1208
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 1206
                self.match(EParser.FROM)
                self.state = 1207 
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Blob_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_blob_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = EParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blob_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1210
            self.match(EParser.BLOB)
            self.state = 1211
            self.match(EParser.FROM)
            self.state = 1212 
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(EParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.firstArg = None # ExpressionContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorFrom(self)


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = EParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1235
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1214 
                localctx.typ = self.mutable_category_type()
                self.state = 1215
                self.match(EParser.FROM)
                self.state = 1216 
                localctx.firstArg = self.expression(0)
                self.state = 1225
                la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
                if la_ == 1:
                    self.state = 1218
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1217
                        self.match(EParser.COMMA)


                    self.state = 1220 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1223
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        self.state = 1221
                        self.match(EParser.AND)
                        self.state = 1222 
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1227 
                localctx.typ = self.mutable_category_type()
                self.state = 1233
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 1228 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1231
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        self.state = 1229
                        self.match(EParser.AND)
                        self.state = 1230 
                        localctx.arg = self.argument_assignment()




                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TO(self):
            return self.getToken(EParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_write_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = EParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1237
            self.match(EParser.WRITE)
            self.state = 1238 
            localctx.what = self.expression(0)
            self.state = 1239
            self.match(EParser.TO)
            self.state = 1240 
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ambiguous_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Ambiguous_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Unresolved_expressionContext
            self.exp = None # ExpressionContext

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def unresolved_expression(self):
            return self.getTypedRuleContext(EParser.Unresolved_expressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_ambiguous_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAmbiguous_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAmbiguous_expression(self)




    def ambiguous_expression(self):

        localctx = EParser.Ambiguous_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1242 
            localctx.method = self.unresolved_expression(0)
            self.state = 1243
            self.match(EParser.MINUS)
            self.state = 1244 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filtered_list_suffixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Filtered_list_suffixContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.predicate = None # ExpressionContext

        def FILTERED(self):
            return self.getToken(EParser.FILTERED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_filtered_list_suffix

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFiltered_list_suffix(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFiltered_list_suffix(self)




    def filtered_list_suffix(self):

        localctx = EParser.Filtered_list_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_filtered_list_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1246
            self.match(EParser.FILTERED)
            self.state = 1247
            self.match(EParser.WITH)
            self.state = 1248 
            localctx.name = self.variable_identifier()
            self.state = 1249
            self.match(EParser.WHERE)
            self.state = 1250 
            localctx.predicate = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_store_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(EParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_store_expressionContext)
            super(EParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)
        def ONE(self):
            return self.getToken(EParser.ONE, 0)
        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Fetch_store_expressionContext)
            super(EParser.FetchManyContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)
        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)
        def ORDER(self):
            return self.getToken(EParser.ORDER, 0)
        def BY(self):
            return self.getToken(EParser.BY, 0)
        def ALL(self):
            return self.getToken(EParser.ALL, 0)
        def TO(self):
            return self.getToken(EParser.TO, 0)
        def ROWS(self):
            return self.getToken(EParser.ROWS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)

        def order_by_list(self):
            return self.getTypedRuleContext(EParser.Order_by_listContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(EParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = EParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1288
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = EParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1252
                self.match(EParser.FETCH)
                self.state = 1253
                self.match(EParser.ONE)

                self.state = 1255
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE or _la==EParser.TYPE_IDENTIFIER:
                    self.state = 1254 
                    localctx.typ = self.mutable_category_type()


                self.state = 1257
                self.match(EParser.WHERE)
                self.state = 1258 
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1259
                self.match(EParser.FETCH)
                self.state = 1277
                token = self._input.LA(1)
                if token in [EParser.ALL]:
                    self.state = 1260
                    self.match(EParser.ALL)
                    self.state = 1262
                    la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                    if la_ == 1:
                        self.state = 1261 
                        localctx.typ = self.mutable_category_type()



                elif token in [EParser.MUTABLE, EParser.TYPE_IDENTIFIER]:
                    self.state = 1264 
                    localctx.typ = self.mutable_category_type()
                    self.state = 1266
                    _la = self._input.LA(1)
                    if _la==EParser.ROWS:
                        self.state = 1265
                        self.match(EParser.ROWS)


                    self.state = 1268 
                    localctx.xstart = self.expression(0)
                    self.state = 1269
                    self.match(EParser.TO)
                    self.state = 1270 
                    localctx.xstop = self.expression(0)

                elif token in [EParser.ROWS]:
                    self.state = 1272
                    self.match(EParser.ROWS)
                    self.state = 1273 
                    localctx.xstart = self.expression(0)
                    self.state = 1274
                    self.match(EParser.TO)
                    self.state = 1275 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1281
                la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                if la_ == 1:
                    self.state = 1279
                    self.match(EParser.WHERE)
                    self.state = 1280 
                    localctx.predicate = self.expression(0)


                self.state = 1286
                la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                if la_ == 1:
                    self.state = 1283
                    self.match(EParser.ORDER)
                    self.state = 1284
                    self.match(EParser.BY)
                    self.state = 1285 
                    localctx.orderby = self.order_by_list()


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
            super(EParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(EParser.SORTED, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(EParser.Instance_expressionContext,i)


        def DESC(self):
            return self.getToken(EParser.DESC, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def key_token(self):
            return self.getTypedRuleContext(EParser.Key_tokenContext,0)


        def getRuleIndex(self):
            return EParser.RULE_sorted_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = EParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1290
            self.match(EParser.SORTED)
            self.state = 1292
            _la = self._input.LA(1)
            if _la==EParser.DESC:
                self.state = 1291
                self.match(EParser.DESC)


            self.state = 1294 
            localctx.source = self.instance_expression(0)
            self.state = 1300
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.state = 1295
                self.match(EParser.WITH)
                self.state = 1296 
                localctx.key = self.instance_expression(0)
                self.state = 1297
                self.match(EParser.AS)
                self.state = 1298 
                self.key_token()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(EParser.Argument_assignment_listContext, self).copyFrom(ctx)



    class ArgumentAssignmentListExpressionContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListExpression(self)


    class ArgumentAssignmentListNoExpressionContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListNoExpressionContext, self).__init__(parser)
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListNoExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListNoExpression(self)



    def argument_assignment_list(self):

        localctx = EParser.Argument_assignment_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_argument_assignment_list)
        try:
            self.state = 1316
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1302
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1303 
                localctx.exp = self.expression(0)
                self.state = 1309
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 1304 
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1307
                    la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                    if la_ == 1:
                        self.state = 1305
                        self.match(EParser.AND)
                        self.state = 1306 
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1311 
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1314
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1312
                    self.match(EParser.AND)
                    self.state = 1313 
                    localctx.item = self.argument_assignment()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.With_argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_with_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(EParser.With_argument_assignment_listContext, self).copyFrom(ctx)


    class ArgumentAssignmentListContext(With_argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.With_argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(With_argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a EParser.With_argument_assignment_listContext)
            super(EParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # With_argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def with_argument_assignment_list(self):
            return self.getTypedRuleContext(EParser.With_argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(EParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def with_argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.With_argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1319
            self.match(EParser.WITH)
            self.state = 1320 
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1322
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1323
                    self.match(EParser.COMMA)
                    self.state = 1324 
                    localctx.item = self.argument_assignment() 
                self.state = 1329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = EParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1330 
            localctx.exp = self.expression(0)
            self.state = 1331
            self.match(EParser.AS)
            self.state = 1332 
            localctx.name = self.variable_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = EParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1334 
            localctx.inst = self.assignable_instance(0)
            self.state = 1335 
            self.assign()
            self.state = 1336 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Child_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(EParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Child_instanceContext)
            super(EParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Child_instanceContext)
            super(EParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = EParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_child_instance)
        try:
            self.state = 1346
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1338
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1339
                self.match(EParser.DOT)
                self.state = 1340 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1341
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1342
                self.match(EParser.LBRAK)
                self.state = 1343 
                localctx.exp = self.expression(0)
                self.state = 1344
                self.match(EParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_tuple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = EParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1348 
            localctx.items = self.variable_identifier_list()
            self.state = 1349 
            self.assign()
            self.state = 1350 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_lfs

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = EParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1352
                    self.match(EParser.LF) 
                self.state = 1357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_lfp

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = EParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1359 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1358
                self.match(EParser.LF)
                self.state = 1361 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(EParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_indent

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = EParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1364 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1363
                self.match(EParser.LF)
                self.state = 1366 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1368
            self.match(EParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(EParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(EParser.LF)
            else:
                return self.getToken(EParser.LF, i)

        def getRuleIndex(self):
            return EParser.RULE_dedent

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = EParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1370
                self.match(EParser.LF)
                self.state = 1375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1376
            self.match(EParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NOTHING(self):
            return self.getToken(EParser.NOTHING, 0)

        def getRuleIndex(self):
            return EParser.RULE_null_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = EParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1378
            self.match(EParser.NOTHING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Declaration_listContext)
            super(EParser.FullDeclarationListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(EParser.LfsContext,0)

        def EOF(self):
            return self.getToken(EParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(EParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = EParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1381
            _la = self._input.LA(1)
            if _la==EParser.COMMENT or _la==EParser.DEFINE:
                self.state = 1380 
                self.declarations()


            self.state = 1383 
            self.lfs()
            self.state = 1384
            self.match(EParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(EParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_declarations

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = EParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1386 
            self.declaration()
            self.state = 1392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1387 
                    self.lfp()
                    self.state = 1388 
                    self.declaration() 
                self.state = 1394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(EParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(EParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(EParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(EParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = EParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMENT:
                self.state = 1395 
                self.comment_statement()
                self.state = 1396 
                self.lfp()
                self.state = 1402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1408
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 1403 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1404 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1405 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1406 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1407 
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
            super(EParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(EParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = EParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1410 
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
            super(EParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_enum_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = EParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_enum_declaration)
        try:
            self.state = 1414
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1412 
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1413 
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
            super(EParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(EParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = EParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1416 
            self.native_symbol()
            self.state = 1422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1417 
                    self.lfp()
                    self.state = 1418 
                    self.native_symbol() 
                self.state = 1424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(EParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = EParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1425 
            self.category_symbol()
            self.state = 1431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1426 
                    self.lfp()
                    self.state = 1427 
                    self.category_symbol() 
                self.state = 1433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = EParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1434 
            self.symbol_identifier()
            self.state = 1439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1435
                self.match(EParser.COMMA)
                self.state = 1436 
                self.symbol_identifier()
                self.state = 1441
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
            super(EParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(EParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(EParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_constraintContext)
            super(EParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(EParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = EParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_attribute_constraint)
        try:
            self.state = 1452
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1442
                self.match(EParser.IN)
                self.state = 1443 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1444
                self.match(EParser.IN)
                self.state = 1445 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1446
                self.match(EParser.IN)
                self.state = 1447 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1448
                self.match(EParser.MATCHING)
                self.state = 1449
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1450
                self.match(EParser.MATCHING)
                self.state = 1451 
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
            super(EParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_list_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = EParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1455
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1454
                self.match(EParser.MUTABLE)


            self.state = 1457
            self.match(EParser.LBRAK)
            self.state = 1459
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (EParser.VARIABLE_IDENTIFIER - 162)) | (1 << (EParser.TEXT_LITERAL - 162)) | (1 << (EParser.UUID_LITERAL - 162)) | (1 << (EParser.INTEGER_LITERAL - 162)) | (1 << (EParser.HEXA_LITERAL - 162)) | (1 << (EParser.DECIMAL_LITERAL - 162)) | (1 << (EParser.DATETIME_LITERAL - 162)) | (1 << (EParser.TIME_LITERAL - 162)) | (1 << (EParser.DATE_LITERAL - 162)) | (1 << (EParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1458 
                self.expression_list()


            self.state = 1461
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(EParser.LT, 0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_set_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = EParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1464
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1463
                self.match(EParser.MUTABLE)


            self.state = 1466
            self.match(EParser.LT)
            self.state = 1468
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (EParser.VARIABLE_IDENTIFIER - 162)) | (1 << (EParser.TEXT_LITERAL - 162)) | (1 << (EParser.UUID_LITERAL - 162)) | (1 << (EParser.INTEGER_LITERAL - 162)) | (1 << (EParser.HEXA_LITERAL - 162)) | (1 << (EParser.DECIMAL_LITERAL - 162)) | (1 << (EParser.DATETIME_LITERAL - 162)) | (1 << (EParser.TIME_LITERAL - 162)) | (1 << (EParser.DATE_LITERAL - 162)) | (1 << (EParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1467 
                self.expression_list()


            self.state = 1470
            self.match(EParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_expression_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = EParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1472 
            self.expression(0)
            self.state = 1477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1473
                self.match(EParser.COMMA)
                self.state = 1474 
                self.expression(0)
                self.state = 1479
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
            super(EParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(EParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_range_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = EParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1480
            self.match(EParser.LBRAK)
            self.state = 1481 
            localctx.low = self.expression(0)
            self.state = 1482
            self.match(EParser.RANGE)
            self.state = 1483 
            localctx.high = self.expression(0)
            self.state = 1484
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(EParser.TypedefContext, self).copyFrom(ctx)


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(EParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIteratorType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(EParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(EParser.CURSOR, 0)
        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a EParser.TypedefContext)
            super(EParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(EParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 164
        self.enterRecursionRule(localctx, 164, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1498
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1487 
                localctx.p = self.primary_type()

            elif token in [EParser.CURSOR]:
                localctx = EParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1488
                self.match(EParser.CURSOR)
                self.state = 1489
                self.match(EParser.LT)
                self.state = 1490 
                localctx.c = self.typedef(0)
                self.state = 1491
                self.match(EParser.GT)

            elif token in [EParser.ITERATOR]:
                localctx = EParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1493
                self.match(EParser.ITERATOR)
                self.state = 1494
                self.match(EParser.LT)
                self.state = 1495 
                localctx.i = self.typedef(0)
                self.state = 1496
                self.match(EParser.GT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1510
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1508
                    la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
                    if la_ == 1:
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1500
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1501
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1502
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1503
                        self.match(EParser.LBRAK)
                        self.state = 1504
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1505
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1506
                        self.match(EParser.LCURL)
                        self.state = 1507
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1512
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(EParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(EParser.Native_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Primary_typeContext)
            super(EParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = EParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_primary_type)
        try:
            self.state = 1515
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1513 
                localctx.n = self.native_type()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1514 
                localctx.c = self.category_type()

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
            super(EParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(EParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(EParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(EParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(EParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_native_type)
        try:
            self.state = 1531
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1517
                self.match(EParser.BOOLEAN)

            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1518
                self.match(EParser.CHARACTER)

            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1519
                self.match(EParser.TEXT)

            elif token in [EParser.IMAGE]:
                localctx = EParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1520
                self.match(EParser.IMAGE)

            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1521
                self.match(EParser.INTEGER)

            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1522
                self.match(EParser.DECIMAL)

            elif token in [EParser.DOCUMENT]:
                localctx = EParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1523
                self.match(EParser.DOCUMENT)

            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1524
                self.match(EParser.DATE)

            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1525
                self.match(EParser.DATETIME)

            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1526
                self.match(EParser.TIME)

            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1527
                self.match(EParser.PERIOD)

            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1528
                self.match(EParser.CODE)

            elif token in [EParser.BLOB]:
                localctx = EParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1529
                self.match(EParser.BLOB)

            elif token in [EParser.UUID]:
                localctx = EParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1530
                self.match(EParser.UUID)

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
            super(EParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_category_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = EParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1533
            localctx.t1 = self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def getRuleIndex(self):
            return EParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = EParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1536
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1535
                self.match(EParser.MUTABLE)


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
            super(EParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def getRuleIndex(self):
            return EParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = EParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1540
            localctx.t1 = self.match(EParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(EParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_declarationContext)
            super(EParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(EParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = EParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_category_declaration)
        try:
            self.state = 1545
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1542 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1543 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
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

    class Type_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = EParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1547 
            self.type_identifier()
            self.state = 1552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1548
                self.match(EParser.COMMA)
                self.state = 1549 
                self.type_identifier()
                self.state = 1554
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
            super(EParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_method_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = EParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_method_identifier)
        try:
            self.state = 1557
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1555 
                self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1556 
                self.type_identifier()

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
            super(EParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(EParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = EParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_identifier)
        try:
            self.state = 1562
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1559 
                self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1560 
                self.type_identifier()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1561 
                self.symbol_identifier()

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
            super(EParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = EParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1564
            self.match(EParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(EParser.STORABLE, 0)

        def getRuleIndex(self):
            return EParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = EParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1566
            _la = self._input.LA(1)
            if not(_la==EParser.STORABLE or _la==EParser.VARIABLE_IDENTIFIER):
                self._errHandler.recoverInline(self)
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
            super(EParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = EParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1568
            self.match(EParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = EParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1570
            self.match(EParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(EParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_argument_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = EParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1572 
            self.argument()
            self.state = 1577
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1573
                self.match(EParser.COMMA)
                self.state = 1574 
                self.argument()
                self.state = 1579
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
            super(EParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(EParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(EParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a EParser.ArgumentContext)
            super(EParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(EParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = EParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1585
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1580 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1582
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1581
                    self.match(EParser.MUTABLE)


                self.state = 1584 
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
            super(EParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def named_argument(self):
            return self.getTypedRuleContext(EParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(EParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return EParser.RULE_operator_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = EParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_operator_argument)
        try:
            self.state = 1589
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1587 
                self.named_argument()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ITERATOR, EParser.CURSOR, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1588 
                self.typed_argument()

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
            super(EParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_named_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = EParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1591 
            self.variable_identifier()
            self.state = 1594
            _la = self._input.LA(1)
            if _la==EParser.EQ:
                self.state = 1592
                self.match(EParser.EQ)
                self.state = 1593 
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
            super(EParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(EParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_code_argument

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = EParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1596 
            self.code_type()
            self.state = 1597 
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
            super(EParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def getRuleIndex(self):
            return EParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = EParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_category_or_any_type)
        try:
            self.state = 1601
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.DOCUMENT, EParser.BLOB, EParser.IMAGE, EParser.UUID, EParser.ITERATOR, EParser.CURSOR, EParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1599 
                self.typedef(0)

            elif token in [EParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1600 
                self.any_type(0)

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
            super(EParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(EParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 204
        self.enterRecursionRule(localctx, 204, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1604
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1614
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1612
                    la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1606
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1607
                        self.match(EParser.LBRAK)
                        self.state = 1608
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1609
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1610
                        self.match(EParser.LCURL)
                        self.state = 1611
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1616
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(EParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = EParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1617 
            self.member_method_declaration()
            self.state = 1623
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1618 
                    self.lfp()
                    self.state = 1619 
                    self.member_method_declaration() 
                self.state = 1625
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(EParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(EParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = EParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_member_method_declaration)
        try:
            self.state = 1631
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1626 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1627 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1628 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1629 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1630 
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
            super(EParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = EParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633 
            self.native_member_method_declaration()
            self.state = 1639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1634 
                    self.lfp()
                    self.state = 1635 
                    self.native_member_method_declaration() 
                self.state = 1641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(EParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(EParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = EParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_native_member_method_declaration)
        try:
            self.state = 1645
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1642 
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1643 
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1644 
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
            super(EParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(EParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(EParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(EParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_category_bindingContext)
            super(EParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(EParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = EParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_native_category_binding)
        try:
            self.state = 1657
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1647
                self.match(EParser.JAVA)
                self.state = 1648 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1649
                self.match(EParser.CSHARP)
                self.state = 1650 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1651
                self.match(EParser.PYTHON2)
                self.state = 1652 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1653
                self.match(EParser.PYTHON3)
                self.state = 1654 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1655
                self.match(EParser.JAVASCRIPT)
                self.state = 1656 
                localctx.binding = self.javascript_category_binding()

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
            super(EParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_category_binding

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = EParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1659 
            self.identifier()
            self.state = 1661
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.state = 1660 
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
            super(EParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(EParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(EParser.DOT)
            else:
                return self.getToken(EParser.DOT, i)

        def getRuleIndex(self):
            return EParser.RULE_python_module

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = EParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1663
            self.match(EParser.FROM)
            self.state = 1664 
            self.module_token()
            self.state = 1665
            self.match(EParser.COLON)
            self.state = 1666 
            self.identifier()
            self.state = 1671
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1667
                    self.match(EParser.DOT)
                    self.state = 1668 
                    self.identifier() 
                self.state = 1673
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = EParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1674 
            self.identifier()
            self.state = 1676
            la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
            if la_ == 1:
                self.state = 1675 
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
            super(EParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(EParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(EParser.SLASH)
            else:
                return self.getToken(EParser.SLASH, i)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_module

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = EParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1678
            self.match(EParser.FROM)
            self.state = 1679 
            self.module_token()
            self.state = 1680
            self.match(EParser.COLON)
            self.state = 1682
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1681
                self.match(EParser.SLASH)


            self.state = 1684 
            self.javascript_identifier()
            self.state = 1689
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1685
                    self.match(EParser.SLASH)
                    self.state = 1686 
                    self.javascript_identifier() 
                self.state = 1691
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

            self.state = 1694
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                self.state = 1692
                self.match(EParser.DOT)
                self.state = 1693 
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
            super(EParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = EParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1696 
            self.variable_identifier()
            self.state = 1701
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1697
                self.match(EParser.COMMA)
                self.state = 1698 
                self.variable_identifier()
                self.state = 1703
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
            super(EParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = EParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_attribute_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1704 
            self.attribute_identifier()
            self.state = 1709
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1705
                    self.match(EParser.COMMA)
                    self.state = 1706 
                    self.attribute_identifier() 
                self.state = 1711
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(EParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return EParser.RULE_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = EParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_method_declaration)
        try:
            self.state = 1716
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1712 
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1713 
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1714 
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1715 
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
            super(EParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(EParser.COMMENT, 0)

        def getRuleIndex(self):
            return EParser.RULE_comment_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = EParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1718
            self.match(EParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_native_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = EParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720 
            self.native_statement()
            self.state = 1726
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,131,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1721 
                    self.lfp()
                    self.state = 1722 
                    self.native_statement() 
                self.state = 1728
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,131,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(EParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.CSharpNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(EParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(EParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(EParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(EParser.Java_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(EParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(EParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(EParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(EParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = EParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_native_statement)
        try:
            self.state = 1739
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1729
                self.match(EParser.JAVA)
                self.state = 1730 
                self.java_statement()

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1731
                self.match(EParser.CSHARP)
                self.state = 1732 
                self.csharp_statement()

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1733
                self.match(EParser.PYTHON2)
                self.state = 1734 
                self.python_native_statement()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1735
                self.match(EParser.PYTHON3)
                self.state = 1736 
                self.python_native_statement()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1737
                self.match(EParser.JAVASCRIPT)
                self.state = 1738 
                self.javascript_native_statement()

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
            super(EParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(EParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(EParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_native_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = EParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1741 
            self.python_statement()
            self.state = 1743
            _la = self._input.LA(1)
            if _la==EParser.SEMI:
                self.state = 1742
                self.match(EParser.SEMI)


            self.state = 1746
            _la = self._input.LA(1)
            if _la==EParser.FROM:
                self.state = 1745 
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
            super(EParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(EParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(EParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = EParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1748 
            self.javascript_statement()
            self.state = 1750
            _la = self._input.LA(1)
            if _la==EParser.SEMI:
                self.state = 1749
                self.match(EParser.SEMI)


            self.state = 1753
            _la = self._input.LA(1)
            if _la==EParser.FROM:
                self.state = 1752 
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
            super(EParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.StatementContext)
            else:
                return self.getTypedRuleContext(EParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = EParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1755 
            self.statement()
            self.state = 1761
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1756 
                    self.lfp()
                    self.state = 1757 
                    self.statement() 
                self.state = 1763
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.AssertionContext)
            else:
                return self.getTypedRuleContext(EParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_assertion_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = EParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1764 
            self.assertion()
            self.state = 1770
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1765 
                    self.lfp()
                    self.state = 1766 
                    self.assertion() 
                self.state = 1772
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = EParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1773 
            self.switch_case_statement()
            self.state = 1779
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1774 
                    self.lfp()
                    self.state = 1775 
                    self.switch_case_statement() 
                self.state = 1781
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(EParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.LfpContext)
            else:
                return self.getTypedRuleContext(EParser.LfpContext,i)


        def getRuleIndex(self):
            return EParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = EParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1782 
            self.catch_statement()
            self.state = 1788
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1783 
                    self.lfp()
                    self.state = 1784 
                    self.catch_statement() 
                self.state = 1790
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(EParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralListLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(EParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(EParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = EParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_literal_collection)
        try:
            self.state = 1805
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1791
                self.match(EParser.LBRAK)
                self.state = 1792 
                localctx.low = self.atomic_literal()
                self.state = 1793
                self.match(EParser.RANGE)
                self.state = 1794 
                localctx.high = self.atomic_literal()
                self.state = 1795
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1797
                self.match(EParser.LBRAK)
                self.state = 1798 
                self.literal_list_literal()
                self.state = 1799
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1801
                self.match(EParser.LT)
                self.state = 1802 
                self.literal_list_literal()
                self.state = 1803
                self.match(EParser.GT)
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
            super(EParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(EParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(EParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(EParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(EParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(EParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(EParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(EParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(EParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(EParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(EParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Atomic_literalContext)
            super(EParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = EParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_atomic_literal)
        try:
            self.state = 1821
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1807
                localctx.t = self.match(EParser.MIN_INTEGER)

            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1808
                localctx.t = self.match(EParser.MAX_INTEGER)

            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1809
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1810
                localctx.t = self.match(EParser.HEXA_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1811
                localctx.t = self.match(EParser.CHAR_LITERAL)

            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1812
                localctx.t = self.match(EParser.DATE_LITERAL)

            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1813
                localctx.t = self.match(EParser.TIME_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1814
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1815
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1816
                localctx.t = self.match(EParser.DATETIME_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1817
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1818
                localctx.t = self.match(EParser.PERIOD_LITERAL)

            elif token in [EParser.UUID_LITERAL]:
                localctx = EParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1819
                localctx.t = self.match(EParser.UUID_LITERAL)

            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1820 
                localctx.n = self.null_literal()

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
            super(EParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(EParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = EParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1823 
            self.atomic_literal()
            self.state = 1828
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1824
                self.match(EParser.COMMA)
                self.state = 1825 
                self.atomic_literal()
                self.state = 1830
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
            super(EParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(EParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(EParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Selectable_expressionContext)
            super(EParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(EParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = EParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_selectable_expression)
        try:
            self.state = 1835
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1831 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1832 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1833 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1834 
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
            super(EParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

        def getRuleIndex(self):
            return EParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = EParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1837
            _la = self._input.LA(1)
            if not(_la==EParser.SELF or _la==EParser.THIS):
                self._errHandler.recoverInline(self)
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
            super(EParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def getRuleIndex(self):
            return EParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = EParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1839
            self.match(EParser.LPAR)
            self.state = 1840 
            self.expression(0)
            self.state = 1841
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(EParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return EParser.RULE_literal_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = EParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_literal_expression)
        try:
            self.state = 1845
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.UUID_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1843 
                self.atomic_literal()

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT, EParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1844 
                self.collection_literal()

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
            super(EParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(EParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(EParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return EParser.RULE_collection_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = EParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_collection_literal)
        try:
            self.state = 1852
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1847 
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1848 
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1849 
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1850 
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1851 
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
            super(EParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(EParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return EParser.RULE_tuple_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = EParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1855
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1854
                self.match(EParser.MUTABLE)


            self.state = 1857
            self.match(EParser.LPAR)
            self.state = 1859
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (EParser.VARIABLE_IDENTIFIER - 162)) | (1 << (EParser.TEXT_LITERAL - 162)) | (1 << (EParser.UUID_LITERAL - 162)) | (1 << (EParser.INTEGER_LITERAL - 162)) | (1 << (EParser.HEXA_LITERAL - 162)) | (1 << (EParser.DECIMAL_LITERAL - 162)) | (1 << (EParser.DATETIME_LITERAL - 162)) | (1 << (EParser.TIME_LITERAL - 162)) | (1 << (EParser.DATE_LITERAL - 162)) | (1 << (EParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1858 
                self.expression_tuple()


            self.state = 1861
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(EParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_dict_literal

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = EParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1864
            _la = self._input.LA(1)
            if _la==EParser.MUTABLE:
                self.state = 1863
                self.match(EParser.MUTABLE)


            self.state = 1866
            self.match(EParser.LCURL)
            self.state = 1868
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (EParser.VARIABLE_IDENTIFIER - 162)) | (1 << (EParser.TEXT_LITERAL - 162)) | (1 << (EParser.UUID_LITERAL - 162)) | (1 << (EParser.INTEGER_LITERAL - 162)) | (1 << (EParser.HEXA_LITERAL - 162)) | (1 << (EParser.DECIMAL_LITERAL - 162)) | (1 << (EParser.DATETIME_LITERAL - 162)) | (1 << (EParser.TIME_LITERAL - 162)) | (1 << (EParser.DATE_LITERAL - 162)) | (1 << (EParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1867 
                self.dict_entry_list()


            self.state = 1870
            self.match(EParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_expression_tuple

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = EParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1872 
            self.expression(0)
            self.state = 1873
            self.match(EParser.COMMA)
            self.state = 1882
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT) | (1 << EParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (EParser.EXECUTE - 98)) | (1 << (EParser.FETCH - 98)) | (1 << (EParser.INVOKE - 98)) | (1 << (EParser.MUTABLE - 98)) | (1 << (EParser.NOT - 98)) | (1 << (EParser.NOTHING - 98)) | (1 << (EParser.READ - 98)) | (1 << (EParser.SELF - 98)) | (1 << (EParser.SORTED - 98)) | (1 << (EParser.THIS - 98)) | (1 << (EParser.BOOLEAN_LITERAL - 98)) | (1 << (EParser.CHAR_LITERAL - 98)) | (1 << (EParser.MIN_INTEGER - 98)) | (1 << (EParser.MAX_INTEGER - 98)) | (1 << (EParser.SYMBOL_IDENTIFIER - 98)) | (1 << (EParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (EParser.VARIABLE_IDENTIFIER - 162)) | (1 << (EParser.TEXT_LITERAL - 162)) | (1 << (EParser.UUID_LITERAL - 162)) | (1 << (EParser.INTEGER_LITERAL - 162)) | (1 << (EParser.HEXA_LITERAL - 162)) | (1 << (EParser.DECIMAL_LITERAL - 162)) | (1 << (EParser.DATETIME_LITERAL - 162)) | (1 << (EParser.TIME_LITERAL - 162)) | (1 << (EParser.DATE_LITERAL - 162)) | (1 << (EParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1874 
                self.expression(0)
                self.state = 1879
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==EParser.COMMA:
                    self.state = 1875
                    self.match(EParser.COMMA)
                    self.state = 1876 
                    self.expression(0)
                    self.state = 1881
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
            super(EParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(EParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = EParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884 
            self.dict_entry()
            self.state = 1889
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.COMMA:
                self.state = 1885
                self.match(EParser.COMMA)
                self.state = 1886 
                self.dict_entry()
                self.state = 1891
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
            super(EParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_dict_entry

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = EParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892 
            localctx.key = self.expression(0)
            self.state = 1893
            self.match(EParser.COLON)
            self.state = 1894 
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
            super(EParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Slice_argumentsContext)
            super(EParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = EParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_slice_arguments)
        try:
            self.state = 1905
            la_ = self._interp.adaptivePredict(self._input,154,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1896 
                localctx.first = self.expression(0)
                self.state = 1897
                self.match(EParser.COLON)
                self.state = 1898 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1900 
                localctx.first = self.expression(0)
                self.state = 1901
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1903
                self.match(EParser.COLON)
                self.state = 1904 
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
            super(EParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = EParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1907 
            self.variable_identifier()
            self.state = 1908 
            self.assign()
            self.state = 1909 
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
            super(EParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(EParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(EParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(EParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 278
        self.enterRecursionRule(localctx, 278, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1912 
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1918
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,155,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1914
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1915 
                    self.child_instance() 
                self.state = 1920
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(EParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsATypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(EParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Is_expressionContext)
            super(EParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = EParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_is_expression)
        try:
            self.state = 1925
            la_ = self._interp.adaptivePredict(self._input,156,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1921
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1922
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1923 
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1924 
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
            super(EParser.Read_all_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def ALL(self):
            return self.getToken(EParser.ALL, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_all_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = EParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1927
            self.match(EParser.READ)
            self.state = 1928
            self.match(EParser.ALL)
            self.state = 1929
            self.match(EParser.FROM)
            self.state = 1930 
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
            super(EParser.Read_one_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def ONE(self):
            return self.getToken(EParser.ONE, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_one_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = EParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932
            self.match(EParser.READ)
            self.state = 1933
            self.match(EParser.ONE)
            self.state = 1934
            self.match(EParser.FROM)
            self.state = 1935 
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
            super(EParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Order_byContext)
            else:
                return self.getTypedRuleContext(EParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(EParser.COMMA)
            else:
                return self.getToken(EParser.COMMA, i)

        def getRuleIndex(self):
            return EParser.RULE_order_by_list

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = EParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1937 
            self.order_by()
            self.state = 1942
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1938
                    self.match(EParser.COMMA)
                    self.state = 1939 
                    self.order_by() 
                self.state = 1944
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(EParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(EParser.DOT)
            else:
                return self.getToken(EParser.DOT, i)

        def ASC(self):
            return self.getToken(EParser.ASC, 0)

        def DESC(self):
            return self.getToken(EParser.DESC, 0)

        def getRuleIndex(self):
            return EParser.RULE_order_by

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = EParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1945 
            self.variable_identifier()
            self.state = 1950
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1946
                    self.match(EParser.DOT)
                    self.state = 1947 
                    self.variable_identifier() 
                self.state = 1952
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

            self.state = 1954
            la_ = self._interp.adaptivePredict(self._input,159,self._ctx)
            if la_ == 1:
                self.state = 1953
                _la = self._input.LA(1)
                if not(_la==EParser.ASC or _la==EParser.DESC):
                    self._errHandler.recoverInline(self)
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
            super(EParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(EParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(EParser.PLUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(EParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(EParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(EParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(EParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a EParser.OperatorContext)
            super(EParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(EParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = EParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_operator)
        try:
            self.state = 1962
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1956
                self.match(EParser.PLUS)

            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1957
                self.match(EParser.MINUS)

            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1958 
                self.multiply()

            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1959 
                self.divide()

            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1960 
                self.idivide()

            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1961 
                self.modulo()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class New_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = EParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1964
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1965
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
            super(EParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = EParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1967
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1968
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
            super(EParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = EParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1970
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1971
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
            super(EParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = EParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1973
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1974
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
            super(EParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return EParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = EParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1976
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1977
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
            super(EParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(EParser.EQ, 0)

        def getRuleIndex(self):
            return EParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = EParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1979
            self.match(EParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(EParser.STAR, 0)

        def getRuleIndex(self):
            return EParser.RULE_multiply

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = EParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1981
            self.match(EParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(EParser.SLASH, 0)

        def getRuleIndex(self):
            return EParser.RULE_divide

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = EParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1983
            self.match(EParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(EParser.BSLASH, 0)

        def getRuleIndex(self):
            return EParser.RULE_idivide

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = EParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1985
            self.match(EParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(EParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(EParser.MODULO, 0)

        def getRuleIndex(self):
            return EParser.RULE_modulo

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = EParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1987
            _la = self._input.LA(1)
            if not(_la==EParser.PERCENT or _la==EParser.MODULO):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_statementContext)
            super(EParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_statementContext)
            super(EParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = EParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_javascript_statement)
        try:
            self.state = 1996
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1989
                self.match(EParser.RETURN)
                self.state = 1990 
                localctx.exp = self.javascript_expression(0)
                self.state = 1991
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1993 
                localctx.exp = self.javascript_expression(0)
                self.state = 1994
                self.match(EParser.SEMI)

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
            super(EParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_expressionContext)
            super(EParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 314
        self.enterRecursionRule(localctx, 314, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1999 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2005
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 2001
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2002 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 2007
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = EParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_primary_expression)
        try:
            self.state = 2015
            la_ = self._interp.adaptivePredict(self._input,163,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2008 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2009 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2010 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2011 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2012 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2013 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2014 
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
            super(EParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = EParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2017 
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
            super(EParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = EParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2019 
            self.new_token()
            self.state = 2020 
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
            super(EParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_selector_expressionContext)
            super(EParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = EParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_selector_expression)
        try:
            self.state = 2027
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                localctx = EParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2022
                self.match(EParser.DOT)
                self.state = 2023 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = EParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2024
                self.match(EParser.DOT)
                self.state = 2025 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = EParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2026 
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
            super(EParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(EParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = EParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2029 
            localctx.name = self.javascript_identifier()
            self.state = 2030
            self.match(EParser.LPAR)
            self.state = 2032
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.SELF - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.THIS - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.BOOLEAN_LITERAL - 132)) | (1 << (EParser.CHAR_LITERAL - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)) | (1 << (EParser.DOLLAR_IDENTIFIER - 132)) | (1 << (EParser.TEXT_LITERAL - 132)) | (1 << (EParser.INTEGER_LITERAL - 132)) | (1 << (EParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2031 
                localctx.args = self.javascript_arguments(0)


            self.state = 2034
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_argumentsContext)
            super(EParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_argumentsContext)
            super(EParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(EParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2037 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2044
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 2039
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2040
                    self.match(EParser.COMMA)
                    self.state = 2041 
                    localctx.item = self.javascript_expression(0) 
                self.state = 2046
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = EParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2047
            self.match(EParser.LBRAK)
            self.state = 2048 
            localctx.exp = self.javascript_expression(0)
            self.state = 2049
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(EParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = EParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2051
            self.match(EParser.LPAR)
            self.state = 2052 
            localctx.exp = self.javascript_expression(0)
            self.state = 2053
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(EParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = EParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2055 
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
            super(EParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Javascript_literal_expressionContext)
            super(EParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = EParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_literal_expression)
        try:
            self.state = 2062
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2057
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2058
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2059
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2060
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2061
                localctx.t = self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def getRuleIndex(self):
            return EParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = EParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2064
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)) | (1 << (EParser.DOLLAR_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
            super(EParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(EParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_statementContext)
            super(EParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_statementContext)
            super(EParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = EParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_python_statement)
        try:
            self.state = 2069
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2066
                self.match(EParser.RETURN)
                self.state = 2067 
                localctx.exp = self.python_expression(0)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2068 
                localctx.exp = self.python_expression(0)

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
            super(EParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(EParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_expressionContext)
            super(EParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(EParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 340
        self.enterRecursionRule(localctx, 340, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2072 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2078
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,169,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2074
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2075 
                    localctx.child = self.python_selector_expression() 
                self.state = 2080
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,169,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(EParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_primary_expressionContext)
            super(EParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = EParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_primary_expression)
        try:
            self.state = 2085
            la_ = self._interp.adaptivePredict(self._input,170,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2081 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2082 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2083 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2084 
                localctx.exp = self.python_method_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_selector_expressionContext)
            super(EParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(EParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_selector_expressionContext)
            super(EParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = EParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_selector_expression)
        try:
            self.state = 2093
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2087
                self.match(EParser.DOT)
                self.state = 2088 
                localctx.exp = self.python_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2089
                self.match(EParser.LBRAK)
                self.state = 2090 
                localctx.exp = self.python_expression(0)
                self.state = 2091
                self.match(EParser.RBRAK)

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
            super(EParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = EParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2095 
            localctx.name = self.python_identifier()
            self.state = 2096
            self.match(EParser.LPAR)
            self.state = 2098
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.SELF - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.THIS - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.BOOLEAN_LITERAL - 132)) | (1 << (EParser.CHAR_LITERAL - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)) | (1 << (EParser.DOLLAR_IDENTIFIER - 132)) | (1 << (EParser.TEXT_LITERAL - 132)) | (1 << (EParser.INTEGER_LITERAL - 132)) | (1 << (EParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2097 
                localctx.args = self.python_argument_list()


            self.state = 2100
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_argument_listContext)
            super(EParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = EParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_python_argument_list)
        try:
            self.state = 2108
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2102 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2103 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2104 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2105
                self.match(EParser.COMMA)
                self.state = 2106 
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
            super(EParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_ordinal_argument_listContext)
            super(EParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_ordinal_argument_listContext)
            super(EParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2111 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,174,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2113
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2114
                    self.match(EParser.COMMA)
                    self.state = 2115 
                    localctx.item = self.python_expression(0) 
                self.state = 2120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,174,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_named_argument_listContext)
            super(EParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_named_argument_listContext)
            super(EParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def EQ(self):
            return self.getToken(EParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(EParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2122 
            localctx.name = self.python_identifier()
            self.state = 2123
            self.match(EParser.EQ)
            self.state = 2124 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,175,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2126
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2127
                    self.match(EParser.COMMA)
                    self.state = 2128 
                    localctx.name = self.python_identifier()
                    self.state = 2129
                    self.match(EParser.EQ)
                    self.state = 2130 
                    localctx.exp = self.python_expression(0) 
                self.state = 2136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,175,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(EParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = EParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2137
            self.match(EParser.LPAR)
            self.state = 2138 
            localctx.exp = self.python_expression(0)
            self.state = 2139
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(EParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 356
        self.enterRecursionRule(localctx, 356, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2144
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2142
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2143 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2146
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2147
                    self.match(EParser.DOT)
                    self.state = 2148 
                    localctx.name = self.python_identifier() 
                self.state = 2153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_literal_expressionContext)
            super(EParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = EParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_python_literal_expression)
        try:
            self.state = 2159
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2154
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2155
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2156
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2157
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2158
                localctx.t = self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def SELF(self):
            return self.getToken(EParser.SELF, 0)

        def THIS(self):
            return self.getToken(EParser.THIS, 0)

        def getRuleIndex(self):
            return EParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = EParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.SELF - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.THIS - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
            super(EParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(EParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_statementContext)
            super(EParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_statementContext)
            super(EParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = EParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_java_statement)
        try:
            self.state = 2170
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2163
                self.match(EParser.RETURN)
                self.state = 2164 
                localctx.exp = self.java_expression(0)
                self.state = 2165
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2167 
                localctx.exp = self.java_expression(0)
                self.state = 2168
                self.match(EParser.SEMI)

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
            super(EParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(EParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_expressionContext)
            super(EParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(EParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 364
        self.enterRecursionRule(localctx, 364, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2173 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,180,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2175
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2176 
                    localctx.child = self.java_selector_expression() 
                self.state = 2181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,180,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(EParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(EParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(EParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = EParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_java_primary_expression)
        try:
            self.state = 2187
            la_ = self._interp.adaptivePredict(self._input,181,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2182 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2183 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2184 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2185 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2186 
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
            super(EParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = EParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2189 
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
            super(EParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(EParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = EParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2191 
            self.new_token()
            self.state = 2192 
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
            super(EParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_selector_expressionContext)
            super(EParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(EParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_selector_expressionContext)
            super(EParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(EParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = EParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_java_selector_expression)
        try:
            self.state = 2197
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2194
                self.match(EParser.DOT)
                self.state = 2195 
                localctx.exp = self.java_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2196 
                localctx.exp = self.java_item_expression()

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
            super(EParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(EParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = EParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2199 
            localctx.name = self.java_identifier()
            self.state = 2200
            self.match(EParser.LPAR)
            self.state = 2202
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.SELF - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.THIS - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.BOOLEAN_LITERAL - 132)) | (1 << (EParser.CHAR_LITERAL - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)) | (1 << (EParser.NATIVE_IDENTIFIER - 132)) | (1 << (EParser.DOLLAR_IDENTIFIER - 132)) | (1 << (EParser.TEXT_LITERAL - 132)) | (1 << (EParser.INTEGER_LITERAL - 132)) | (1 << (EParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2201 
                localctx.args = self.java_arguments(0)


            self.state = 2204
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(EParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_argumentsContext)
            super(EParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2207 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,184,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2209
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2210
                    self.match(EParser.COMMA)
                    self.state = 2211 
                    localctx.item = self.java_expression(0) 
                self.state = 2216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,184,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = EParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2217
            self.match(EParser.LBRAK)
            self.state = 2218 
            localctx.exp = self.java_expression(0)
            self.state = 2219
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(EParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = EParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2221
            self.match(EParser.LPAR)
            self.state = 2222 
            localctx.exp = self.java_expression(0)
            self.state = 2223
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_identifier_expressionContext)
            super(EParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_identifier_expressionContext)
            super(EParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(EParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 382
        self.enterRecursionRule(localctx, 382, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2226 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2228
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2229
                    self.match(EParser.DOT)
                    self.state = 2230 
                    localctx.name = self.java_identifier() 
                self.state = 2235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_class_identifier_expressionContext)
            super(EParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 384
        self.enterRecursionRule(localctx, 384, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2237 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2239
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2240
                    localctx.name = self.match(EParser.DOLLAR_IDENTIFIER) 
                self.state = 2245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Java_literal_expressionContext)
            super(EParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = EParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_java_literal_expression)
        try:
            self.state = 2251
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2246
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2247
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2248
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2249
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2250
                localctx.t = self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(EParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def getRuleIndex(self):
            return EParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = EParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2253
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)) | (1 << (EParser.NATIVE_IDENTIFIER - 132)) | (1 << (EParser.DOLLAR_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
            super(EParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_statementContext)
            super(EParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(EParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_statementContext)
            super(EParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(EParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = EParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_csharp_statement)
        try:
            self.state = 2262
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2255
                self.match(EParser.RETURN)
                self.state = 2256 
                localctx.exp = self.csharp_expression(0)
                self.state = 2257
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2259 
                localctx.exp = self.csharp_expression(0)
                self.state = 2260
                self.match(EParser.SEMI)

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
            super(EParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_expressionContext)
            super(EParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 392
        self.enterRecursionRule(localctx, 392, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2265 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,189,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2267
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2268 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,189,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = EParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_csharp_primary_expression)
        try:
            self.state = 2279
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2274 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2275 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2276 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2277 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2278 
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
            super(EParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(EParser.This_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = EParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2281 
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
            super(EParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(EParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = EParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2283 
            self.new_token()
            self.state = 2284 
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
            super(EParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_selector_expressionContext)
            super(EParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = EParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_csharp_selector_expression)
        try:
            self.state = 2289
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2286
                self.match(EParser.DOT)
                self.state = 2287 
                localctx.exp = self.csharp_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2288 
                localctx.exp = self.csharp_item_expression()

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
            super(EParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(EParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = EParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2291 
            localctx.name = self.csharp_identifier()
            self.state = 2292
            self.match(EParser.LPAR)
            self.state = 2294
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.SELF - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.THIS - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.BOOLEAN_LITERAL - 132)) | (1 << (EParser.CHAR_LITERAL - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)) | (1 << (EParser.DOLLAR_IDENTIFIER - 132)) | (1 << (EParser.TEXT_LITERAL - 132)) | (1 << (EParser.INTEGER_LITERAL - 132)) | (1 << (EParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2293 
                localctx.args = self.csharp_arguments(0)


            self.state = 2296
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_argumentsContext)
            super(EParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_argumentsContext)
            super(EParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(EParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 404
        self.enterRecursionRule(localctx, 404, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2299 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,193,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2301
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2302
                    self.match(EParser.COMMA)
                    self.state = 2303 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,193,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = EParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2309
            self.match(EParser.LBRAK)
            self.state = 2310 
            localctx.exp = self.csharp_expression(0)
            self.state = 2311
            self.match(EParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = EParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2313
            self.match(EParser.LPAR)
            self.state = 2314 
            localctx.exp = self.csharp_expression(0)
            self.state = 2315
            self.match(EParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(EParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(EParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(EParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 410
        self.enterRecursionRule(localctx, 410, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2320
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2318
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2319 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2322
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2323
                    self.match(EParser.DOT)
                    self.state = 2324 
                    localctx.name = self.csharp_identifier() 
                self.state = 2329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(EParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(EParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(EParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(EParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_literal_expressionContext)
            super(EParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(EParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = EParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_csharp_literal_expression)
        try:
            self.state = 2335
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2330
                self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2331
                self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2332
                self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2333
                self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2334
                self.match(EParser.CHAR_LITERAL)

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
            super(EParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(EParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(EParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(EParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def WRITE(self):
            return self.getToken(EParser.WRITE, 0)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def getRuleIndex(self):
            return EParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = EParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2337
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (EParser.READ - 132)) | (1 << (EParser.TEST - 132)) | (1 << (EParser.WRITE - 132)) | (1 << (EParser.SYMBOL_IDENTIFIER - 132)) | (1 << (EParser.TYPE_IDENTIFIER - 132)) | (1 << (EParser.VARIABLE_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
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
        self._predicates[16] = self.native_category_binding_list_sempred
        self._predicates[37] = self.else_if_statement_list_sempred
        self._predicates[43] = self.expression_sempred
        self._predicates[44] = self.unresolved_expression_sempred
        self._predicates[45] = self.unresolved_selector_sempred
        self._predicates[47] = self.invocation_trailer_sempred
        self._predicates[48] = self.instance_expression_sempred
        self._predicates[49] = self.instance_selector_sempred
        self._predicates[58] = self.argument_assignment_list_sempred
        self._predicates[59] = self.with_argument_assignment_list_sempred
        self._predicates[62] = self.child_instance_sempred
        self._predicates[82] = self.typedef_sempred
        self._predicates[102] = self.any_type_sempred
        self._predicates[139] = self.assignable_instance_sempred
        self._predicates[140] = self.is_expression_sempred
        self._predicates[146] = self.new_token_sempred
        self._predicates[147] = self.key_token_sempred
        self._predicates[148] = self.module_token_sempred
        self._predicates[149] = self.value_token_sempred
        self._predicates[150] = self.symbols_token_sempred
        self._predicates[157] = self.javascript_expression_sempred
        self._predicates[163] = self.javascript_arguments_sempred
        self._predicates[170] = self.python_expression_sempred
        self._predicates[175] = self.python_ordinal_argument_list_sempred
        self._predicates[176] = self.python_named_argument_list_sempred
        self._predicates[178] = self.python_identifier_expression_sempred
        self._predicates[182] = self.java_expression_sempred
        self._predicates[188] = self.java_arguments_sempred
        self._predicates[191] = self.java_identifier_expression_sempred
        self._predicates[192] = self.java_class_identifier_expression_sempred
        self._predicates[196] = self.csharp_expression_sempred
        self._predicates[202] = self.csharp_arguments_sempred
        self._predicates[205] = self.csharp_identifier_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 40)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 39)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 38)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 37)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 8)
         

    def unresolved_expression_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.precpred(self._ctx, 1)
         

    def unresolved_selector_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.wasNot(EParser.WS)
         

    def invocation_trailer_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.willBe(EParser.LF)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.wasNot(EParser.WS)
         

            if predIndex == 35:
                return self.wasNot(EParser.WS)
         

            if predIndex == 36:
                return self.wasNot(EParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.was(EParser.WS)
         

    def with_argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.wasNot(EParser.WS)
         

            if predIndex == 40:
                return self.wasNot(EParser.WS)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 42:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         



