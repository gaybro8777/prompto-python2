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
        buf.write(u"\u009b\u0877\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0188\n\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\5\2\u018f\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u01ae\n\5\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u01b7\n\6\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\5\7\u01bf\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\5\7\u01ca\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write(u"\5\7\u01d3\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\5\b\u01e3\n\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\5\b\u01ec\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u01f3")
        buf.write(u"\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write(u"\u0200\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\3\r\5\r\u0227\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\5\r\u0235\n\r\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0244")
        buf.write(u"\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u0252\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\7\20\u0264\n\20\f\20\16\20\u0267\13\20\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0273\n")
        buf.write(u"\21\5\21\u0275\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\5\22\u0280\n\22\3\22\3\22\3\22\5\22\u0285")
        buf.write(u"\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u028f")
        buf.write(u"\n\23\3\23\3\23\3\23\5\23\u0294\n\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\5\24\u02a5\n\24\3\24\3\24\3\24\5\24\u02aa\n\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\5\25\u02c6\n\25\3\26\3\26\3")
        buf.write(u"\27\3\27\3\27\5\27\u02cd\n\27\3\30\3\30\3\30\5\30\u02d2")
        buf.write(u"\n\30\3\30\3\30\5\30\u02d6\n\30\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\5\31\u02e7\n\31\3\32\3\32\5\32\u02eb\n\32\3\32\5\32")
        buf.write(u"\u02ee\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\5\35\u030f\n\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\5\36\u0322\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0329")
        buf.write(u"\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write(u"\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\5\"\u034b\n\"\3\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\5\"\u0354\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u0369\n#\f#\16#\u036c")
        buf.write(u"\13#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u037b")
        buf.write(u"\n%\3%\3%\3%\5%\u0380\n%\3%\3%\3%\3%\3%\3%\5%\u0388\n")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\3%\5%\u0391\n%\3%\3%\3&\3&\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u03a8")
        buf.write(u"\n&\3\'\3\'\5\'\u03ac\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5")
        buf.write(u"(\u03c8\n(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7(\u0428\n(\f(\16(\u042b")
        buf.write(u"\13(\3)\3)\3)\3)\3)\7)\u0432\n)\f)\16)\u0435\13)\3*\3")
        buf.write(u"*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3-\3-\3-\3-\3-\7-\u0447")
        buf.write(u"\n-\f-\16-\u044a\13-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\5.\u0459\n.\3/\3/\3\60\5\60\u045e\n\60\3\60\3")
        buf.write(u"\60\3\60\3\60\5\60\u0464\n\60\3\60\3\60\3\60\5\60\u0469")
        buf.write(u"\n\60\5\60\u046b\n\60\3\60\5\60\u046e\n\60\3\60\3\60")
        buf.write(u"\3\60\3\60\5\60\u0474\n\60\5\60\u0476\n\60\5\60\u0478")
        buf.write(u"\n\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write(u"\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0496\n")
        buf.write(u"\65\3\66\3\66\3\66\3\66\3\66\5\66\u049d\n\66\5\66\u049f")
        buf.write(u"\n\66\3\66\3\66\3\66\5\66\u04a4\n\66\5\66\u04a6\n\66")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u04af\n\67\f")
        buf.write(u"\67\16\67\u04b2\13\67\38\38\38\38\39\39\39\39\3:\3:\3")
        buf.write(u":\3:\3:\3:\3:\3:\5:\u04c4\n:\3;\3;\3;\3;\3<\7<\u04cb")
        buf.write(u"\n<\f<\16<\u04ce\13<\3=\6=\u04d1\n=\r=\16=\u04d2\3>\6")
        buf.write(u">\u04d6\n>\r>\16>\u04d7\3>\3>\3?\7?\u04dd\n?\f?\16?\u04e0")
        buf.write(u"\13?\3?\3?\3@\3@\3A\5A\u04e7\nA\3A\3A\3A\3B\3B\3B\3B")
        buf.write(u"\3B\3B\3B\7B\u04f3\nB\fB\16B\u04f6\13B\3C\3C\3C\3C\3")
        buf.write(u"C\5C\u04fd\nC\3D\3D\3E\3E\5E\u0503\nE\3F\3F\3F\3F\3F")
        buf.write(u"\3F\3F\7F\u050c\nF\fF\16F\u050f\13F\3G\3G\3G\3G\3G\3")
        buf.write(u"G\3G\7G\u0518\nG\fG\16G\u051b\13G\3H\3H\3H\3H\3H\3H\7")
        buf.write(u"H\u0523\nH\fH\16H\u0526\13H\3I\3I\3I\3I\3I\3I\3I\3I\3")
        buf.write(u"I\3I\5I\u0532\nI\3J\3J\5J\u0536\nJ\3J\3J\3K\3K\5K\u053c")
        buf.write(u"\nK\3K\3K\3L\3L\3L\3L\3L\3L\7L\u0546\nL\fL\16L\u0549")
        buf.write(u"\13L\3M\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N")
        buf.write(u"\3N\7N\u055c\nN\fN\16N\u055f\13N\3O\3O\5O\u0563\nO\3")
        buf.write(u"P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u056f\nP\3Q\3Q\3R\3R")
        buf.write(u"\3S\3S\3T\3T\3T\5T\u057a\nT\3U\3U\3U\3U\3U\3U\7U\u0582")
        buf.write(u"\nU\fU\16U\u0585\13U\3V\3V\5V\u0589\nV\3W\3W\3W\5W\u058e")
        buf.write(u"\nW\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3[\3[\3[\3[\7[\u059c\n[\f")
        buf.write(u"[\16[\u059f\13[\3\\\3\\\5\\\u05a3\n\\\3\\\5\\\u05a6\n")
        buf.write(u"\\\3]\3]\5]\u05aa\n]\3^\3^\3^\5^\u05af\n^\3_\3_\3_\3")
        buf.write(u"`\3`\5`\u05b6\n`\3a\3a\3a\3a\3a\3a\3a\3a\3a\7a\u05c1")
        buf.write(u"\na\fa\16a\u05c4\13a\3b\3b\3b\3b\3b\3b\3b\7b\u05cd\n")
        buf.write(u"b\fb\16b\u05d0\13b\3c\3c\3c\3c\3c\5c\u05d7\nc\3d\3d\3")
        buf.write(u"d\3d\3d\3d\3d\7d\u05e0\nd\fd\16d\u05e3\13d\3e\3e\5e\u05e7")
        buf.write(u"\ne\3f\3f\3f\3f\3f\3f\3f\3f\3f\3f\5f\u05f3\nf\3g\3g\5")
        buf.write(u"g\u05f7\ng\3h\3h\3h\3h\3h\3h\7h\u05ff\nh\fh\16h\u0602")
        buf.write(u"\13h\3i\3i\3i\3j\3j\5j\u0609\nj\3k\3k\3k\3k\5k\u060f")
        buf.write(u"\nk\3k\3k\3k\7k\u0614\nk\fk\16k\u0617\13k\3k\3k\5k\u061b")
        buf.write(u"\nk\3l\3l\3l\3l\3l\3l\7l\u0623\nl\fl\16l\u0626\13l\3")
        buf.write(u"m\3m\3m\3m\5m\u062c\nm\3n\3n\3n\3n\3n\3n\3n\7n\u0635")
        buf.write(u"\nn\fn\16n\u0638\13n\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\5")
        buf.write(u"o\u0644\no\3p\3p\5p\u0648\np\3p\5p\u064b\np\3q\3q\5q")
        buf.write(u"\u064f\nq\3q\5q\u0652\nq\3r\3r\3r\3r\3r\3r\3r\7r\u065b")
        buf.write(u"\nr\fr\16r\u065e\13r\3s\3s\3s\3s\3s\3s\3s\7s\u0667\n")
        buf.write(u"s\fs\16s\u066a\13s\3t\3t\3t\3t\3t\3t\3t\7t\u0673\nt\f")
        buf.write(u"t\16t\u0676\13t\3u\3u\3u\3u\3u\3u\3u\7u\u067f\nu\fu\16")
        buf.write(u"u\u0682\13u\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write(u"v\5v\u0692\nv\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w")
        buf.write(u"\5w\u06a1\nw\3x\3x\3x\3x\3x\3x\7x\u06a9\nx\fx\16x\u06ac")
        buf.write(u"\13x\3y\3y\3y\3y\5y\u06b2\ny\3z\3z\3{\3{\3{\3{\3|\3|")
        buf.write(u"\5|\u06bc\n|\3}\3}\3}\3}\3}\5}\u06c3\n}\3~\3~\5~\u06c7")
        buf.write(u"\n~\3~\3~\3\177\3\177\5\177\u06cd\n\177\3\177\3\177\3")
        buf.write(u"\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\7\u0080")
        buf.write(u"\u06d7\n\u0080\f\u0080\16\u0080\u06da\13\u0080\3\u0081")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\7\u0081\u06e2")
        buf.write(u"\n\u0081\f\u0081\16\u0081\u06e5\13\u0081\3\u0082\3\u0082")
        buf.write(u"\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083\u06f4\n\u0083")
        buf.write(u"\3\u0084\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\7\u0085\u06ff\n\u0085\f\u0085\16\u0085")
        buf.write(u"\u0702\13\u0085\3\u0086\3\u0086\3\u0086\3\u0086\5\u0086")
        buf.write(u"\u0708\n\u0086\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\5\u0087\u0710\n\u0087\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0089\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\3\u008b")
        buf.write(u"\3\u008b\3\u008c\3\u008c\3\u008d\3\u008d\3\u008e\3\u008e")
        buf.write(u"\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write(u"\3\u0090\3\u0090\5\u0090\u072c\n\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0091\7\u0091\u0733\n\u0091\f\u0091")
        buf.write(u"\16\u0091\u0736\13\u0091\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\3\u0092\5\u0092\u073e\n\u0092\3\u0093\3\u0093")
        buf.write(u"\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\5\u0094\u0747")
        buf.write(u"\n\u0094\3\u0095\3\u0095\3\u0095\5\u0095\u074c\n\u0095")
        buf.write(u"\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write(u"\3\u0096\7\u0096\u0756\n\u0096\f\u0096\16\u0096\u0759")
        buf.write(u"\13\u0096\3\u0097\3\u0097\3\u0097\3\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0098\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a\3\u009a")
        buf.write(u"\3\u009a\3\u009a\5\u009a\u076a\n\u009a\3\u009b\3\u009b")
        buf.write(u"\3\u009c\3\u009c\3\u009c\5\u009c\u0771\n\u009c\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009d\7\u009d\u0778\n\u009d")
        buf.write(u"\f\u009d\16\u009d\u077b\13\u009d\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\5\u009e\u0781\n\u009e\3\u009f\3\u009f\3\u009f")
        buf.write(u"\3\u009f\3\u009f\3\u009f\5\u009f\u0789\n\u009f\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a0\5\u00a0\u078e\n\u00a0\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\5\u00a1")
        buf.write(u"\u0798\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a2\7\u00a2\u07a0\n\u00a2\f\u00a2\16\u00a2\u07a3")
        buf.write(u"\13\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\7\u00a3\u07b0")
        buf.write(u"\n\u00a3\f\u00a3\16\u00a3\u07b3\13\u00a3\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u07bc")
        buf.write(u"\n\u00a5\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u07c1\n\u00a5")
        buf.write(u"\f\u00a5\16\u00a5\u07c4\13\u00a5\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a6\5\u00a6\u07cb\n\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write(u"\5\u00a8\u07d6\n\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\7\u00a9\u07dd\n\u00a9\f\u00a9\16\u00a9\u07e0")
        buf.write(u"\13\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa\u07e6")
        buf.write(u"\n\u00aa\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac\5\u00ac")
        buf.write(u"\u07ed\n\u00ac\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u07f2")
        buf.write(u"\n\u00ad\3\u00ad\3\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\7\u00ae\u07fc\n\u00ae\f\u00ae\16\u00ae")
        buf.write(u"\u07ff\13\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\7\u00b1\u080f\n\u00b1\f\u00b1\16\u00b1")
        buf.write(u"\u0812\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\7\u00b2\u0819\n\u00b2\f\u00b2\16\u00b2\u081c\13\u00b2")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\5\u00b3\u0823")
        buf.write(u"\n\u00b3\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u082e\n\u00b5\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u0835\n\u00b6")
        buf.write(u"\f\u00b6\16\u00b6\u0838\13\u00b6\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\5\u00b7\u083e\n\u00b7\3\u00b8\3\u00b8\3\u00b9")
        buf.write(u"\3\u00b9\3\u00b9\5\u00b9\u0845\n\u00b9\3\u00ba\3\u00ba")
        buf.write(u"\3\u00ba\5\u00ba\u084a\n\u00ba\3\u00ba\3\u00ba\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u0854")
        buf.write(u"\n\u00bb\f\u00bb\16\u00bb\u0857\13\u00bb\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be")
        buf.write(u"\3\u00be\3\u00be\5\u00be\u0864\n\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00be\7\u00be\u0869\n\u00be\f\u00be\16\u00be\u086c")
        buf.write(u"\13\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf\5\u00bf")
        buf.write(u"\u0873\n\u00bf\3\u00c0\3\u00c0\3\u00c0\2*\36DNPXl\u0082")
        buf.write(u"\u008a\u008c\u008e\u0096\u009a\u00a8\u00b4\u00c0\u00c2")
        buf.write(u"\u00c6\u00d6\u00da\u00e2\u00e4\u00e6\u00e8\u00ee\u00fe")
        buf.write(u"\u0100\u0108\u0120\u012a\u0138\u0142\u0144\u0148\u0150")
        buf.write(u"\u015a\u0160\u0162\u016a\u0174\u017a\u00c1\2\4\6\b\n")
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
        buf.write(u"\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e\2\t")
        buf.write(u"\3\2!\"\4\2{{\u0081\u0081\4\2&&hh\b\2\63;vv\u0080\u0080")
        buf.write(u"\u0089\u0089\u008e\u0090\u0092\u0092\b\2\63;vv{{\u0080")
        buf.write(u"\u0081\u0089\u0089\u008e\u0090\7\2\63;vv\u0080\u0080")
        buf.write(u"\u0089\u0089\u008e\u0092\7\2\63;vv\u0080\u0080\u0089")
        buf.write(u"\u0089\u008e\u0090\u08de\2\u0180\3\2\2\2\4\u0196\3\2")
        buf.write(u"\2\2\6\u01a3\3\2\2\2\b\u01a9\3\2\2\2\n\u01af\3\2\2\2")
        buf.write(u"\f\u01b8\3\2\2\2\16\u01d4\3\2\2\2\20\u01f2\3\2\2\2\22")
        buf.write(u"\u01f4\3\2\2\2\24\u0207\3\2\2\2\26\u0210\3\2\2\2\30\u0219")
        buf.write(u"\3\2\2\2\32\u0236\3\2\2\2\34\u0253\3\2\2\2\36\u025c\3")
        buf.write(u"\2\2\2 \u0274\3\2\2\2\"\u0276\3\2\2\2$\u0286\3\2\2\2")
        buf.write(u"&\u029b\3\2\2\2(\u02b1\3\2\2\2*\u02c7\3\2\2\2,\u02c9")
        buf.write(u"\3\2\2\2.\u02ce\3\2\2\2\60\u02e6\3\2\2\2\62\u02ed\3\2")
        buf.write(u"\2\2\64\u02ef\3\2\2\2\66\u02f8\3\2\2\28\u0301\3\2\2\2")
        buf.write(u":\u0321\3\2\2\2<\u0323\3\2\2\2>\u0331\3\2\2\2@\u033a")
        buf.write(u"\3\2\2\2B\u0341\3\2\2\2D\u0355\3\2\2\2F\u036d\3\2\2\2")
        buf.write(u"H\u0370\3\2\2\2J\u03a7\3\2\2\2L\u03a9\3\2\2\2N\u03c7")
        buf.write(u"\3\2\2\2P\u042c\3\2\2\2R\u0436\3\2\2\2T\u043a\3\2\2\2")
        buf.write(u"V\u043f\3\2\2\2X\u0441\3\2\2\2Z\u0458\3\2\2\2\\\u045a")
        buf.write(u"\3\2\2\2^\u0477\3\2\2\2`\u0479\3\2\2\2b\u047d\3\2\2\2")
        buf.write(u"d\u0482\3\2\2\2f\u0486\3\2\2\2h\u048e\3\2\2\2j\u04a5")
        buf.write(u"\3\2\2\2l\u04a7\3\2\2\2n\u04b3\3\2\2\2p\u04b7\3\2\2\2")
        buf.write(u"r\u04c3\3\2\2\2t\u04c5\3\2\2\2v\u04cc\3\2\2\2x\u04d0")
        buf.write(u"\3\2\2\2z\u04d5\3\2\2\2|\u04de\3\2\2\2~\u04e3\3\2\2\2")
        buf.write(u"\u0080\u04e6\3\2\2\2\u0082\u04eb\3\2\2\2\u0084\u04fc")
        buf.write(u"\3\2\2\2\u0086\u04fe\3\2\2\2\u0088\u0502\3\2\2\2\u008a")
        buf.write(u"\u0504\3\2\2\2\u008c\u0510\3\2\2\2\u008e\u051c\3\2\2")
        buf.write(u"\2\u0090\u0531\3\2\2\2\u0092\u0533\3\2\2\2\u0094\u0539")
        buf.write(u"\3\2\2\2\u0096\u053f\3\2\2\2\u0098\u054a\3\2\2\2\u009a")
        buf.write(u"\u0550\3\2\2\2\u009c\u0562\3\2\2\2\u009e\u056e\3\2\2")
        buf.write(u"\2\u00a0\u0570\3\2\2\2\u00a2\u0572\3\2\2\2\u00a4\u0574")
        buf.write(u"\3\2\2\2\u00a6\u0579\3\2\2\2\u00a8\u057b\3\2\2\2\u00aa")
        buf.write(u"\u0588\3\2\2\2\u00ac\u058d\3\2\2\2\u00ae\u058f\3\2\2")
        buf.write(u"\2\u00b0\u0591\3\2\2\2\u00b2\u0593\3\2\2\2\u00b4\u0595")
        buf.write(u"\3\2\2\2\u00b6\u05a5\3\2\2\2\u00b8\u05a9\3\2\2\2\u00ba")
        buf.write(u"\u05ab\3\2\2\2\u00bc\u05b0\3\2\2\2\u00be\u05b5\3\2\2")
        buf.write(u"\2\u00c0\u05b7\3\2\2\2\u00c2\u05c5\3\2\2\2\u00c4\u05d6")
        buf.write(u"\3\2\2\2\u00c6\u05d8\3\2\2\2\u00c8\u05e6\3\2\2\2\u00ca")
        buf.write(u"\u05f2\3\2\2\2\u00cc\u05f4\3\2\2\2\u00ce\u05f8\3\2\2")
        buf.write(u"\2\u00d0\u0603\3\2\2\2\u00d2\u0606\3\2\2\2\u00d4\u060a")
        buf.write(u"\3\2\2\2\u00d6\u061c\3\2\2\2\u00d8\u062b\3\2\2\2\u00da")
        buf.write(u"\u062d\3\2\2\2\u00dc\u0643\3\2\2\2\u00de\u0645\3\2\2")
        buf.write(u"\2\u00e0\u064c\3\2\2\2\u00e2\u0653\3\2\2\2\u00e4\u065f")
        buf.write(u"\3\2\2\2\u00e6\u066b\3\2\2\2\u00e8\u0677\3\2\2\2\u00ea")
        buf.write(u"\u0691\3\2\2\2\u00ec\u06a0\3\2\2\2\u00ee\u06a2\3\2\2")
        buf.write(u"\2\u00f0\u06b1\3\2\2\2\u00f2\u06b3\3\2\2\2\u00f4\u06b5")
        buf.write(u"\3\2\2\2\u00f6\u06bb\3\2\2\2\u00f8\u06c2\3\2\2\2\u00fa")
        buf.write(u"\u06c4\3\2\2\2\u00fc\u06ca\3\2\2\2\u00fe\u06d0\3\2\2")
        buf.write(u"\2\u0100\u06db\3\2\2\2\u0102\u06e6\3\2\2\2\u0104\u06f3")
        buf.write(u"\3\2\2\2\u0106\u06f5\3\2\2\2\u0108\u06f9\3\2\2\2\u010a")
        buf.write(u"\u0707\3\2\2\2\u010c\u070f\3\2\2\2\u010e\u0711\3\2\2")
        buf.write(u"\2\u0110\u0714\3\2\2\2\u0112\u0717\3\2\2\2\u0114\u071a")
        buf.write(u"\3\2\2\2\u0116\u071c\3\2\2\2\u0118\u071e\3\2\2\2\u011a")
        buf.write(u"\u0720\3\2\2\2\u011c\u0722\3\2\2\2\u011e\u072b\3\2\2")
        buf.write(u"\2\u0120\u072d\3\2\2\2\u0122\u073d\3\2\2\2\u0124\u073f")
        buf.write(u"\3\2\2\2\u0126\u0746\3\2\2\2\u0128\u0748\3\2\2\2\u012a")
        buf.write(u"\u074f\3\2\2\2\u012c\u075a\3\2\2\2\u012e\u075e\3\2\2")
        buf.write(u"\2\u0130\u0762\3\2\2\2\u0132\u0769\3\2\2\2\u0134\u076b")
        buf.write(u"\3\2\2\2\u0136\u0770\3\2\2\2\u0138\u0772\3\2\2\2\u013a")
        buf.write(u"\u0780\3\2\2\2\u013c\u0788\3\2\2\2\u013e\u078a\3\2\2")
        buf.write(u"\2\u0140\u0797\3\2\2\2\u0142\u0799\3\2\2\2\u0144\u07a4")
        buf.write(u"\3\2\2\2\u0146\u07b4\3\2\2\2\u0148\u07bb\3\2\2\2\u014a")
        buf.write(u"\u07ca\3\2\2\2\u014c\u07cc\3\2\2\2\u014e\u07d5\3\2\2")
        buf.write(u"\2\u0150\u07d7\3\2\2\2\u0152\u07e5\3\2\2\2\u0154\u07e7")
        buf.write(u"\3\2\2\2\u0156\u07ec\3\2\2\2\u0158\u07ee\3\2\2\2\u015a")
        buf.write(u"\u07f5\3\2\2\2\u015c\u0800\3\2\2\2\u015e\u0804\3\2\2")
        buf.write(u"\2\u0160\u0808\3\2\2\2\u0162\u0813\3\2\2\2\u0164\u0822")
        buf.write(u"\3\2\2\2\u0166\u0824\3\2\2\2\u0168\u082d\3\2\2\2\u016a")
        buf.write(u"\u082f\3\2\2\2\u016c\u083d\3\2\2\2\u016e\u083f\3\2\2")
        buf.write(u"\2\u0170\u0844\3\2\2\2\u0172\u0846\3\2\2\2\u0174\u084d")
        buf.write(u"\3\2\2\2\u0176\u0858\3\2\2\2\u0178\u085c\3\2\2\2\u017a")
        buf.write(u"\u0863\3\2\2\2\u017c\u0872\3\2\2\2\u017e\u0874\3\2\2")
        buf.write(u"\2\u0180\u0181\7Q\2\2\u0181\u0182\5\u00b0Y\2\u0182\u0183")
        buf.write(u"\7D\2\2\u0183\u0184\7\20\2\2\u0184\u0187\7W\2\2\u0185")
        buf.write(u"\u0188\7K\2\2\u0186\u0188\5\u00b0Y\2\u0187\u0185\3\2")
        buf.write(u"\2\2\u0187\u0186\3\2\2\2\u0188\u018e\3\2\2\2\u0189\u018a")
        buf.write(u"\5 \21\2\u018a\u018b\7\22\2\2\u018b\u018c\7B\2\2\u018c")
        buf.write(u"\u018f\3\2\2\2\u018d\u018f\7\u0085\2\2\u018e\u0189\3")
        buf.write(u"\2\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write(u"\u0191\5\u0112\u008a\2\u0191\u0192\7\20\2\2\u0192\u0193")
        buf.write(u"\5z>\2\u0193\u0194\5\u008cG\2\u0194\u0195\5|?\2\u0195")
        buf.write(u"\3\3\2\2\2\u0196\u0197\7Q\2\2\u0197\u0198\5\u00b0Y\2")
        buf.write(u"\u0198\u0199\7D\2\2\u0199\u019a\7\20\2\2\u019a\u019b")
        buf.write(u"\7W\2\2\u019b\u019c\5\u009eP\2\u019c\u019d\7\u0085\2")
        buf.write(u"\2\u019d\u019e\5\u0112\u008a\2\u019e\u019f\7\20\2\2\u019f")
        buf.write(u"\u01a0\5z>\2\u01a0\u01a1\5\u008aF\2\u01a1\u01a2\5|?\2")
        buf.write(u"\u01a2\5\3\2\2\2\u01a3\u01a4\5\u00b2Z\2\u01a4\u01a5\7")
        buf.write(u"\u0085\2\2\u01a5\u01a6\5N(\2\u01a6\u01a7\7D\2\2\u01a7")
        buf.write(u"\u01a8\5\u0110\u0089\2\u01a8\7\3\2\2\2\u01a9\u01aa\5")
        buf.write(u"\u00b2Z\2\u01aa\u01ad\5l\67\2\u01ab\u01ac\7B\2\2\u01ac")
        buf.write(u"\u01ae\5n8\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write(u"\u01ae\t\3\2\2\2\u01af\u01b0\7Q\2\2\u01b0\u01b1\5\u00ae")
        buf.write(u"X\2\u01b1\u01b2\7D\2\2\u01b2\u01b3\7\20\2\2\u01b3\u01b4")
        buf.write(u"\5\u009aN\2\u01b4\u01b6\7F\2\2\u01b5\u01b7\5\u0090I\2")
        buf.write(u"\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\13\3\2")
        buf.write(u"\2\2\u01b8\u01b9\7Q\2\2\u01b9\u01ba\5\u00b0Y\2\u01ba")
        buf.write(u"\u01bb\7D\2\2\u01bb\u01be\7\20\2\2\u01bc\u01bf\7K\2\2")
        buf.write(u"\u01bd\u01bf\5\20\t\2\u01be\u01bc\3\2\2\2\u01be\u01bd")
        buf.write(u"\3\2\2\2\u01bf\u01d2\3\2\2\2\u01c0\u01c9\5 \21\2\u01c1")
        buf.write(u"\u01c2\7\22\2\2\u01c2\u01c3\7B\2\2\u01c3\u01c4\7g\2\2")
        buf.write(u"\u01c4\u01c5\7\20\2\2\u01c5\u01c6\5z>\2\u01c6\u01c7\5")
        buf.write(u"\u00c2b\2\u01c7\u01c8\5|?\2\u01c8\u01ca\3\2\2\2\u01c9")
        buf.write(u"\u01c1\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01d3\3\2\2")
        buf.write(u"\2\u01cb\u01cc\7\u0085\2\2\u01cc\u01cd\7g\2\2\u01cd\u01ce")
        buf.write(u"\7\20\2\2\u01ce\u01cf\5z>\2\u01cf\u01d0\5\u00c2b\2\u01d0")
        buf.write(u"\u01d1\5|?\2\u01d1\u01d3\3\2\2\2\u01d2\u01c0\3\2\2\2")
        buf.write(u"\u01d2\u01cb\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\r\3\2")
        buf.write(u"\2\2\u01d4\u01d5\7Q\2\2\u01d5\u01d6\5\u00b0Y\2\u01d6")
        buf.write(u"\u01d7\7D\2\2\u01d7\u01d8\7\20\2\2\u01d8\u01eb\7}\2\2")
        buf.write(u"\u01d9\u01e2\5 \21\2\u01da\u01db\7\22\2\2\u01db\u01dc")
        buf.write(u"\7B\2\2\u01dc\u01dd\7g\2\2\u01dd\u01de\7\20\2\2\u01de")
        buf.write(u"\u01df\5z>\2\u01df\u01e0\5\u00c2b\2\u01e0\u01e1\5|?\2")
        buf.write(u"\u01e1\u01e3\3\2\2\2\u01e2\u01da\3\2\2\2\u01e2\u01e3")
        buf.write(u"\3\2\2\2\u01e3\u01ec\3\2\2\2\u01e4\u01e5\7\u0085\2\2")
        buf.write(u"\u01e5\u01e6\7g\2\2\u01e6\u01e7\7\20\2\2\u01e7\u01e8")
        buf.write(u"\5z>\2\u01e8\u01e9\5\u00c2b\2\u01e9\u01ea\5|?\2\u01ea")
        buf.write(u"\u01ec\3\2\2\2\u01eb\u01d9\3\2\2\2\u01eb\u01e4\3\2\2")
        buf.write(u"\2\u01eb\u01ec\3\2\2\2\u01ec\17\3\2\2\2\u01ed\u01f3\5")
        buf.write(u"\u00a8U\2\u01ee\u01ef\5\u00a8U\2\u01ef\u01f0\7B\2\2\u01f0")
        buf.write(u"\u01f1\5\u00b0Y\2\u01f1\u01f3\3\2\2\2\u01f2\u01ed\3\2")
        buf.write(u"\2\2\u01f2\u01ee\3\2\2\2\u01f3\21\3\2\2\2\u01f4\u01f5")
        buf.write(u"\7Q\2\2\u01f5\u01f6\5\u010c\u0087\2\u01f6\u01f7\7D\2")
        buf.write(u"\2\u01f7\u01f8\7\20\2\2\u01f8\u01f9\7q\2\2\u01f9\u01fa")
        buf.write(u"\7w\2\2\u01fa\u01fb\7\20\2\2\u01fb\u01ff\5\u00b8]\2\u01fc")
        buf.write(u"\u01fd\7z\2\2\u01fd\u01fe\7\20\2\2\u01fe\u0200\5\u009a")
        buf.write(u"N\2\u01ff\u01fc\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201")
        buf.write(u"\3\2\2\2\u0201\u0202\7S\2\2\u0202\u0203\7\20\2\2\u0203")
        buf.write(u"\u0204\5z>\2\u0204\u0205\5\u00e2r\2\u0205\u0206\5|?\2")
        buf.write(u"\u0206\23\3\2\2\2\u0207\u0208\7Q\2\2\u0208\u0209\5\u00ae")
        buf.write(u"X\2\u0209\u020a\7|\2\2\u020a\u020b\7S\2\2\u020b\u020c")
        buf.write(u"\7\20\2\2\u020c\u020d\5z>\2\u020d\u020e\5\u00e2r\2\u020e")
        buf.write(u"\u020f\5|?\2\u020f\25\3\2\2\2\u0210\u0211\7Q\2\2\u0211")
        buf.write(u"\u0212\5\u00aeX\2\u0212\u0213\7`\2\2\u0213\u0214\7S\2")
        buf.write(u"\2\u0214\u0215\7\20\2\2\u0215\u0216\5z>\2\u0216\u0217")
        buf.write(u"\5\u00e2r\2\u0217\u0218\5|?\2\u0218\27\3\2\2\2\u0219")
        buf.write(u"\u021a\7Q\2\2\u021a\u021b\5\u00b0Y\2\u021b\u021c\7D\2")
        buf.write(u"\2\u021c\u021d\7\20\2\2\u021d\u021e\7j\2\2\u021e\u0226")
        buf.write(u"\7K\2\2\u021f\u0220\5 \21\2\u0220\u0221\7\22\2\2\u0221")
        buf.write(u"\u0222\7B\2\2\u0222\u0223\7H\2\2\u0223\u0227\3\2\2\2")
        buf.write(u"\u0224\u0225\7\u0085\2\2\u0225\u0227\7H\2\2\u0226\u021f")
        buf.write(u"\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write(u"\u0229\7\20\2\2\u0229\u022a\5z>\2\u022a\u022b\5\34\17")
        buf.write(u"\2\u022b\u0234\5|?\2\u022c\u022d\5x=\2\u022d\u022e\7")
        buf.write(u"B\2\2\u022e\u022f\7g\2\2\u022f\u0230\7\20\2\2\u0230\u0231")
        buf.write(u"\5z>\2\u0231\u0232\5\u00c6d\2\u0232\u0233\5|?\2\u0233")
        buf.write(u"\u0235\3\2\2\2\u0234\u022c\3\2\2\2\u0234\u0235\3\2\2")
        buf.write(u"\2\u0235\31\3\2\2\2\u0236\u0237\7Q\2\2\u0237\u0238\5")
        buf.write(u"\u00b0Y\2\u0238\u0239\7D\2\2\u0239\u023a\7\20\2\2\u023a")
        buf.write(u"\u023b\7j\2\2\u023b\u0243\7x\2\2\u023c\u023d\5 \21\2")
        buf.write(u"\u023d\u023e\7\22\2\2\u023e\u023f\7B\2\2\u023f\u0240")
        buf.write(u"\7H\2\2\u0240\u0244\3\2\2\2\u0241\u0242\7\u0085\2\2\u0242")
        buf.write(u"\u0244\7H\2\2\u0243\u023c\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write(u"\u0244\u0245\3\2\2\2\u0245\u0246\7\20\2\2\u0246\u0247")
        buf.write(u"\5z>\2\u0247\u0248\5\34\17\2\u0248\u0251\5|?\2\u0249")
        buf.write(u"\u024a\5x=\2\u024a\u024b\7B\2\2\u024b\u024c\7g\2\2\u024c")
        buf.write(u"\u024d\7\20\2\2\u024d\u024e\5z>\2\u024e\u024f\5\u00c6")
        buf.write(u"d\2\u024f\u0250\5|?\2\u0250\u0252\3\2\2\2\u0251\u0249")
        buf.write(u"\3\2\2\2\u0251\u0252\3\2\2\2\u0252\33\3\2\2\2\u0253\u0254")
        buf.write(u"\7Q\2\2\u0254\u0255\7K\2\2\u0255\u0256\7H\2\2\u0256\u0257")
        buf.write(u"\7D\2\2\u0257\u0258\7\20\2\2\u0258\u0259\5z>\2\u0259")
        buf.write(u"\u025a\5\36\20\2\u025a\u025b\5|?\2\u025b\35\3\2\2\2\u025c")
        buf.write(u"\u025d\b\20\1\2\u025d\u025e\5\u00caf\2\u025e\u0265\3")
        buf.write(u"\2\2\2\u025f\u0260\f\3\2\2\u0260\u0261\5x=\2\u0261\u0262")
        buf.write(u"\5\u00caf\2\u0262\u0264\3\2\2\2\u0263\u025f\3\2\2\2\u0264")
        buf.write(u"\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2")
        buf.write(u"\2\u0266\37\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u0269\7")
        buf.write(u"\u0085\2\2\u0269\u026a\7F\2\2\u026a\u026b\7\20\2\2\u026b")
        buf.write(u"\u0275\5\u00aeX\2\u026c\u026d\7\u0085\2\2\u026d\u026e")
        buf.write(u"\7G\2\2\u026e\u026f\7\20\2\2\u026f\u0272\5\u00d6l\2\u0270")
        buf.write(u"\u0271\7B\2\2\u0271\u0273\5\u00aeX\2\u0272\u0270\3\2")
        buf.write(u"\2\2\u0272\u0273\3\2\2\2\u0273\u0275\3\2\2\2\u0274\u0268")
        buf.write(u"\3\2\2\2\u0274\u026c\3\2\2\2\u0275!\3\2\2\2\u0276\u0277")
        buf.write(u"\7Q\2\2\u0277\u0278\5\u00aaV\2\u0278\u0279\7D\2\2\u0279")
        buf.write(u"\u027a\7\20\2\2\u027a\u027b\7?\2\2\u027b\u027f\7f\2\2")
        buf.write(u"\u027c\u027d\7w\2\2\u027d\u027e\7\20\2\2\u027e\u0280")
        buf.write(u"\5,\27\2\u027f\u027c\3\2\2\2\u027f\u0280\3\2\2\2\u0280")
        buf.write(u"\u0284\3\2\2\2\u0281\u0282\7z\2\2\u0282\u0283\7\20\2")
        buf.write(u"\2\u0283\u0285\5\u009aN\2\u0284\u0281\3\2\2\2\u0284\u0285")
        buf.write(u"\3\2\2\2\u0285#\3\2\2\2\u0286\u0287\7Q\2\2\u0287\u0288")
        buf.write(u"\5\u00aaV\2\u0288\u0289\7D\2\2\u0289\u028a\7\20\2\2\u028a")
        buf.write(u"\u028e\7f\2\2\u028b\u028c\7w\2\2\u028c\u028d\7\20\2\2")
        buf.write(u"\u028d\u028f\5,\27\2\u028e\u028b\3\2\2\2\u028e\u028f")
        buf.write(u"\3\2\2\2\u028f\u0293\3\2\2\2\u0290\u0291\7z\2\2\u0291")
        buf.write(u"\u0292\7\20\2\2\u0292\u0294\5\u009aN\2\u0293\u0290\3")
        buf.write(u"\2\2\2\u0293\u0294\3\2\2\2\u0294\u0295\3\2\2\2\u0295")
        buf.write(u"\u0296\7S\2\2\u0296\u0297\7\20\2\2\u0297\u0298\5z>\2")
        buf.write(u"\u0298\u0299\5\u00e2r\2\u0299\u029a\5|?\2\u029a%\3\2")
        buf.write(u"\2\2\u029b\u029c\7Q\2\2\u029c\u029d\5\u00aaV\2\u029d")
        buf.write(u"\u029e\7D\2\2\u029e\u029f\7\20\2\2\u029f\u02a0\7j\2\2")
        buf.write(u"\u02a0\u02a4\7f\2\2\u02a1\u02a2\7w\2\2\u02a2\u02a3\7")
        buf.write(u"\20\2\2\u02a3\u02a5\5,\27\2\u02a4\u02a1\3\2\2\2\u02a4")
        buf.write(u"\u02a5\3\2\2\2\u02a5\u02a9\3\2\2\2\u02a6\u02a7\7z\2\2")
        buf.write(u"\u02a7\u02a8\7\20\2\2\u02a8\u02aa\5\u00be`\2\u02a9\u02a6")
        buf.write(u"\3\2\2\2\u02a9\u02aa\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab")
        buf.write(u"\u02ac\7S\2\2\u02ac\u02ad\7\20\2\2\u02ad\u02ae\5z>\2")
        buf.write(u"\u02ae\u02af\5\u00dan\2\u02af\u02b0\5|?\2\u02b0\'\3\2")
        buf.write(u"\2\2\u02b1\u02b2\7Q\2\2\u02b2\u02b3\7\u0093\2\2\u02b3")
        buf.write(u"\u02b4\7D\2\2\u02b4\u02b5\7\20\2\2\u02b5\u02b6\7\u0080")
        buf.write(u"\2\2\u02b6\u02b7\7f\2\2\u02b7\u02b8\7S\2\2\u02b8\u02b9")
        buf.write(u"\7\20\2\2\u02b9\u02ba\5z>\2\u02ba\u02bb\5\u00e2r\2\u02bb")
        buf.write(u"\u02bc\5|?\2\u02bc\u02bd\5x=\2\u02bd\u02be\7B\2\2\u02be")
        buf.write(u"\u02bf\7Z\2\2\u02bf\u02c5\7\20\2\2\u02c0\u02c1\5z>\2")
        buf.write(u"\u02c1\u02c2\5\u00e4s\2\u02c2\u02c3\5|?\2\u02c3\u02c6")
        buf.write(u"\3\2\2\2\u02c4\u02c6\5\u00b2Z\2\u02c5\u02c0\3\2\2\2\u02c5")
        buf.write(u"\u02c4\3\2\2\2\u02c6)\3\2\2\2\u02c7\u02c8\5N(\2\u02c8")
        buf.write(u"+\3\2\2\2\u02c9\u02cc\5\u00b4[\2\u02ca\u02cb\7B\2\2\u02cb")
        buf.write(u"\u02cd\5\u00b6\\\2\u02cc\u02ca\3\2\2\2\u02cc\u02cd\3")
        buf.write(u"\2\2\2\u02cd-\3\2\2\2\u02ce\u02cf\5\u00be`\2\u02cf\u02d1")
        buf.write(u"\5\u00aeX\2\u02d0\u02d2\5 \21\2\u02d1\u02d0\3\2\2\2\u02d1")
        buf.write(u"\u02d2\3\2\2\2\u02d2\u02d5\3\2\2\2\u02d3\u02d4\7,\2\2")
        buf.write(u"\u02d4\u02d6\5\u00f6|\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6")
        buf.write(u"\3\2\2\2\u02d6/\3\2\2\2\u02d7\u02e7\5p9\2\u02d8\u02e7")
        buf.write(u"\5\62\32\2\u02d9\u02e7\5t;\2\u02da\u02e7\5L\'\2\u02db")
        buf.write(u"\u02e7\5B\"\2\u02dc\u02e7\58\35\2\u02dd\u02e7\5<\37\2")
        buf.write(u"\u02de\u02e7\5@!\2\u02df\u02e7\5> \2\u02e0\u02e7\5F$")
        buf.write(u"\2\u02e1\u02e7\5H%\2\u02e2\u02e7\5b\62\2\u02e3\u02e7")
        buf.write(u"\5\64\33\2\u02e4\u02e7\5\66\34\2\u02e5\u02e7\5$\23\2")
        buf.write(u"\u02e6\u02d7\3\2\2\2\u02e6\u02d8\3\2\2\2\u02e6\u02d9")
        buf.write(u"\3\2\2\2\u02e6\u02da\3\2\2\2\u02e6\u02db\3\2\2\2\u02e6")
        buf.write(u"\u02dc\3\2\2\2\u02e6\u02dd\3\2\2\2\u02e6\u02de\3\2\2")
        buf.write(u"\2\u02e6\u02df\3\2\2\2\u02e6\u02e0\3\2\2\2\u02e6\u02e1")
        buf.write(u"\3\2\2\2\u02e6\u02e2\3\2\2\2\u02e6\u02e3\3\2\2\2\u02e6")
        buf.write(u"\u02e4\3\2\2\2\u02e6\u02e5\3\2\2\2\u02e7\61\3\2\2\2\u02e8")
        buf.write(u"\u02ea\5P)\2\u02e9\u02eb\5j\66\2\u02ea\u02e9\3\2\2\2")
        buf.write(u"\u02ea\u02eb\3\2\2\2\u02eb\u02ee\3\2\2\2\u02ec\u02ee")
        buf.write(u"\5T+\2\u02ed\u02e8\3\2\2\2\u02ed\u02ec\3\2\2\2\u02ee")
        buf.write(u"\63\3\2\2\2\u02ef\u02f0\7\u0085\2\2\u02f0\u02f1\5\u0106")
        buf.write(u"\u0084\2\u02f1\u02f2\7\22\2\2\u02f2\u02f3\7R\2\2\u02f3")
        buf.write(u"\u02f4\7\20\2\2\u02f4\u02f5\5z>\2\u02f5\u02f6\5\u00e2")
        buf.write(u"r\2\u02f6\u02f7\5|?\2\u02f7\65\3\2\2\2\u02f8\u02f9\7")
        buf.write(u"\u0085\2\2\u02f9\u02fa\5\u00b0Y\2\u02fa\u02fb\7\22\2")
        buf.write(u"\2\u02fb\u02fc\7R\2\2\u02fc\u02fd\7\20\2\2\u02fd\u02fe")
        buf.write(u"\5z>\2\u02fe\u02ff\5\u00e2r\2\u02ff\u0300\5|?\2\u0300")
        buf.write(u"\67\3\2\2\2\u0301\u0302\7\177\2\2\u0302\u0303\7o\2\2")
        buf.write(u"\u0303\u0304\5N(\2\u0304\u0305\7\20\2\2\u0305\u0306\5")
        buf.write(u"z>\2\u0306\u030e\5\u00e6t\2\u0307\u0308\5x=\2\u0308\u0309")
        buf.write(u"\7s\2\2\u0309\u030a\7\20\2\2\u030a\u030b\5z>\2\u030b")
        buf.write(u"\u030c\5\u00e2r\2\u030c\u030d\5|?\2\u030d\u030f\3\2\2")
        buf.write(u"\2\u030e\u0307\3\2\2\2\u030e\u030f\3\2\2\2\u030f\u0310")
        buf.write(u"\3\2\2\2\u0310\u0311\5|?\2\u03119\3\2\2\2\u0312\u0313")
        buf.write(u"\7\u0086\2\2\u0313\u0314\5\u00ecw\2\u0314\u0315\7\20")
        buf.write(u"\2\2\u0315\u0316\5z>\2\u0316\u0317\5\u00e2r\2\u0317\u0318")
        buf.write(u"\5|?\2\u0318\u0322\3\2\2\2\u0319\u031a\7\u0086\2\2\u031a")
        buf.write(u"\u031b\7b\2\2\u031b\u031c\5\u00eav\2\u031c\u031d\7\20")
        buf.write(u"\2\2\u031d\u031e\5z>\2\u031e\u031f\5\u00e2r\2\u031f\u0320")
        buf.write(u"\5|?\2\u0320\u0322\3\2\2\2\u0321\u0312\3\2\2\2\u0321")
        buf.write(u"\u0319\3\2\2\2\u0322;\3\2\2\2\u0323\u0324\7^\2\2\u0324")
        buf.write(u"\u0325\7T\2\2\u0325\u0328\5\u00aeX\2\u0326\u0327\7\22")
        buf.write(u"\2\2\u0327\u0329\5\u00aeX\2\u0328\u0326\3\2\2\2\u0328")
        buf.write(u"\u0329\3\2\2\2\u0329\u032a\3\2\2\2\u032a\u032b\7b\2\2")
        buf.write(u"\u032b\u032c\5N(\2\u032c\u032d\7\20\2\2\u032d\u032e\5")
        buf.write(u"z>\2\u032e\u032f\5\u00e2r\2\u032f\u0330\5|?\2\u0330=")
        buf.write(u"\3\2\2\2\u0331\u0332\7R\2\2\u0332\u0333\7\20\2\2\u0333")
        buf.write(u"\u0334\5z>\2\u0334\u0335\5\u00e2r\2\u0335\u0336\5|?\2")
        buf.write(u"\u0336\u0337\5x=\2\u0337\u0338\7\u0088\2\2\u0338\u0339")
        buf.write(u"\5N(\2\u0339?\3\2\2\2\u033a\u033b\7\u0088\2\2\u033b\u033c")
        buf.write(u"\5N(\2\u033c\u033d\7\20\2\2\u033d\u033e\5z>\2\u033e\u033f")
        buf.write(u"\5\u00e2r\2\u033f\u0340\5|?\2\u0340A\3\2\2\2\u0341\u0342")
        buf.write(u"\7a\2\2\u0342\u0343\5N(\2\u0343\u0344\7\20\2\2\u0344")
        buf.write(u"\u0345\5z>\2\u0345\u0346\5\u00e2r\2\u0346\u034a\5|?\2")
        buf.write(u"\u0347\u0348\5x=\2\u0348\u0349\5D#\2\u0349\u034b\3\2")
        buf.write(u"\2\2\u034a\u0347\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u0353")
        buf.write(u"\3\2\2\2\u034c\u034d\5x=\2\u034d\u034e\7U\2\2\u034e\u034f")
        buf.write(u"\7\20\2\2\u034f\u0350\5z>\2\u0350\u0351\5\u00e2r\2\u0351")
        buf.write(u"\u0352\5|?\2\u0352\u0354\3\2\2\2\u0353\u034c\3\2\2\2")
        buf.write(u"\u0353\u0354\3\2\2\2\u0354C\3\2\2\2\u0355\u0356\b#\1")
        buf.write(u"\2\u0356\u0357\7U\2\2\u0357\u0358\7a\2\2\u0358\u0359")
        buf.write(u"\5N(\2\u0359\u035a\7\20\2\2\u035a\u035b\5z>\2\u035b\u035c")
        buf.write(u"\5\u00e2r\2\u035c\u035d\5|?\2\u035d\u036a\3\2\2\2\u035e")
        buf.write(u"\u035f\f\3\2\2\u035f\u0360\5x=\2\u0360\u0361\7U\2\2\u0361")
        buf.write(u"\u0362\7a\2\2\u0362\u0363\5N(\2\u0363\u0364\7\20\2\2")
        buf.write(u"\u0364\u0365\5z>\2\u0365\u0366\5\u00e2r\2\u0366\u0367")
        buf.write(u"\5|?\2\u0367\u0369\3\2\2\2\u0368\u035e\3\2\2\2\u0369")
        buf.write(u"\u036c\3\2\2\2\u036a\u0368\3\2\2\2\u036a\u036b\3\2\2")
        buf.write(u"\2\u036bE\3\2\2\2\u036c\u036a\3\2\2\2\u036d\u036e\7u")
        buf.write(u"\2\2\u036e\u036f\5N(\2\u036fG\3\2\2\2\u0370\u0371\7\177")
        buf.write(u"\2\2\u0371\u0372\7o\2\2\u0372\u0373\5\u00aeX\2\u0373")
        buf.write(u"\u0374\7S\2\2\u0374\u0375\7\20\2\2\u0375\u0376\5z>\2")
        buf.write(u"\u0376\u0377\5\u00e2r\2\u0377\u0378\5|?\2\u0378\u037a")
        buf.write(u"\5v<\2\u0379\u037b\5\u00e8u\2\u037a\u0379\3\2\2\2\u037a")
        buf.write(u"\u037b\3\2\2\2\u037b\u0387\3\2\2\2\u037c\u0380\7s\2\2")
        buf.write(u"\u037d\u037e\7\u0086\2\2\u037e\u0380\7C\2\2\u037f\u037c")
        buf.write(u"\3\2\2\2\u037f\u037d\3\2\2\2\u0380\u0381\3\2\2\2\u0381")
        buf.write(u"\u0382\7\20\2\2\u0382\u0383\5z>\2\u0383\u0384\5\u00e2")
        buf.write(u"r\2\u0384\u0385\5|?\2\u0385\u0386\5v<\2\u0386\u0388\3")
        buf.write(u"\2\2\2\u0387\u037f\3\2\2\2\u0387\u0388\3\2\2\2\u0388")
        buf.write(u"\u0390\3\2\2\2\u0389\u038a\7A\2\2\u038a\u038b\7\20\2")
        buf.write(u"\2\u038b\u038c\5z>\2\u038c\u038d\5\u00e2r\2\u038d\u038e")
        buf.write(u"\5|?\2\u038e\u038f\5v<\2\u038f\u0391\3\2\2\2\u0390\u0389")
        buf.write(u"\3\2\2\2\u0390\u0391\3\2\2\2\u0391\u0392\3\2\2\2\u0392")
        buf.write(u"\u0393\5v<\2\u0393I\3\2\2\2\u0394\u0395\7\u0086\2\2\u0395")
        buf.write(u"\u0396\5\u00b2Z\2\u0396\u0397\7\20\2\2\u0397\u0398\5")
        buf.write(u"z>\2\u0398\u0399\5\u00e2r\2\u0399\u039a\5|?\2\u039a\u039b")
        buf.write(u"\5v<\2\u039b\u03a8\3\2\2\2\u039c\u039d\7\u0086\2\2\u039d")
        buf.write(u"\u039e\7b\2\2\u039e\u039f\7\27\2\2\u039f\u03a0\5\u008e")
        buf.write(u"H\2\u03a0\u03a1\7\30\2\2\u03a1\u03a2\7\20\2\2\u03a2\u03a3")
        buf.write(u"\5z>\2\u03a3\u03a4\5\u00e2r\2\u03a4\u03a5\5|?\2\u03a5")
        buf.write(u"\u03a6\5v<\2\u03a6\u03a8\3\2\2\2\u03a7\u0394\3\2\2\2")
        buf.write(u"\u03a7\u039c\3\2\2\2\u03a8K\3\2\2\2\u03a9\u03ab\7y\2")
        buf.write(u"\2\u03aa\u03ac\5N(\2\u03ab\u03aa\3\2\2\2\u03ab\u03ac")
        buf.write(u"\3\2\2\2\u03acM\3\2\2\2\u03ad\u03ae\b(\1\2\u03ae\u03af")
        buf.write(u"\7\"\2\2\u03af\u03c8\5N((\u03b0\u03b1\7l\2\2\u03b1\u03c8")
        buf.write(u"\5N(\'\u03b2\u03b3\7=\2\2\u03b3\u03b4\7\20\2\2\u03b4")
        buf.write(u"\u03c8\5N(\f\u03b5\u03c8\5X-\2\u03b6\u03c8\5P)\2\u03b7")
        buf.write(u"\u03b8\5P)\2\u03b8\u03b9\5j\66\2\u03b9\u03c8\3\2\2\2")
        buf.write(u"\u03ba\u03bb\7Y\2\2\u03bb\u03bc\7\20\2\2\u03bc\u03c8")
        buf.write(u"\5\u00aeX\2\u03bd\u03be\7<\2\2\u03be\u03bf\7\20\2\2\u03bf")
        buf.write(u"\u03c8\5\u00aaV\2\u03c0\u03c8\5\\/\2\u03c1\u03c8\5^\60")
        buf.write(u"\2\u03c2\u03c8\5f\64\2\u03c3\u03c8\5`\61\2\u03c4\u03c8")
        buf.write(u"\5h\65\2\u03c5\u03c8\5d\63\2\u03c6\u03c8\5T+\2\u03c7")
        buf.write(u"\u03ad\3\2\2\2\u03c7\u03b0\3\2\2\2\u03c7\u03b2\3\2\2")
        buf.write(u"\2\u03c7\u03b5\3\2\2\2\u03c7\u03b6\3\2\2\2\u03c7\u03b7")
        buf.write(u"\3\2\2\2\u03c7\u03ba\3\2\2\2\u03c7\u03bd\3\2\2\2\u03c7")
        buf.write(u"\u03c0\3\2\2\2\u03c7\u03c1\3\2\2\2\u03c7\u03c2\3\2\2")
        buf.write(u"\2\u03c7\u03c3\3\2\2\2\u03c7\u03c4\3\2\2\2\u03c7\u03c5")
        buf.write(u"\3\2\2\2\u03c7\u03c6\3\2\2\2\u03c8\u0429\3\2\2\2\u03c9")
        buf.write(u"\u03ca\f&\2\2\u03ca\u03cb\5\u0116\u008c\2\u03cb\u03cc")
        buf.write(u"\5N(\'\u03cc\u0428\3\2\2\2\u03cd\u03ce\f%\2\2\u03ce\u03cf")
        buf.write(u"\5\u0118\u008d\2\u03cf\u03d0\5N(&\u03d0\u0428\3\2\2\2")
        buf.write(u"\u03d1\u03d2\f$\2\2\u03d2\u03d3\5\u011c\u008f\2\u03d3")
        buf.write(u"\u03d4\5N(%\u03d4\u0428\3\2\2\2\u03d5\u03d6\f#\2\2\u03d6")
        buf.write(u"\u03d7\5\u011a\u008e\2\u03d7\u03d8\5N($\u03d8\u0428\3")
        buf.write(u"\2\2\2\u03d9\u03da\f\"\2\2\u03da\u03db\t\2\2\2\u03db")
        buf.write(u"\u0428\5N(#\u03dc\u03dd\f!\2\2\u03dd\u03de\7)\2\2\u03de")
        buf.write(u"\u0428\5N(\"\u03df\u03e0\f \2\2\u03e0\u03e1\7*\2\2\u03e1")
        buf.write(u"\u0428\5N(!\u03e2\u03e3\f\37\2\2\u03e3\u03e4\7\'\2\2")
        buf.write(u"\u03e4\u0428\5N( \u03e5\u03e6\f\36\2\2\u03e6\u03e7\7")
        buf.write(u"(\2\2\u03e7\u0428\5N(\37\u03e8\u03e9\f\33\2\2\u03e9\u03ea")
        buf.write(u"\7,\2\2\u03ea\u0428\5N(\34\u03eb\u03ec\f\32\2\2\u03ec")
        buf.write(u"\u03ed\7+\2\2\u03ed\u0428\5N(\33\u03ee\u03ef\f\31\2\2")
        buf.write(u"\u03ef\u03f0\7\60\2\2\u03f0\u0428\5N(\32\u03f1\u03f2")
        buf.write(u"\f\30\2\2\u03f2\u03f3\7r\2\2\u03f3\u0428\5N(\31\u03f4")
        buf.write(u"\u03f5\f\27\2\2\u03f5\u03f6\7B\2\2\u03f6\u0428\5N(\30")
        buf.write(u"\u03f7\u03f8\f\26\2\2\u03f8\u03f9\7a\2\2\u03f9\u03fa")
        buf.write(u"\5N(\2\u03fa\u03fb\7U\2\2\u03fb\u03fc\5N(\27\u03fc\u0428")
        buf.write(u"\3\2\2\2\u03fd\u03fe\f\24\2\2\u03fe\u03ff\7b\2\2\u03ff")
        buf.write(u"\u0428\5N(\25\u0400\u0401\f\23\2\2\u0401\u0402\7N\2\2")
        buf.write(u"\u0402\u0428\5N(\24\u0403\u0404\f\22\2\2\u0404\u0405")
        buf.write(u"\7N\2\2\u0405\u0406\7@\2\2\u0406\u0428\5N(\23\u0407\u0408")
        buf.write(u"\f\21\2\2\u0408\u0409\7N\2\2\u0409\u040a\7C\2\2\u040a")
        buf.write(u"\u0428\5N(\22\u040b\u040c\f\20\2\2\u040c\u040d\7l\2\2")
        buf.write(u"\u040d\u040e\7b\2\2\u040e\u0428\5N(\21\u040f\u0410\f")
        buf.write(u"\17\2\2\u0410\u0411\7l\2\2\u0411\u0412\7N\2\2\u0412\u0428")
        buf.write(u"\5N(\20\u0413\u0414\f\16\2\2\u0414\u0415\7l\2\2\u0415")
        buf.write(u"\u0416\7N\2\2\u0416\u0417\7@\2\2\u0417\u0428\5N(\17\u0418")
        buf.write(u"\u0419\f\r\2\2\u0419\u041a\7l\2\2\u041a\u041b\7N\2\2")
        buf.write(u"\u041b\u041c\7C\2\2\u041c\u0428\5N(\16\u041d\u041e\f")
        buf.write(u"\35\2\2\u041e\u041f\7d\2\2\u041f\u0420\7l\2\2\u0420\u0428")
        buf.write(u"\5\u010a\u0086\2\u0421\u0422\f\34\2\2\u0422\u0423\7d")
        buf.write(u"\2\2\u0423\u0428\5\u010a\u0086\2\u0424\u0425\f\25\2\2")
        buf.write(u"\u0425\u0426\7D\2\2\u0426\u0428\5\u00be`\2\u0427\u03c9")
        buf.write(u"\3\2\2\2\u0427\u03cd\3\2\2\2\u0427\u03d1\3\2\2\2\u0427")
        buf.write(u"\u03d5\3\2\2\2\u0427\u03d9\3\2\2\2\u0427\u03dc\3\2\2")
        buf.write(u"\2\u0427\u03df\3\2\2\2\u0427\u03e2\3\2\2\2\u0427\u03e5")
        buf.write(u"\3\2\2\2\u0427\u03e8\3\2\2\2\u0427\u03eb\3\2\2\2\u0427")
        buf.write(u"\u03ee\3\2\2\2\u0427\u03f1\3\2\2\2\u0427\u03f4\3\2\2")
        buf.write(u"\2\u0427\u03f7\3\2\2\2\u0427\u03fd\3\2\2\2\u0427\u0400")
        buf.write(u"\3\2\2\2\u0427\u0403\3\2\2\2\u0427\u0407\3\2\2\2\u0427")
        buf.write(u"\u040b\3\2\2\2\u0427\u040f\3\2\2\2\u0427\u0413\3\2\2")
        buf.write(u"\2\u0427\u0418\3\2\2\2\u0427\u041d\3\2\2\2\u0427\u0421")
        buf.write(u"\3\2\2\2\u0427\u0424\3\2\2\2\u0428\u042b\3\2\2\2\u0429")
        buf.write(u"\u0427\3\2\2\2\u0429\u042a\3\2\2\2\u042aO\3\2\2\2\u042b")
        buf.write(u"\u0429\3\2\2\2\u042c\u042d\b)\1\2\u042d\u042e\5\u00ac")
        buf.write(u"W\2\u042e\u0433\3\2\2\2\u042f\u0430\f\3\2\2\u0430\u0432")
        buf.write(u"\5R*\2\u0431\u042f\3\2\2\2\u0432\u0435\3\2\2\2\u0433")
        buf.write(u"\u0431\3\2\2\2\u0433\u0434\3\2\2\2\u0434Q\3\2\2\2\u0435")
        buf.write(u"\u0433\3\2\2\2\u0436\u0437\6*\37\3\u0437\u0438\7\24\2")
        buf.write(u"\2\u0438\u0439\5\u00acW\2\u0439S\3\2\2\2\u043a\u043b")
        buf.write(u"\7c\2\2\u043b\u043c\7\20\2\2\u043c\u043d\5\u00aeX\2\u043d")
        buf.write(u"\u043e\5V,\2\u043eU\3\2\2\2\u043f\u0440\6, \3\u0440W")
        buf.write(u"\3\2\2\2\u0441\u0442\b-\1\2\u0442\u0443\5\u00f0y\2\u0443")
        buf.write(u"\u0448\3\2\2\2\u0444\u0445\f\3\2\2\u0445\u0447\5Z.\2")
        buf.write(u"\u0446\u0444\3\2\2\2\u0447\u044a\3\2\2\2\u0448\u0446")
        buf.write(u"\3\2\2\2\u0448\u0449\3\2\2\2\u0449Y\3\2\2\2\u044a\u0448")
        buf.write(u"\3\2\2\2\u044b\u044c\6.\"\3\u044c\u044d\7\24\2\2\u044d")
        buf.write(u"\u0459\5\u00aeX\2\u044e\u044f\6.#\3\u044f\u0450\7\27")
        buf.write(u"\2\2\u0450\u0451\5\u0104\u0083\2\u0451\u0452\7\30\2\2")
        buf.write(u"\u0452\u0459\3\2\2\2\u0453\u0454\6.$\3\u0454\u0455\7")
        buf.write(u"\27\2\2\u0455\u0456\5N(\2\u0456\u0457\7\30\2\2\u0457")
        buf.write(u"\u0459\3\2\2\2\u0458\u044b\3\2\2\2\u0458\u044e\3\2\2")
        buf.write(u"\2\u0458\u0453\3\2\2\2\u0459[\3\2\2\2\u045a\u045b\5\u00a4")
        buf.write(u"S\2\u045b]\3\2\2\2\u045c\u045e\7i\2\2\u045d\u045c\3\2")
        buf.write(u"\2\2\u045d\u045e\3\2\2\2\u045e\u045f\3\2\2\2\u045f\u0460")
        buf.write(u"\5\u00a0Q\2\u0460\u0461\7_\2\2\u0461\u046a\5N(\2\u0462")
        buf.write(u"\u0464\7\22\2\2\u0463\u0462\3\2\2\2\u0463\u0464\3\2\2")
        buf.write(u"\2\u0464\u0465\3\2\2\2\u0465\u0468\5l\67\2\u0466\u0467")
        buf.write(u"\7B\2\2\u0467\u0469\5n8\2\u0468\u0466\3\2\2\2\u0468\u0469")
        buf.write(u"\3\2\2\2\u0469\u046b\3\2\2\2\u046a\u0463\3\2\2\2\u046a")
        buf.write(u"\u046b\3\2\2\2\u046b\u0478\3\2\2\2\u046c\u046e\7i\2\2")
        buf.write(u"\u046d\u046c\3\2\2\2\u046d\u046e\3\2\2\2\u046e\u046f")
        buf.write(u"\3\2\2\2\u046f\u0475\5\u00a0Q\2\u0470\u0473\5l\67\2\u0471")
        buf.write(u"\u0472\7B\2\2\u0472\u0474\5n8\2\u0473\u0471\3\2\2\2\u0473")
        buf.write(u"\u0474\3\2\2\2\u0474\u0476\3\2\2\2\u0475\u0470\3\2\2")
        buf.write(u"\2\u0475\u0476\3\2\2\2\u0476\u0478\3\2\2\2\u0477\u045d")
        buf.write(u"\3\2\2\2\u0477\u046d\3\2\2\2\u0478_\3\2\2\2\u0479\u047a")
        buf.write(u"\7v\2\2\u047a\u047b\7_\2\2\u047b\u047c\5N(\2\u047ca\3")
        buf.write(u"\2\2\2\u047d\u047e\7\u0089\2\2\u047e\u047f\5N(\2\u047f")
        buf.write(u"\u0480\7\u0083\2\2\u0480\u0481\5N(\2\u0481c\3\2\2\2\u0482")
        buf.write(u"\u0483\5P)\2\u0483\u0484\7\"\2\2\u0484\u0485\5N(\2\u0485")
        buf.write(u"e\3\2\2\2\u0486\u0487\7\\\2\2\u0487\u0488\7C\2\2\u0488")
        buf.write(u"\u0489\5\u00aeX\2\u0489\u048a\7_\2\2\u048a\u048b\5N(")
        buf.write(u"\2\u048b\u048c\7\u0087\2\2\u048c\u048d\5N(\2\u048dg\3")
        buf.write(u"\2\2\2\u048e\u048f\7~\2\2\u048f\u0495\5X-\2\u0490\u0491")
        buf.write(u"\7\u0085\2\2\u0491\u0492\5X-\2\u0492\u0493\7D\2\2\u0493")
        buf.write(u"\u0494\5\u010e\u0088\2\u0494\u0496\3\2\2\2\u0495\u0490")
        buf.write(u"\3\2\2\2\u0495\u0496\3\2\2\2\u0496i\3\2\2\2\u0497\u0498")
        buf.write(u"\6\66%\3\u0498\u049e\5N(\2\u0499\u049c\5l\67\2\u049a")
        buf.write(u"\u049b\7B\2\2\u049b\u049d\5n8\2\u049c\u049a\3\2\2\2\u049c")
        buf.write(u"\u049d\3\2\2\2\u049d\u049f\3\2\2\2\u049e\u0499\3\2\2")
        buf.write(u"\2\u049e\u049f\3\2\2\2\u049f\u04a6\3\2\2\2\u04a0\u04a3")
        buf.write(u"\5l\67\2\u04a1\u04a2\7B\2\2\u04a2\u04a4\5n8\2\u04a3\u04a1")
        buf.write(u"\3\2\2\2\u04a3\u04a4\3\2\2\2\u04a4\u04a6\3\2\2\2\u04a5")
        buf.write(u"\u0497\3\2\2\2\u04a5\u04a0\3\2\2\2\u04a6k\3\2\2\2\u04a7")
        buf.write(u"\u04a8\b\67\1\2\u04a8\u04a9\7\u0085\2\2\u04a9\u04aa\5")
        buf.write(u"n8\2\u04aa\u04b0\3\2\2\2\u04ab\u04ac\f\3\2\2\u04ac\u04ad")
        buf.write(u"\7\22\2\2\u04ad\u04af\5n8\2\u04ae\u04ab\3\2\2\2\u04af")
        buf.write(u"\u04b2\3\2\2\2\u04b0\u04ae\3\2\2\2\u04b0\u04b1\3\2\2")
        buf.write(u"\2\u04b1m\3\2\2\2\u04b2\u04b0\3\2\2\2\u04b3\u04b4\5N")
        buf.write(u"(\2\u04b4\u04b5\7D\2\2\u04b5\u04b6\5\u00aeX\2\u04b6o")
        buf.write(u"\3\2\2\2\u04b7\u04b8\5\u0108\u0085\2\u04b8\u04b9\5\u0114")
        buf.write(u"\u008b\2\u04b9\u04ba\5N(\2\u04baq\3\2\2\2\u04bb\u04bc")
        buf.write(u"\6:\'\3\u04bc\u04bd\7\24\2\2\u04bd\u04c4\5\u00aeX\2\u04be")
        buf.write(u"\u04bf\6:(\3\u04bf\u04c0\7\27\2\2\u04c0\u04c1\5N(\2\u04c1")
        buf.write(u"\u04c2\7\30\2\2\u04c2\u04c4\3\2\2\2\u04c3\u04bb\3\2\2")
        buf.write(u"\2\u04c3\u04be\3\2\2\2\u04c4s\3\2\2\2\u04c5\u04c6\5\u00d6")
        buf.write(u"l\2\u04c6\u04c7\5\u0114\u008b\2\u04c7\u04c8\5N(\2\u04c8")
        buf.write(u"u\3\2\2\2\u04c9\u04cb\7\7\2\2\u04ca\u04c9\3\2\2\2\u04cb")
        buf.write(u"\u04ce\3\2\2\2\u04cc\u04ca\3\2\2\2\u04cc\u04cd\3\2\2")
        buf.write(u"\2\u04cdw\3\2\2\2\u04ce\u04cc\3\2\2\2\u04cf\u04d1\7\7")
        buf.write(u"\2\2\u04d0\u04cf\3\2\2\2\u04d1\u04d2\3\2\2\2\u04d2\u04d0")
        buf.write(u"\3\2\2\2\u04d2\u04d3\3\2\2\2\u04d3y\3\2\2\2\u04d4\u04d6")
        buf.write(u"\7\7\2\2\u04d5\u04d4\3\2\2\2\u04d6\u04d7\3\2\2\2\u04d7")
        buf.write(u"\u04d5\3\2\2\2\u04d7\u04d8\3\2\2\2\u04d8\u04d9\3\2\2")
        buf.write(u"\2\u04d9\u04da\7\3\2\2\u04da{\3\2\2\2\u04db\u04dd\7\7")
        buf.write(u"\2\2\u04dc\u04db\3\2\2\2\u04dd\u04e0\3\2\2\2\u04de\u04dc")
        buf.write(u"\3\2\2\2\u04de\u04df\3\2\2\2\u04df\u04e1\3\2\2\2\u04e0")
        buf.write(u"\u04de\3\2\2\2\u04e1\u04e2\7\4\2\2\u04e2}\3\2\2\2\u04e3")
        buf.write(u"\u04e4\7m\2\2\u04e4\177\3\2\2\2\u04e5\u04e7\5\u0082B")
        buf.write(u"\2\u04e6\u04e5\3\2\2\2\u04e6\u04e7\3\2\2\2\u04e7\u04e8")
        buf.write(u"\3\2\2\2\u04e8\u04e9\5v<\2\u04e9\u04ea\7\2\2\3\u04ea")
        buf.write(u"\u0081\3\2\2\2\u04eb\u04ec\bB\1\2\u04ec\u04ed\5\u0084")
        buf.write(u"C\2\u04ed\u04f4\3\2\2\2\u04ee\u04ef\f\3\2\2\u04ef\u04f0")
        buf.write(u"\5x=\2\u04f0\u04f1\5\u0084C\2\u04f1\u04f3\3\2\2\2\u04f2")
        buf.write(u"\u04ee\3\2\2\2\u04f3\u04f6\3\2\2\2\u04f4\u04f2\3\2\2")
        buf.write(u"\2\u04f4\u04f5\3\2\2\2\u04f5\u0083\3\2\2\2\u04f6\u04f4")
        buf.write(u"\3\2\2\2\u04f7\u04fd\5\n\6\2\u04f8\u04fd\5\u00a6T\2\u04f9")
        buf.write(u"\u04fd\5\u0086D\2\u04fa\u04fd\5\u0088E\2\u04fb\u04fd")
        buf.write(u"\5\u00d8m\2\u04fc\u04f7\3\2\2\2\u04fc\u04f8\3\2\2\2\u04fc")
        buf.write(u"\u04f9\3\2\2\2\u04fc\u04fa\3\2\2\2\u04fc\u04fb\3\2\2")
        buf.write(u"\2\u04fd\u0085\3\2\2\2\u04fe\u04ff\5\32\16\2\u04ff\u0087")
        buf.write(u"\3\2\2\2\u0500\u0503\5\2\2\2\u0501\u0503\5\4\3\2\u0502")
        buf.write(u"\u0500\3\2\2\2\u0502\u0501\3\2\2\2\u0503\u0089\3\2\2")
        buf.write(u"\2\u0504\u0505\bF\1\2\u0505\u0506\5\6\4\2\u0506\u050d")
        buf.write(u"\3\2\2\2\u0507\u0508\f\3\2\2\u0508\u0509\5x=\2\u0509")
        buf.write(u"\u050a\5\6\4\2\u050a\u050c\3\2\2\2\u050b\u0507\3\2\2")
        buf.write(u"\2\u050c\u050f\3\2\2\2\u050d\u050b\3\2\2\2\u050d\u050e")
        buf.write(u"\3\2\2\2\u050e\u008b\3\2\2\2\u050f\u050d\3\2\2\2\u0510")
        buf.write(u"\u0511\bG\1\2\u0511\u0512\5\b\5\2\u0512\u0519\3\2\2\2")
        buf.write(u"\u0513\u0514\f\3\2\2\u0514\u0515\5x=\2\u0515\u0516\5")
        buf.write(u"\b\5\2\u0516\u0518\3\2\2\2\u0517\u0513\3\2\2\2\u0518")
        buf.write(u"\u051b\3\2\2\2\u0519\u0517\3\2\2\2\u0519\u051a\3\2\2")
        buf.write(u"\2\u051a\u008d\3\2\2\2\u051b\u0519\3\2\2\2\u051c\u051d")
        buf.write(u"\bH\1\2\u051d\u051e\5\u00b2Z\2\u051e\u0524\3\2\2\2\u051f")
        buf.write(u"\u0520\f\3\2\2\u0520\u0521\7\22\2\2\u0521\u0523\5\u00b2")
        buf.write(u"Z\2\u0522\u051f\3\2\2\2\u0523\u0526\3\2\2\2\u0524\u0522")
        buf.write(u"\3\2\2\2\u0524\u0525\3\2\2\2\u0525\u008f\3\2\2\2\u0526")
        buf.write(u"\u0524\3\2\2\2\u0527\u0528\7b\2\2\u0528\u0532\5\u0092")
        buf.write(u"J\2\u0529\u052a\7b\2\2\u052a\u0532\5\u0094K\2\u052b\u052c")
        buf.write(u"\7b\2\2\u052c\u0532\5\u0098M\2\u052d\u052e\7e\2\2\u052e")
        buf.write(u"\u0532\7\u0093\2\2\u052f\u0530\7e\2\2\u0530\u0532\5N")
        buf.write(u"(\2\u0531\u0527\3\2\2\2\u0531\u0529\3\2\2\2\u0531\u052b")
        buf.write(u"\3\2\2\2\u0531\u052d\3\2\2\2\u0531\u052f\3\2\2\2\u0532")
        buf.write(u"\u0091\3\2\2\2\u0533\u0535\7\27\2\2\u0534\u0536\5\u0096")
        buf.write(u"L\2\u0535\u0534\3\2\2\2\u0535\u0536\3\2\2\2\u0536\u0537")
        buf.write(u"\3\2\2\2\u0537\u0538\7\30\2\2\u0538\u0093\3\2\2\2\u0539")
        buf.write(u"\u053b\7)\2\2\u053a\u053c\5\u0096L\2\u053b\u053a\3\2")
        buf.write(u"\2\2\u053b\u053c\3\2\2\2\u053c\u053d\3\2\2\2\u053d\u053e")
        buf.write(u"\7\'\2\2\u053e\u0095\3\2\2\2\u053f\u0540\bL\1\2\u0540")
        buf.write(u"\u0541\5N(\2\u0541\u0547\3\2\2\2\u0542\u0543\f\3\2\2")
        buf.write(u"\u0543\u0544\7\22\2\2\u0544\u0546\5N(\2\u0545\u0542\3")
        buf.write(u"\2\2\2\u0546\u0549\3\2\2\2\u0547\u0545\3\2\2\2\u0547")
        buf.write(u"\u0548\3\2\2\2\u0548\u0097\3\2\2\2\u0549\u0547\3\2\2")
        buf.write(u"\2\u054a\u054b\7\27\2\2\u054b\u054c\5N(\2\u054c\u054d")
        buf.write(u"\7\23\2\2\u054d\u054e\5N(\2\u054e\u054f\7\30\2\2\u054f")
        buf.write(u"\u0099\3\2\2\2\u0550\u0551\bN\1\2\u0551\u0552\5\u009c")
        buf.write(u"O\2\u0552\u055d\3\2\2\2\u0553\u0554\f\5\2\2\u0554\u055c")
        buf.write(u"\7+\2\2\u0555\u0556\f\4\2\2\u0556\u0557\7\27\2\2\u0557")
        buf.write(u"\u055c\7\30\2\2\u0558\u0559\f\3\2\2\u0559\u055a\7\31")
        buf.write(u"\2\2\u055a\u055c\7\32\2\2\u055b\u0553\3\2\2\2\u055b\u0555")
        buf.write(u"\3\2\2\2\u055b\u0558\3\2\2\2\u055c\u055f\3\2\2\2\u055d")
        buf.write(u"\u055b\3\2\2\2\u055d\u055e\3\2\2\2\u055e\u009b\3\2\2")
        buf.write(u"\2\u055f\u055d\3\2\2\2\u0560\u0563\5\u009eP\2\u0561\u0563")
        buf.write(u"\5\u00a0Q\2\u0562\u0560\3\2\2\2\u0562\u0561\3\2\2\2\u0563")
        buf.write(u"\u009d\3\2\2\2\u0564\u056f\7\63\2\2\u0565\u056f\7\64")
        buf.write(u"\2\2\u0566\u056f\7\65\2\2\u0567\u056f\7\66\2\2\u0568")
        buf.write(u"\u056f\7\67\2\2\u0569\u056f\78\2\2\u056a\u056f\7:\2\2")
        buf.write(u"\u056b\u056f\79\2\2\u056c\u056f\7;\2\2\u056d\u056f\7")
        buf.write(u"=\2\2\u056e\u0564\3\2\2\2\u056e\u0565\3\2\2\2\u056e\u0566")
        buf.write(u"\3\2\2\2\u056e\u0567\3\2\2\2\u056e\u0568\3\2\2\2\u056e")
        buf.write(u"\u0569\3\2\2\2\u056e\u056a\3\2\2\2\u056e\u056b\3\2\2")
        buf.write(u"\2\u056e\u056c\3\2\2\2\u056e\u056d\3\2\2\2\u056f\u009f")
        buf.write(u"\3\2\2\2\u0570\u0571\7\u008f\2\2\u0571\u00a1\3\2\2\2")
        buf.write(u"\u0572\u0573\7=\2\2\u0573\u00a3\3\2\2\2\u0574\u0575\7")
        buf.write(u">\2\2\u0575\u00a5\3\2\2\2\u0576\u057a\5\f\7\2\u0577\u057a")
        buf.write(u"\5\30\r\2\u0578\u057a\5\16\b\2\u0579\u0576\3\2\2\2\u0579")
        buf.write(u"\u0577\3\2\2\2\u0579\u0578\3\2\2\2\u057a\u00a7\3\2\2")
        buf.write(u"\2\u057b\u057c\bU\1\2\u057c\u057d\5\u00b0Y\2\u057d\u0583")
        buf.write(u"\3\2\2\2\u057e\u057f\f\3\2\2\u057f\u0580\7\22\2\2\u0580")
        buf.write(u"\u0582\5\u00b0Y\2\u0581\u057e\3\2\2\2\u0582\u0585\3\2")
        buf.write(u"\2\2\u0583\u0581\3\2\2\2\u0583\u0584\3\2\2\2\u0584\u00a9")
        buf.write(u"\3\2\2\2\u0585\u0583\3\2\2\2\u0586\u0589\5\u00aeX\2\u0587")
        buf.write(u"\u0589\5\u00b0Y\2\u0588\u0586\3\2\2\2\u0588\u0587\3\2")
        buf.write(u"\2\2\u0589\u00ab\3\2\2\2\u058a\u058e\5\u00aeX\2\u058b")
        buf.write(u"\u058e\5\u00b0Y\2\u058c\u058e\5\u00b2Z\2\u058d\u058a")
        buf.write(u"\3\2\2\2\u058d\u058b\3\2\2\2\u058d\u058c\3\2\2\2\u058e")
        buf.write(u"\u00ad\3\2\2\2\u058f\u0590\7\u0090\2\2\u0590\u00af\3")
        buf.write(u"\2\2\2\u0591\u0592\7\u008f\2\2\u0592\u00b1\3\2\2\2\u0593")
        buf.write(u"\u0594\7\u008e\2\2\u0594\u00b3\3\2\2\2\u0595\u0596\b")
        buf.write(u"[\1\2\u0596\u0597\5\u00b6\\\2\u0597\u059d\3\2\2\2\u0598")
        buf.write(u"\u0599\f\3\2\2\u0599\u059a\7\22\2\2\u059a\u059c\5\u00b6")
        buf.write(u"\\\2\u059b\u0598\3\2\2\2\u059c\u059f\3\2\2\2\u059d\u059b")
        buf.write(u"\3\2\2\2\u059d\u059e\3\2\2\2\u059e\u00b5\3\2\2\2\u059f")
        buf.write(u"\u059d\3\2\2\2\u05a0\u05a6\5\u00bc_\2\u05a1\u05a3\7i")
        buf.write(u"\2\2\u05a2\u05a1\3\2\2\2\u05a2\u05a3\3\2\2\2\u05a3\u05a4")
        buf.write(u"\3\2\2\2\u05a4\u05a6\5\u00b8]\2\u05a5\u05a0\3\2\2\2\u05a5")
        buf.write(u"\u05a2\3\2\2\2\u05a6\u00b7\3\2\2\2\u05a7\u05aa\5\u00ba")
        buf.write(u"^\2\u05a8\u05aa\5.\30\2\u05a9\u05a7\3\2\2\2\u05a9\u05a8")
        buf.write(u"\3\2\2\2\u05aa\u00b9\3\2\2\2\u05ab\u05ae\5\u00aeX\2\u05ac")
        buf.write(u"\u05ad\7,\2\2\u05ad\u05af\5\u00f6|\2\u05ae\u05ac\3\2")
        buf.write(u"\2\2\u05ae\u05af\3\2\2\2\u05af\u00bb\3\2\2\2\u05b0\u05b1")
        buf.write(u"\5\u00a2R\2\u05b1\u05b2\5\u00aeX\2\u05b2\u00bd\3\2\2")
        buf.write(u"\2\u05b3\u05b6\5\u009aN\2\u05b4\u05b6\5\u00c0a\2\u05b5")
        buf.write(u"\u05b3\3\2\2\2\u05b5\u05b4\3\2\2\2\u05b6\u00bf\3\2\2")
        buf.write(u"\2\u05b7\u05b8\ba\1\2\u05b8\u05b9\7C\2\2\u05b9\u05c2")
        buf.write(u"\3\2\2\2\u05ba\u05bb\f\4\2\2\u05bb\u05bc\7\27\2\2\u05bc")
        buf.write(u"\u05c1\7\30\2\2\u05bd\u05be\f\3\2\2\u05be\u05bf\7\31")
        buf.write(u"\2\2\u05bf\u05c1\7\32\2\2\u05c0\u05ba\3\2\2\2\u05c0\u05bd")
        buf.write(u"\3\2\2\2\u05c1\u05c4\3\2\2\2\u05c2\u05c0\3\2\2\2\u05c2")
        buf.write(u"\u05c3\3\2\2\2\u05c3\u00c1\3\2\2\2\u05c4\u05c2\3\2\2")
        buf.write(u"\2\u05c5\u05c6\bb\1\2\u05c6\u05c7\5\u00c4c\2\u05c7\u05ce")
        buf.write(u"\3\2\2\2\u05c8\u05c9\f\3\2\2\u05c9\u05ca\5x=\2\u05ca")
        buf.write(u"\u05cb\5\u00c4c\2\u05cb\u05cd\3\2\2\2\u05cc\u05c8\3\2")
        buf.write(u"\2\2\u05cd\u05d0\3\2\2\2\u05ce\u05cc\3\2\2\2\u05ce\u05cf")
        buf.write(u"\3\2\2\2\u05cf\u00c3\3\2\2\2\u05d0\u05ce\3\2\2\2\u05d1")
        buf.write(u"\u05d7\5\24\13\2\u05d2\u05d7\5\26\f\2\u05d3\u05d7\5$")
        buf.write(u"\23\2\u05d4\u05d7\5\"\22\2\u05d5\u05d7\5\22\n\2\u05d6")
        buf.write(u"\u05d1\3\2\2\2\u05d6\u05d2\3\2\2\2\u05d6\u05d3\3\2\2")
        buf.write(u"\2\u05d6\u05d4\3\2\2\2\u05d6\u05d5\3\2\2\2\u05d7\u00c5")
        buf.write(u"\3\2\2\2\u05d8\u05d9\bd\1\2\u05d9\u05da\5\u00c8e\2\u05da")
        buf.write(u"\u05e1\3\2\2\2\u05db\u05dc\f\3\2\2\u05dc\u05dd\5x=\2")
        buf.write(u"\u05dd\u05de\5\u00c8e\2\u05de\u05e0\3\2\2\2\u05df\u05db")
        buf.write(u"\3\2\2\2\u05e0\u05e3\3\2\2\2\u05e1\u05df\3\2\2\2\u05e1")
        buf.write(u"\u05e2\3\2\2\2\u05e2\u00c7\3\2\2\2\u05e3\u05e1\3\2\2")
        buf.write(u"\2\u05e4\u05e7\5\u00c4c\2\u05e5\u05e7\5&\24\2\u05e6\u05e4")
        buf.write(u"\3\2\2\2\u05e6\u05e5\3\2\2\2\u05e7\u00c9\3\2\2\2\u05e8")
        buf.write(u"\u05e9\7\n\2\2\u05e9\u05f3\5\u0162\u00b2\2\u05ea\u05eb")
        buf.write(u"\7\13\2\2\u05eb\u05f3\5\u017a\u00be\2\u05ec\u05ed\7\f")
        buf.write(u"\2\2\u05ed\u05f3\5\u00ccg\2\u05ee\u05ef\7\r\2\2\u05ef")
        buf.write(u"\u05f3\5\u00ccg\2\u05f0\u05f1\7\16\2\2\u05f1\u05f3\5")
        buf.write(u"\u00d2j\2\u05f2\u05e8\3\2\2\2\u05f2\u05ea\3\2\2\2\u05f2")
        buf.write(u"\u05ec\3\2\2\2\u05f2\u05ee\3\2\2\2\u05f2\u05f0\3\2\2")
        buf.write(u"\2\u05f3\u00cb\3\2\2\2\u05f4\u05f6\5\u00acW\2\u05f5\u05f7")
        buf.write(u"\5\u00ceh\2\u05f6\u05f5\3\2\2\2\u05f6\u05f7\3\2\2\2\u05f7")
        buf.write(u"\u00cd\3\2\2\2\u05f8\u05f9\7_\2\2\u05f9\u05fa\5\u00d0")
        buf.write(u"i\2\u05fa\u05fb\7\20\2\2\u05fb\u0600\5\u00acW\2\u05fc")
        buf.write(u"\u05fd\7\24\2\2\u05fd\u05ff\5\u00acW\2\u05fe\u05fc\3")
        buf.write(u"\2\2\2\u05ff\u0602\3\2\2\2\u0600\u05fe\3\2\2\2\u0600")
        buf.write(u"\u0601\3\2\2\2\u0601\u00cf\3\2\2\2\u0602\u0600\3\2\2")
        buf.write(u"\2\u0603\u0604\7\u0090\2\2\u0604\u0605\6i\67\3\u0605")
        buf.write(u"\u00d1\3\2\2\2\u0606\u0608\5\u00acW\2\u0607\u0609\5\u00d4")
        buf.write(u"k\2\u0608\u0607\3\2\2\2\u0608\u0609\3\2\2\2\u0609\u00d3")
        buf.write(u"\3\2\2\2\u060a\u060b\7_\2\2\u060b\u060c\5\u00d0i\2\u060c")
        buf.write(u"\u060e\7\20\2\2\u060d\u060f\7$\2\2\u060e\u060d\3\2\2")
        buf.write(u"\2\u060e\u060f\3\2\2\2\u060f\u0610\3\2\2\2\u0610\u0615")
        buf.write(u"\5\u0134\u009b\2\u0611\u0612\7$\2\2\u0612\u0614\5\u0134")
        buf.write(u"\u009b\2\u0613\u0611\3\2\2\2\u0614\u0617\3\2\2\2\u0615")
        buf.write(u"\u0613\3\2\2\2\u0615\u0616\3\2\2\2\u0616\u061a\3\2\2")
        buf.write(u"\2\u0617\u0615\3\2\2\2\u0618\u0619\7\24\2\2\u0619\u061b")
        buf.write(u"\5\u0134\u009b\2\u061a\u0618\3\2\2\2\u061a\u061b\3\2")
        buf.write(u"\2\2\u061b\u00d5\3\2\2\2\u061c\u061d\bl\1\2\u061d\u061e")
        buf.write(u"\5\u00aeX\2\u061e\u0624\3\2\2\2\u061f\u0620\f\3\2\2\u0620")
        buf.write(u"\u0621\7\22\2\2\u0621\u0623\5\u00aeX\2\u0622\u061f\3")
        buf.write(u"\2\2\2\u0623\u0626\3\2\2\2\u0624\u0622\3\2\2\2\u0624")
        buf.write(u"\u0625\3\2\2\2\u0625\u00d7\3\2\2\2\u0626\u0624\3\2\2")
        buf.write(u"\2\u0627\u062c\5\"\22\2\u0628\u062c\5$\23\2\u0629\u062c")
        buf.write(u"\5&\24\2\u062a\u062c\5(\25\2\u062b\u0627\3\2\2\2\u062b")
        buf.write(u"\u0628\3\2\2\2\u062b\u0629\3\2\2\2\u062b\u062a\3\2\2")
        buf.write(u"\2\u062c\u00d9\3\2\2\2\u062d\u062e\bn\1\2\u062e\u062f")
        buf.write(u"\5\u00dco\2\u062f\u0636\3\2\2\2\u0630\u0631\f\3\2\2\u0631")
        buf.write(u"\u0632\5x=\2\u0632\u0633\5\u00dco\2\u0633\u0635\3\2\2")
        buf.write(u"\2\u0634\u0630\3\2\2\2\u0635\u0638\3\2\2\2\u0636\u0634")
        buf.write(u"\3\2\2\2\u0636\u0637\3\2\2\2\u0637\u00db\3\2\2\2\u0638")
        buf.write(u"\u0636\3\2\2\2\u0639\u063a\7\n\2\2\u063a\u0644\5\u014e")
        buf.write(u"\u00a8\2\u063b\u063c\7\13\2\2\u063c\u0644\5\u0168\u00b5")
        buf.write(u"\2\u063d\u063e\7\f\2\2\u063e\u0644\5\u00dep\2\u063f\u0640")
        buf.write(u"\7\r\2\2\u0640\u0644\5\u00dep\2\u0641\u0642\7\16\2\2")
        buf.write(u"\u0642\u0644\5\u00e0q\2\u0643\u0639\3\2\2\2\u0643\u063b")
        buf.write(u"\3\2\2\2\u0643\u063d\3\2\2\2\u0643\u063f\3\2\2\2\u0643")
        buf.write(u"\u0641\3\2\2\2\u0644\u00dd\3\2\2\2\u0645\u0647\5\u0136")
        buf.write(u"\u009c\2\u0646\u0648\7\21\2\2\u0647\u0646\3\2\2\2\u0647")
        buf.write(u"\u0648\3\2\2\2\u0648\u064a\3\2\2\2\u0649\u064b\5\u00ce")
        buf.write(u"h\2\u064a\u0649\3\2\2\2\u064a\u064b\3\2\2\2\u064b\u00df")
        buf.write(u"\3\2\2\2\u064c\u064e\5\u011e\u0090\2\u064d\u064f\7\21")
        buf.write(u"\2\2\u064e\u064d\3\2\2\2\u064e\u064f\3\2\2\2\u064f\u0651")
        buf.write(u"\3\2\2\2\u0650\u0652\5\u00d4k\2\u0651\u0650\3\2\2\2\u0651")
        buf.write(u"\u0652\3\2\2\2\u0652\u00e1\3\2\2\2\u0653\u0654\br\1\2")
        buf.write(u"\u0654\u0655\5\60\31\2\u0655\u065c\3\2\2\2\u0656\u0657")
        buf.write(u"\f\3\2\2\u0657\u0658\5x=\2\u0658\u0659\5\60\31\2\u0659")
        buf.write(u"\u065b\3\2\2\2\u065a\u0656\3\2\2\2\u065b\u065e\3\2\2")
        buf.write(u"\2\u065c\u065a\3\2\2\2\u065c\u065d\3\2\2\2\u065d\u00e3")
        buf.write(u"\3\2\2\2\u065e\u065c\3\2\2\2\u065f\u0660\bs\1\2\u0660")
        buf.write(u"\u0661\5*\26\2\u0661\u0668\3\2\2\2\u0662\u0663\f\3\2")
        buf.write(u"\2\u0663\u0664\5x=\2\u0664\u0665\5*\26\2\u0665\u0667")
        buf.write(u"\3\2\2\2\u0666\u0662\3\2\2\2\u0667\u066a\3\2\2\2\u0668")
        buf.write(u"\u0666\3\2\2\2\u0668\u0669\3\2\2\2\u0669\u00e5\3\2\2")
        buf.write(u"\2\u066a\u0668\3\2\2\2\u066b\u066c\bt\1\2\u066c\u066d")
        buf.write(u"\5:\36\2\u066d\u0674\3\2\2\2\u066e\u066f\f\3\2\2\u066f")
        buf.write(u"\u0670\5x=\2\u0670\u0671\5:\36\2\u0671\u0673\3\2\2\2")
        buf.write(u"\u0672\u066e\3\2\2\2\u0673\u0676\3\2\2\2\u0674\u0672")
        buf.write(u"\3\2\2\2\u0674\u0675\3\2\2\2\u0675\u00e7\3\2\2\2\u0676")
        buf.write(u"\u0674\3\2\2\2\u0677\u0678\bu\1\2\u0678\u0679\5J&\2\u0679")
        buf.write(u"\u0680\3\2\2\2\u067a\u067b\f\3\2\2\u067b\u067c\5x=\2")
        buf.write(u"\u067c\u067d\5J&\2\u067d\u067f\3\2\2\2\u067e\u067a\3")
        buf.write(u"\2\2\2\u067f\u0682\3\2\2\2\u0680\u067e\3\2\2\2\u0680")
        buf.write(u"\u0681\3\2\2\2\u0681\u00e9\3\2\2\2\u0682\u0680\3\2\2")
        buf.write(u"\2\u0683\u0684\7\27\2\2\u0684\u0685\5\u00ecw\2\u0685")
        buf.write(u"\u0686\7\23\2\2\u0686\u0687\5\u00ecw\2\u0687\u0688\7")
        buf.write(u"\30\2\2\u0688\u0692\3\2\2\2\u0689\u068a\7\27\2\2\u068a")
        buf.write(u"\u068b\5\u00eex\2\u068b\u068c\7\30\2\2\u068c\u0692\3")
        buf.write(u"\2\2\2\u068d\u068e\7)\2\2\u068e\u068f\5\u00eex\2\u068f")
        buf.write(u"\u0690\7\'\2\2\u0690\u0692\3\2\2\2\u0691\u0683\3\2\2")
        buf.write(u"\2\u0691\u0689\3\2\2\2\u0691\u068d\3\2\2\2\u0692\u00eb")
        buf.write(u"\3\2\2\2\u0693\u06a1\7\u008c\2\2\u0694\u06a1\7\u008d")
        buf.write(u"\2\2\u0695\u06a1\7\u0094\2\2\u0696\u06a1\7\u0095\2\2")
        buf.write(u"\u0697\u06a1\7\u008b\2\2\u0698\u06a1\7\u0099\2\2\u0699")
        buf.write(u"\u06a1\7\u0098\2\2\u069a\u06a1\7\u0093\2\2\u069b\u06a1")
        buf.write(u"\7\u0096\2\2\u069c\u06a1\7\u0097\2\2\u069d\u06a1\7\u008a")
        buf.write(u"\2\2\u069e\u06a1\7\u009a\2\2\u069f\u06a1\5~@\2\u06a0")
        buf.write(u"\u0693\3\2\2\2\u06a0\u0694\3\2\2\2\u06a0\u0695\3\2\2")
        buf.write(u"\2\u06a0\u0696\3\2\2\2\u06a0\u0697\3\2\2\2\u06a0\u0698")
        buf.write(u"\3\2\2\2\u06a0\u0699\3\2\2\2\u06a0\u069a\3\2\2\2\u06a0")
        buf.write(u"\u069b\3\2\2\2\u06a0\u069c\3\2\2\2\u06a0\u069d\3\2\2")
        buf.write(u"\2\u06a0\u069e\3\2\2\2\u06a0\u069f\3\2\2\2\u06a1\u00ed")
        buf.write(u"\3\2\2\2\u06a2\u06a3\bx\1\2\u06a3\u06a4\5\u00ecw\2\u06a4")
        buf.write(u"\u06aa\3\2\2\2\u06a5\u06a6\f\3\2\2\u06a6\u06a7\7\22\2")
        buf.write(u"\2\u06a7\u06a9\5\u00ecw\2\u06a8\u06a5\3\2\2\2\u06a9\u06ac")
        buf.write(u"\3\2\2\2\u06aa\u06a8\3\2\2\2\u06aa\u06ab\3\2\2\2\u06ab")
        buf.write(u"\u00ef\3\2\2\2\u06ac\u06aa\3\2\2\2\u06ad\u06b2\5\u00f4")
        buf.write(u"{\2\u06ae\u06b2\5\u00f6|\2\u06af\u06b2\5\u00acW\2\u06b0")
        buf.write(u"\u06b2\5\u00f2z\2\u06b1\u06ad\3\2\2\2\u06b1\u06ae\3\2")
        buf.write(u"\2\2\u06b1\u06af\3\2\2\2\u06b1\u06b0\3\2\2\2\u06b2\u00f1")
        buf.write(u"\3\2\2\2\u06b3\u06b4\t\3\2\2\u06b4\u00f3\3\2\2\2\u06b5")
        buf.write(u"\u06b6\7\25\2\2\u06b6\u06b7\5N(\2\u06b7\u06b8\7\26\2")
        buf.write(u"\2\u06b8\u00f5\3\2\2\2\u06b9\u06bc\5\u00ecw\2\u06ba\u06bc")
        buf.write(u"\5\u00f8}\2\u06bb\u06b9\3\2\2\2\u06bb\u06ba\3\2\2\2\u06bc")
        buf.write(u"\u00f7\3\2\2\2\u06bd\u06c3\5\u0098M\2\u06be\u06c3\5\u0092")
        buf.write(u"J\2\u06bf\u06c3\5\u0094K\2\u06c0\u06c3\5\u00fc\177\2")
        buf.write(u"\u06c1\u06c3\5\u00fa~\2\u06c2\u06bd\3\2\2\2\u06c2\u06be")
        buf.write(u"\3\2\2\2\u06c2\u06bf\3\2\2\2\u06c2\u06c0\3\2\2\2\u06c2")
        buf.write(u"\u06c1\3\2\2\2\u06c3\u00f9\3\2\2\2\u06c4\u06c6\7\25\2")
        buf.write(u"\2\u06c5\u06c7\5\u00fe\u0080\2\u06c6\u06c5\3\2\2\2\u06c6")
        buf.write(u"\u06c7\3\2\2\2\u06c7\u06c8\3\2\2\2\u06c8\u06c9\7\26\2")
        buf.write(u"\2\u06c9\u00fb\3\2\2\2\u06ca\u06cc\7\31\2\2\u06cb\u06cd")
        buf.write(u"\5\u0100\u0081\2\u06cc\u06cb\3\2\2\2\u06cc\u06cd\3\2")
        buf.write(u"\2\2\u06cd\u06ce\3\2\2\2\u06ce\u06cf\7\32\2\2\u06cf\u00fd")
        buf.write(u"\3\2\2\2\u06d0\u06d1\b\u0080\1\2\u06d1\u06d2\5N(\2\u06d2")
        buf.write(u"\u06d8\3\2\2\2\u06d3\u06d4\f\3\2\2\u06d4\u06d5\7\22\2")
        buf.write(u"\2\u06d5\u06d7\5N(\2\u06d6\u06d3\3\2\2\2\u06d7\u06da")
        buf.write(u"\3\2\2\2\u06d8\u06d6\3\2\2\2\u06d8\u06d9\3\2\2\2\u06d9")
        buf.write(u"\u00ff\3\2\2\2\u06da\u06d8\3\2\2\2\u06db\u06dc\b\u0081")
        buf.write(u"\1\2\u06dc\u06dd\5\u0102\u0082\2\u06dd\u06e3\3\2\2\2")
        buf.write(u"\u06de\u06df\f\3\2\2\u06df\u06e0\7\22\2\2\u06e0\u06e2")
        buf.write(u"\5\u0102\u0082\2\u06e1\u06de\3\2\2\2\u06e2\u06e5\3\2")
        buf.write(u"\2\2\u06e3\u06e1\3\2\2\2\u06e3\u06e4\3\2\2\2\u06e4\u0101")
        buf.write(u"\3\2\2\2\u06e5\u06e3\3\2\2\2\u06e6\u06e7\5N(\2\u06e7")
        buf.write(u"\u06e8\7\20\2\2\u06e8\u06e9\5N(\2\u06e9\u0103\3\2\2\2")
        buf.write(u"\u06ea\u06eb\5N(\2\u06eb\u06ec\7\20\2\2\u06ec\u06ed\5")
        buf.write(u"N(\2\u06ed\u06f4\3\2\2\2\u06ee\u06ef\5N(\2\u06ef\u06f0")
        buf.write(u"\7\20\2\2\u06f0\u06f4\3\2\2\2\u06f1\u06f2\7\20\2\2\u06f2")
        buf.write(u"\u06f4\5N(\2\u06f3\u06ea\3\2\2\2\u06f3\u06ee\3\2\2\2")
        buf.write(u"\u06f3\u06f1\3\2\2\2\u06f4\u0105\3\2\2\2\u06f5\u06f6")
        buf.write(u"\5\u00aeX\2\u06f6\u06f7\5\u0114\u008b\2\u06f7\u06f8\5")
        buf.write(u"N(\2\u06f8\u0107\3\2\2\2\u06f9\u06fa\b\u0085\1\2\u06fa")
        buf.write(u"\u06fb\5\u00aeX\2\u06fb\u0700\3\2\2\2\u06fc\u06fd\f\3")
        buf.write(u"\2\2\u06fd\u06ff\5r:\2\u06fe\u06fc\3\2\2\2\u06ff\u0702")
        buf.write(u"\3\2\2\2\u0700\u06fe\3\2\2\2\u0700\u0701\3\2\2\2\u0701")
        buf.write(u"\u0109\3\2\2\2\u0702\u0700\3\2\2\2\u0703\u0704\6\u0086")
        buf.write(u"B\3\u0704\u0705\7\u0090\2\2\u0705\u0708\5\u00be`\2\u0706")
        buf.write(u"\u0708\5N(\2\u0707\u0703\3\2\2\2\u0707\u0706\3\2\2\2")
        buf.write(u"\u0708\u010b\3\2\2\2\u0709\u0710\7!\2\2\u070a\u0710\7")
        buf.write(u"\"\2\2\u070b\u0710\5\u0116\u008c\2\u070c\u0710\5\u0118")
        buf.write(u"\u008d\2\u070d\u0710\5\u011a\u008e\2\u070e\u0710\5\u011c")
        buf.write(u"\u008f\2\u070f\u0709\3\2\2\2\u070f\u070a\3\2\2\2\u070f")
        buf.write(u"\u070b\3\2\2\2\u070f\u070c\3\2\2\2\u070f\u070d\3\2\2")
        buf.write(u"\2\u070f\u070e\3\2\2\2\u0710\u010d\3\2\2\2\u0711\u0712")
        buf.write(u"\7\u0090\2\2\u0712\u0713\6\u0088C\3\u0713\u010f\3\2\2")
        buf.write(u"\2\u0714\u0715\7\u0090\2\2\u0715\u0716\6\u0089D\3\u0716")
        buf.write(u"\u0111\3\2\2\2\u0717\u0718\7\u0090\2\2\u0718\u0719\6")
        buf.write(u"\u008aE\3\u0719\u0113\3\2\2\2\u071a\u071b\7,\2\2\u071b")
        buf.write(u"\u0115\3\2\2\2\u071c\u071d\7#\2\2\u071d\u0117\3\2\2\2")
        buf.write(u"\u071e\u071f\7$\2\2\u071f\u0119\3\2\2\2\u0720\u0721\7")
        buf.write(u"%\2\2\u0721\u011b\3\2\2\2\u0722\u0723\t\4\2\2\u0723\u011d")
        buf.write(u"\3\2\2\2\u0724\u0725\7y\2\2\u0725\u0726\5\u0120\u0091")
        buf.write(u"\2\u0726\u0727\7\21\2\2\u0727\u072c\3\2\2\2\u0728\u0729")
        buf.write(u"\5\u0120\u0091\2\u0729\u072a\7\21\2\2\u072a\u072c\3\2")
        buf.write(u"\2\2\u072b\u0724\3\2\2\2\u072b\u0728\3\2\2\2\u072c\u011f")
        buf.write(u"\3\2\2\2\u072d\u072e\b\u0091\1\2\u072e\u072f\5\u0122")
        buf.write(u"\u0092\2\u072f\u0734\3\2\2\2\u0730\u0731\f\3\2\2\u0731")
        buf.write(u"\u0733\5\u0126\u0094\2\u0732\u0730\3\2\2\2\u0733\u0736")
        buf.write(u"\3\2\2\2\u0734\u0732\3\2\2\2\u0734\u0735\3\2\2\2\u0735")
        buf.write(u"\u0121\3\2\2\2\u0736\u0734\3\2\2\2\u0737\u073e\5\u0124")
        buf.write(u"\u0093\2\u0738\u073e\5\u012e\u0098\2\u0739\u073e\5\u0130")
        buf.write(u"\u0099\2\u073a\u073e\5\u0132\u009a\2\u073b\u073e\5\u0128")
        buf.write(u"\u0095\2\u073c\u073e\5\u012c\u0097\2\u073d\u0737\3\2")
        buf.write(u"\2\2\u073d\u0738\3\2\2\2\u073d\u0739\3\2\2\2\u073d\u073a")
        buf.write(u"\3\2\2\2\u073d\u073b\3\2\2\2\u073d\u073c\3\2\2\2\u073e")
        buf.write(u"\u0123\3\2\2\2\u073f\u0740\5\u00f2z\2\u0740\u0125\3\2")
        buf.write(u"\2\2\u0741\u0742\7\24\2\2\u0742\u0747\5\u0128\u0095\2")
        buf.write(u"\u0743\u0744\7\24\2\2\u0744\u0747\5\u0134\u009b\2\u0745")
        buf.write(u"\u0747\5\u012c\u0097\2\u0746\u0741\3\2\2\2\u0746\u0743")
        buf.write(u"\3\2\2\2\u0746\u0745\3\2\2\2\u0747\u0127\3\2\2\2\u0748")
        buf.write(u"\u0749\5\u0134\u009b\2\u0749\u074b\7\25\2\2\u074a\u074c")
        buf.write(u"\5\u012a\u0096\2\u074b\u074a\3\2\2\2\u074b\u074c\3\2")
        buf.write(u"\2\2\u074c\u074d\3\2\2\2\u074d\u074e\7\26\2\2\u074e\u0129")
        buf.write(u"\3\2\2\2\u074f\u0750\b\u0096\1\2\u0750\u0751\5\u0120")
        buf.write(u"\u0091\2\u0751\u0757\3\2\2\2\u0752\u0753\f\3\2\2\u0753")
        buf.write(u"\u0754\7\22\2\2\u0754\u0756\5\u0120\u0091\2\u0755\u0752")
        buf.write(u"\3\2\2\2\u0756\u0759\3\2\2\2\u0757\u0755\3\2\2\2\u0757")
        buf.write(u"\u0758\3\2\2\2\u0758\u012b\3\2\2\2\u0759\u0757\3\2\2")
        buf.write(u"\2\u075a\u075b\7\27\2\2\u075b\u075c\5\u0120\u0091\2\u075c")
        buf.write(u"\u075d\7\30\2\2\u075d\u012d\3\2\2\2\u075e\u075f\7\25")
        buf.write(u"\2\2\u075f\u0760\5\u0120\u0091\2\u0760\u0761\7\26\2\2")
        buf.write(u"\u0761\u012f\3\2\2\2\u0762\u0763\5\u0134\u009b\2\u0763")
        buf.write(u"\u0131\3\2\2\2\u0764\u076a\7\u0094\2\2\u0765\u076a\7")
        buf.write(u"\u0096\2\2\u0766\u076a\7\u0093\2\2\u0767\u076a\7\u008a")
        buf.write(u"\2\2\u0768\u076a\7\u008b\2\2\u0769\u0764\3\2\2\2\u0769")
        buf.write(u"\u0765\3\2\2\2\u0769\u0766\3\2\2\2\u0769\u0767\3\2\2")
        buf.write(u"\2\u0769\u0768\3\2\2\2\u076a\u0133\3\2\2\2\u076b\u076c")
        buf.write(u"\t\5\2\2\u076c\u0135\3\2\2\2\u076d\u076e\7y\2\2\u076e")
        buf.write(u"\u0771\5\u0138\u009d\2\u076f\u0771\5\u0138\u009d\2\u0770")
        buf.write(u"\u076d\3\2\2\2\u0770\u076f\3\2\2\2\u0771\u0137\3\2\2")
        buf.write(u"\2\u0772\u0773\b\u009d\1\2\u0773\u0774\5\u013a\u009e")
        buf.write(u"\2\u0774\u0779\3\2\2\2\u0775\u0776\f\3\2\2\u0776\u0778")
        buf.write(u"\5\u013c\u009f\2\u0777\u0775\3\2\2\2\u0778\u077b\3\2")
        buf.write(u"\2\2\u0779\u0777\3\2\2\2\u0779\u077a\3\2\2\2\u077a\u0139")
        buf.write(u"\3\2\2\2\u077b\u0779\3\2\2\2\u077c\u0781\5\u0146\u00a4")
        buf.write(u"\2\u077d\u0781\5\u0148\u00a5\2\u077e\u0781\5\u014a\u00a6")
        buf.write(u"\2\u077f\u0781\5\u013e\u00a0\2\u0780\u077c\3\2\2\2\u0780")
        buf.write(u"\u077d\3\2\2\2\u0780\u077e\3\2\2\2\u0780\u077f\3\2\2")
        buf.write(u"\2\u0781\u013b\3\2\2\2\u0782\u0783\7\24\2\2\u0783\u0789")
        buf.write(u"\5\u013e\u00a0\2\u0784\u0785\7\27\2\2\u0785\u0786\5\u0138")
        buf.write(u"\u009d\2\u0786\u0787\7\30\2\2\u0787\u0789\3\2\2\2\u0788")
        buf.write(u"\u0782\3\2\2\2\u0788\u0784\3\2\2\2\u0789\u013d\3\2\2")
        buf.write(u"\2\u078a\u078b\5\u014c\u00a7\2\u078b\u078d\7\25\2\2\u078c")
        buf.write(u"\u078e\5\u0140\u00a1\2\u078d\u078c\3\2\2\2\u078d\u078e")
        buf.write(u"\3\2\2\2\u078e\u078f\3\2\2\2\u078f\u0790\7\26\2\2\u0790")
        buf.write(u"\u013f\3\2\2\2\u0791\u0798\5\u0142\u00a2\2\u0792\u0798")
        buf.write(u"\5\u0144\u00a3\2\u0793\u0794\5\u0142\u00a2\2\u0794\u0795")
        buf.write(u"\7\22\2\2\u0795\u0796\5\u0144\u00a3\2\u0796\u0798\3\2")
        buf.write(u"\2\2\u0797\u0791\3\2\2\2\u0797\u0792\3\2\2\2\u0797\u0793")
        buf.write(u"\3\2\2\2\u0798\u0141\3\2\2\2\u0799\u079a\b\u00a2\1\2")
        buf.write(u"\u079a\u079b\5\u0138\u009d\2\u079b\u07a1\3\2\2\2\u079c")
        buf.write(u"\u079d\f\3\2\2\u079d\u079e\7\22\2\2\u079e\u07a0\5\u0138")
        buf.write(u"\u009d\2\u079f\u079c\3\2\2\2\u07a0\u07a3\3\2\2\2\u07a1")
        buf.write(u"\u079f\3\2\2\2\u07a1\u07a2\3\2\2\2\u07a2\u0143\3\2\2")
        buf.write(u"\2\u07a3\u07a1\3\2\2\2\u07a4\u07a5\b\u00a3\1\2\u07a5")
        buf.write(u"\u07a6\5\u014c\u00a7\2\u07a6\u07a7\7,\2\2\u07a7\u07a8")
        buf.write(u"\5\u0138\u009d\2\u07a8\u07b1\3\2\2\2\u07a9\u07aa\f\3")
        buf.write(u"\2\2\u07aa\u07ab\7\22\2\2\u07ab\u07ac\5\u014c\u00a7\2")
        buf.write(u"\u07ac\u07ad\7,\2\2\u07ad\u07ae\5\u0138\u009d\2\u07ae")
        buf.write(u"\u07b0\3\2\2\2\u07af\u07a9\3\2\2\2\u07b0\u07b3\3\2\2")
        buf.write(u"\2\u07b1\u07af\3\2\2\2\u07b1\u07b2\3\2\2\2\u07b2\u0145")
        buf.write(u"\3\2\2\2\u07b3\u07b1\3\2\2\2\u07b4\u07b5\7\25\2\2\u07b5")
        buf.write(u"\u07b6\5\u0138\u009d\2\u07b6\u07b7\7\26\2\2\u07b7\u0147")
        buf.write(u"\3\2\2\2\u07b8\u07b9\b\u00a5\1\2\u07b9\u07bc\7\u0092")
        buf.write(u"\2\2\u07ba\u07bc\5\u014c\u00a7\2\u07bb\u07b8\3\2\2\2")
        buf.write(u"\u07bb\u07ba\3\2\2\2\u07bc\u07c2\3\2\2\2\u07bd\u07be")
        buf.write(u"\f\3\2\2\u07be\u07bf\7\24\2\2\u07bf\u07c1\5\u014c\u00a7")
        buf.write(u"\2\u07c0\u07bd\3\2\2\2\u07c1\u07c4\3\2\2\2\u07c2\u07c0")
        buf.write(u"\3\2\2\2\u07c2\u07c3\3\2\2\2\u07c3\u0149\3\2\2\2\u07c4")
        buf.write(u"\u07c2\3\2\2\2\u07c5\u07cb\7\u0094\2\2\u07c6\u07cb\7")
        buf.write(u"\u0096\2\2\u07c7\u07cb\7\u0093\2\2\u07c8\u07cb\7\u008a")
        buf.write(u"\2\2\u07c9\u07cb\7\u008b\2\2\u07ca\u07c5\3\2\2\2\u07ca")
        buf.write(u"\u07c6\3\2\2\2\u07ca\u07c7\3\2\2\2\u07ca\u07c8\3\2\2")
        buf.write(u"\2\u07ca\u07c9\3\2\2\2\u07cb\u014b\3\2\2\2\u07cc\u07cd")
        buf.write(u"\t\6\2\2\u07cd\u014d\3\2\2\2\u07ce\u07cf\7y\2\2\u07cf")
        buf.write(u"\u07d0\5\u0150\u00a9\2\u07d0\u07d1\7\21\2\2\u07d1\u07d6")
        buf.write(u"\3\2\2\2\u07d2\u07d3\5\u0150\u00a9\2\u07d3\u07d4\7\21")
        buf.write(u"\2\2\u07d4\u07d6\3\2\2\2\u07d5\u07ce\3\2\2\2\u07d5\u07d2")
        buf.write(u"\3\2\2\2\u07d6\u014f\3\2\2\2\u07d7\u07d8\b\u00a9\1\2")
        buf.write(u"\u07d8\u07d9\5\u0152\u00aa\2\u07d9\u07de\3\2\2\2\u07da")
        buf.write(u"\u07db\f\3\2\2\u07db\u07dd\5\u0156\u00ac\2\u07dc\u07da")
        buf.write(u"\3\2\2\2\u07dd\u07e0\3\2\2\2\u07de\u07dc\3\2\2\2\u07de")
        buf.write(u"\u07df\3\2\2\2\u07df\u0151\3\2\2\2\u07e0\u07de\3\2\2")
        buf.write(u"\2\u07e1\u07e6\5\u0154\u00ab\2\u07e2\u07e6\5\u015e\u00b0")
        buf.write(u"\2\u07e3\u07e6\5\u0160\u00b1\2\u07e4\u07e6\5\u0164\u00b3")
        buf.write(u"\2\u07e5\u07e1\3\2\2\2\u07e5\u07e2\3\2\2\2\u07e5\u07e3")
        buf.write(u"\3\2\2\2\u07e5\u07e4\3\2\2\2\u07e6\u0153\3\2\2\2\u07e7")
        buf.write(u"\u07e8\5\u00f2z\2\u07e8\u0155\3\2\2\2\u07e9\u07ea\7\24")
        buf.write(u"\2\2\u07ea\u07ed\5\u0158\u00ad\2\u07eb\u07ed\5\u015c")
        buf.write(u"\u00af\2\u07ec\u07e9\3\2\2\2\u07ec\u07eb\3\2\2\2\u07ed")
        buf.write(u"\u0157\3\2\2\2\u07ee\u07ef\5\u0166\u00b4\2\u07ef\u07f1")
        buf.write(u"\7\25\2\2\u07f0\u07f2\5\u015a\u00ae\2\u07f1\u07f0\3\2")
        buf.write(u"\2\2\u07f1\u07f2\3\2\2\2\u07f2\u07f3\3\2\2\2\u07f3\u07f4")
        buf.write(u"\7\26\2\2\u07f4\u0159\3\2\2\2\u07f5\u07f6\b\u00ae\1\2")
        buf.write(u"\u07f6\u07f7\5\u0150\u00a9\2\u07f7\u07fd\3\2\2\2\u07f8")
        buf.write(u"\u07f9\f\3\2\2\u07f9\u07fa\7\22\2\2\u07fa\u07fc\5\u0150")
        buf.write(u"\u00a9\2\u07fb\u07f8\3\2\2\2\u07fc\u07ff\3\2\2\2\u07fd")
        buf.write(u"\u07fb\3\2\2\2\u07fd\u07fe\3\2\2\2\u07fe\u015b\3\2\2")
        buf.write(u"\2\u07ff\u07fd\3\2\2\2\u0800\u0801\7\27\2\2\u0801\u0802")
        buf.write(u"\5\u0150\u00a9\2\u0802\u0803\7\30\2\2\u0803\u015d\3\2")
        buf.write(u"\2\2\u0804\u0805\7\25\2\2\u0805\u0806\5\u0150\u00a9\2")
        buf.write(u"\u0806\u0807\7\26\2\2\u0807\u015f\3\2\2\2\u0808\u0809")
        buf.write(u"\b\u00b1\1\2\u0809\u080a\5\u0166\u00b4\2\u080a\u0810")
        buf.write(u"\3\2\2\2\u080b\u080c\f\3\2\2\u080c\u080d\7\24\2\2\u080d")
        buf.write(u"\u080f\5\u0166\u00b4\2\u080e\u080b\3\2\2\2\u080f\u0812")
        buf.write(u"\3\2\2\2\u0810\u080e\3\2\2\2\u0810\u0811\3\2\2\2\u0811")
        buf.write(u"\u0161\3\2\2\2\u0812\u0810\3\2\2\2\u0813\u0814\b\u00b2")
        buf.write(u"\1\2\u0814\u0815\5\u0160\u00b1\2\u0815\u081a\3\2\2\2")
        buf.write(u"\u0816\u0817\f\3\2\2\u0817\u0819\7\u0092\2\2\u0818\u0816")
        buf.write(u"\3\2\2\2\u0819\u081c\3\2\2\2\u081a\u0818\3\2\2\2\u081a")
        buf.write(u"\u081b\3\2\2\2\u081b\u0163\3\2\2\2\u081c\u081a\3\2\2")
        buf.write(u"\2\u081d\u0823\7\u0094\2\2\u081e\u0823\7\u0096\2\2\u081f")
        buf.write(u"\u0823\7\u0093\2\2\u0820\u0823\7\u008a\2\2\u0821\u0823")
        buf.write(u"\7\u008b\2\2\u0822\u081d\3\2\2\2\u0822\u081e\3\2\2\2")
        buf.write(u"\u0822\u081f\3\2\2\2\u0822\u0820\3\2\2\2\u0822\u0821")
        buf.write(u"\3\2\2\2\u0823\u0165\3\2\2\2\u0824\u0825\t\7\2\2\u0825")
        buf.write(u"\u0167\3\2\2\2\u0826\u0827\7y\2\2\u0827\u0828\5\u016a")
        buf.write(u"\u00b6\2\u0828\u0829\7\21\2\2\u0829\u082e\3\2\2\2\u082a")
        buf.write(u"\u082b\5\u016a\u00b6\2\u082b\u082c\7\21\2\2\u082c\u082e")
        buf.write(u"\3\2\2\2\u082d\u0826\3\2\2\2\u082d\u082a\3\2\2\2\u082e")
        buf.write(u"\u0169\3\2\2\2\u082f\u0830\b\u00b6\1\2\u0830\u0831\5")
        buf.write(u"\u016c\u00b7\2\u0831\u0836\3\2\2\2\u0832\u0833\f\3\2")
        buf.write(u"\2\u0833\u0835\5\u0170\u00b9\2\u0834\u0832\3\2\2\2\u0835")
        buf.write(u"\u0838\3\2\2\2\u0836\u0834\3\2\2\2\u0836\u0837\3\2\2")
        buf.write(u"\2\u0837\u016b\3\2\2\2\u0838\u0836\3\2\2\2\u0839\u083e")
        buf.write(u"\5\u016e\u00b8\2\u083a\u083e\5\u0178\u00bd\2\u083b\u083e")
        buf.write(u"\5\u017a\u00be\2\u083c\u083e\5\u017c\u00bf\2\u083d\u0839")
        buf.write(u"\3\2\2\2\u083d\u083a\3\2\2\2\u083d\u083b\3\2\2\2\u083d")
        buf.write(u"\u083c\3\2\2\2\u083e\u016d\3\2\2\2\u083f\u0840\5\u00f2")
        buf.write(u"z\2\u0840\u016f\3\2\2\2\u0841\u0842\7\24\2\2\u0842\u0845")
        buf.write(u"\5\u0172\u00ba\2\u0843\u0845\5\u0176\u00bc\2\u0844\u0841")
        buf.write(u"\3\2\2\2\u0844\u0843\3\2\2\2\u0845\u0171\3\2\2\2\u0846")
        buf.write(u"\u0847\5\u017e\u00c0\2\u0847\u0849\7\25\2\2\u0848\u084a")
        buf.write(u"\5\u0174\u00bb\2\u0849\u0848\3\2\2\2\u0849\u084a\3\2")
        buf.write(u"\2\2\u084a\u084b\3\2\2\2\u084b\u084c\7\26\2\2\u084c\u0173")
        buf.write(u"\3\2\2\2\u084d\u084e\b\u00bb\1\2\u084e\u084f\5\u016a")
        buf.write(u"\u00b6\2\u084f\u0855\3\2\2\2\u0850\u0851\f\3\2\2\u0851")
        buf.write(u"\u0852\7\22\2\2\u0852\u0854\5\u016a\u00b6\2\u0853\u0850")
        buf.write(u"\3\2\2\2\u0854\u0857\3\2\2\2\u0855\u0853\3\2\2\2\u0855")
        buf.write(u"\u0856\3\2\2\2\u0856\u0175\3\2\2\2\u0857\u0855\3\2\2")
        buf.write(u"\2\u0858\u0859\7\27\2\2\u0859\u085a\5\u016a\u00b6\2\u085a")
        buf.write(u"\u085b\7\30\2\2\u085b\u0177\3\2\2\2\u085c\u085d\7\25")
        buf.write(u"\2\2\u085d\u085e\5\u016a\u00b6\2\u085e\u085f\7\26\2\2")
        buf.write(u"\u085f\u0179\3\2\2\2\u0860\u0861\b\u00be\1\2\u0861\u0864")
        buf.write(u"\7\u0092\2\2\u0862\u0864\5\u017e\u00c0\2\u0863\u0860")
        buf.write(u"\3\2\2\2\u0863\u0862\3\2\2\2\u0864\u086a\3\2\2\2\u0865")
        buf.write(u"\u0866\f\3\2\2\u0866\u0867\7\24\2\2\u0867\u0869\5\u017e")
        buf.write(u"\u00c0\2\u0868\u0865\3\2\2\2\u0869\u086c\3\2\2\2\u086a")
        buf.write(u"\u0868\3\2\2\2\u086a\u086b\3\2\2\2\u086b\u017b\3\2\2")
        buf.write(u"\2\u086c\u086a\3\2\2\2\u086d\u0873\7\u0094\2\2\u086e")
        buf.write(u"\u0873\7\u0096\2\2\u086f\u0873\7\u0093\2\2\u0870\u0873")
        buf.write(u"\7\u008a\2\2\u0871\u0873\7\u008b\2\2\u0872\u086d\3\2")
        buf.write(u"\2\2\u0872\u086e\3\2\2\2\u0872\u086f\3\2\2\2\u0872\u0870")
        buf.write(u"\3\2\2\2\u0872\u0871\3\2\2\2\u0873\u017d\3\2\2\2\u0874")
        buf.write(u"\u0875\t\b\2\2\u0875\u017f\3\2\2\2\u00aa\u0187\u018e")
        buf.write(u"\u01ad\u01b6\u01be\u01c9\u01d2\u01e2\u01eb\u01f2\u01ff")
        buf.write(u"\u0226\u0234\u0243\u0251\u0265\u0272\u0274\u027f\u0284")
        buf.write(u"\u028e\u0293\u02a4\u02a9\u02c5\u02cc\u02d1\u02d5\u02e6")
        buf.write(u"\u02ea\u02ed\u030e\u0321\u0328\u034a\u0353\u036a\u037a")
        buf.write(u"\u037f\u0387\u0390\u03a7\u03ab\u03c7\u0427\u0429\u0433")
        buf.write(u"\u0448\u0458\u045d\u0463\u0468\u046a\u046d\u0473\u0475")
        buf.write(u"\u0477\u0495\u049c\u049e\u04a3\u04a5\u04b0\u04c3\u04cc")
        buf.write(u"\u04d2\u04d7\u04de\u04e6\u04f4\u04fc\u0502\u050d\u0519")
        buf.write(u"\u0524\u0531\u0535\u053b\u0547\u055b\u055d\u0562\u056e")
        buf.write(u"\u0579\u0583\u0588\u058d\u059d\u05a2\u05a5\u05a9\u05ae")
        buf.write(u"\u05b5\u05c0\u05c2\u05ce\u05d6\u05e1\u05e6\u05f2\u05f6")
        buf.write(u"\u0600\u0608\u060e\u0615\u061a\u0624\u062b\u0636\u0643")
        buf.write(u"\u0647\u064a\u064e\u0651\u065c\u0668\u0674\u0680\u0691")
        buf.write(u"\u06a0\u06aa\u06b1\u06bb\u06c2\u06c6\u06cc\u06d8\u06e3")
        buf.write(u"\u06f3\u0700\u0707\u070f\u072b\u0734\u073d\u0746\u074b")
        buf.write(u"\u0757\u0769\u0770\u0779\u0780\u0788\u078d\u0797\u07a1")
        buf.write(u"\u07b1\u07bb\u07c2\u07ca\u07d5\u07de\u07e5\u07ec\u07f1")
        buf.write(u"\u07fd\u0810\u081a\u0822\u082d\u0836\u083d\u0844\u0849")
        buf.write(u"\u0855\u0863\u086a\u0872")
        return buf.getvalue()
		

class EParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"'Java:'", 
                     u"'C#:'", u"'Python2:'", u"'Python3:'", u"'JavaScript:'", 
                     u"'Swift:'", u"':'", u"';'", u"','", u"'..'", u"'.'", 
                     u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'?'", 
                     u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'\\'", u"'%'", u"'>'", u"'>='", u"'<'", 
                     u"'<='", u"'<>'", u"'='", u"'!='", u"'=='", u"'~='", 
                     u"'~'", u"'<-'", u"'->'", u"'Boolean'", u"'Character'", 
                     u"'Text'", u"'Integer'", u"'Decimal'", u"'Date'", u"'Time'", 
                     u"'DateTime'", u"'Period'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"'attr'", u"'attribute'", 
                     u"'attributes'", u"'bindings'", u"'case'", u"'catch'", 
                     u"'category'", u"'class'", u"'close'", u"'contains'", 
                     u"'def'", u"'default'", u"'define'", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
                     u"'methods'", u"'modulo'", u"'mutable'", u"'native'", 
                     u"'None'", u"'not'", u"<INVALID>", u"'null'", u"'on'", 
                     u"'open'", u"'operator'", u"'or'", u"'otherwise'", 
                     u"'pass'", u"'raise'", u"'read'", u"'receiving'", u"'resource'", 
                     u"'return'", u"'returning'", u"'self'", u"'setter'", 
                     u"'singleton'", u"'sorted'", u"'switch'", u"'test'", 
                     u"'this'", u"'throw'", u"'to'", u"'try'", u"'with'", 
                     u"'when'", u"'where'", u"'while'", u"'write'", u"<INVALID>", 
                     u"<INVALID>", u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"INDENT", u"DEDENT", u"LF_TAB", u"LF_MORE", 
                      u"LF", u"TAB", u"WS", u"JAVA", u"CSHARP", u"PYTHON2", 
                      u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", u"SEMI", 
                      u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", u"LBRAK", 
                      u"RBRAK", u"LCURL", u"RCURL", u"QMARK", u"XMARK", 
                      u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", u"MINUS", 
                      u"STAR", u"SLASH", u"BSLASH", u"PERCENT", u"GT", u"GTE", 
                      u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", u"EQ2", u"TEQ", 
                      u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", u"CHARACTER", 
                      u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", u"TIME", 
                      u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", u"DOCUMENT", 
                      u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", u"ANY", u"AS", 
                      u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", u"BINDINGS", 
                      u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DO", 
                      u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FINALLY", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INVOKE", u"IS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"OPEN", u"OPERATOR", 
                      u"OR", u"OTHERWISE", u"PASS", u"RAISE", u"READ", u"RECEIVING", 
                      u"RESOURCE", u"RETURN", u"RETURNING", u"SELF", u"SETTER", 
                      u"SINGLETON", u"SORTED", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"WITH", u"WHEN", u"WHERE", 
                      u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", u"CHAR_LITERAL", 
                      u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"INTEGER_LITERAL", 
                      u"HEXA_LITERAL", u"DECIMAL_LITERAL", u"DATETIME_LITERAL", 
                      u"TIME_LITERAL", u"DATE_LITERAL", u"PERIOD_LITERAL", 
                      u"COMMENT" ]

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
    RULE_getter_method_declaration = 10
    RULE_native_category_declaration = 11
    RULE_native_resource_declaration = 12
    RULE_native_category_bindings = 13
    RULE_native_category_binding_list = 14
    RULE_attribute_list = 15
    RULE_abstract_method_declaration = 16
    RULE_concrete_method_declaration = 17
    RULE_native_method_declaration = 18
    RULE_test_method_declaration = 19
    RULE_assertion = 20
    RULE_full_argument_list = 21
    RULE_typed_argument = 22
    RULE_statement = 23
    RULE_method_call_statement = 24
    RULE_with_resource_statement = 25
    RULE_with_singleton_statement = 26
    RULE_switch_statement = 27
    RULE_switch_case_statement = 28
    RULE_for_each_statement = 29
    RULE_do_while_statement = 30
    RULE_while_statement = 31
    RULE_if_statement = 32
    RULE_else_if_statement_list = 33
    RULE_raise_statement = 34
    RULE_try_statement = 35
    RULE_catch_statement = 36
    RULE_return_statement = 37
    RULE_expression = 38
    RULE_unresolved_expression = 39
    RULE_unresolved_selector = 40
    RULE_invocation_expression = 41
    RULE_invocation_trailer = 42
    RULE_instance_expression = 43
    RULE_instance_selector = 44
    RULE_document_expression = 45
    RULE_constructor_expression = 46
    RULE_read_expression = 47
    RULE_write_statement = 48
    RULE_ambiguous_expression = 49
    RULE_fetch_expression = 50
    RULE_sorted_expression = 51
    RULE_argument_assignment_list = 52
    RULE_with_argument_assignment_list = 53
    RULE_argument_assignment = 54
    RULE_assign_instance_statement = 55
    RULE_child_instance = 56
    RULE_assign_tuple_statement = 57
    RULE_lfs = 58
    RULE_lfp = 59
    RULE_indent = 60
    RULE_dedent = 61
    RULE_null_literal = 62
    RULE_declaration_list = 63
    RULE_declarations = 64
    RULE_declaration = 65
    RULE_resource_declaration = 66
    RULE_enum_declaration = 67
    RULE_native_symbol_list = 68
    RULE_category_symbol_list = 69
    RULE_symbol_list = 70
    RULE_attribute_constraint = 71
    RULE_list_literal = 72
    RULE_set_literal = 73
    RULE_expression_list = 74
    RULE_range_literal = 75
    RULE_typedef = 76
    RULE_primary_type = 77
    RULE_native_type = 78
    RULE_category_type = 79
    RULE_code_type = 80
    RULE_document_type = 81
    RULE_category_declaration = 82
    RULE_type_identifier_list = 83
    RULE_method_identifier = 84
    RULE_identifier = 85
    RULE_variable_identifier = 86
    RULE_type_identifier = 87
    RULE_symbol_identifier = 88
    RULE_argument_list = 89
    RULE_argument = 90
    RULE_operator_argument = 91
    RULE_named_argument = 92
    RULE_code_argument = 93
    RULE_category_or_any_type = 94
    RULE_any_type = 95
    RULE_member_method_declaration_list = 96
    RULE_member_method_declaration = 97
    RULE_native_member_method_declaration_list = 98
    RULE_native_member_method_declaration = 99
    RULE_native_category_binding = 100
    RULE_python_category_binding = 101
    RULE_python_module = 102
    RULE_module_token = 103
    RULE_javascript_category_binding = 104
    RULE_javascript_module = 105
    RULE_variable_identifier_list = 106
    RULE_method_declaration = 107
    RULE_native_statement_list = 108
    RULE_native_statement = 109
    RULE_python_native_statement = 110
    RULE_javascript_native_statement = 111
    RULE_statement_list = 112
    RULE_assertion_list = 113
    RULE_switch_case_statement_list = 114
    RULE_catch_statement_list = 115
    RULE_literal_collection = 116
    RULE_atomic_literal = 117
    RULE_literal_list_literal = 118
    RULE_selectable_expression = 119
    RULE_this_expression = 120
    RULE_parenthesis_expression = 121
    RULE_literal_expression = 122
    RULE_collection_literal = 123
    RULE_tuple_literal = 124
    RULE_dict_literal = 125
    RULE_expression_tuple = 126
    RULE_dict_entry_list = 127
    RULE_dict_entry = 128
    RULE_slice_arguments = 129
    RULE_assign_variable_statement = 130
    RULE_assignable_instance = 131
    RULE_is_expression = 132
    RULE_operator = 133
    RULE_key_token = 134
    RULE_value_token = 135
    RULE_symbols_token = 136
    RULE_assign = 137
    RULE_multiply = 138
    RULE_divide = 139
    RULE_idivide = 140
    RULE_modulo = 141
    RULE_javascript_statement = 142
    RULE_javascript_expression = 143
    RULE_javascript_primary_expression = 144
    RULE_javascript_this_expression = 145
    RULE_javascript_selector_expression = 146
    RULE_javascript_method_expression = 147
    RULE_javascript_arguments = 148
    RULE_javascript_item_expression = 149
    RULE_javascript_parenthesis_expression = 150
    RULE_javascript_identifier_expression = 151
    RULE_javascript_literal_expression = 152
    RULE_javascript_identifier = 153
    RULE_python_statement = 154
    RULE_python_expression = 155
    RULE_python_primary_expression = 156
    RULE_python_selector_expression = 157
    RULE_python_method_expression = 158
    RULE_python_argument_list = 159
    RULE_python_ordinal_argument_list = 160
    RULE_python_named_argument_list = 161
    RULE_python_parenthesis_expression = 162
    RULE_python_identifier_expression = 163
    RULE_python_literal_expression = 164
    RULE_python_identifier = 165
    RULE_java_statement = 166
    RULE_java_expression = 167
    RULE_java_primary_expression = 168
    RULE_java_this_expression = 169
    RULE_java_selector_expression = 170
    RULE_java_method_expression = 171
    RULE_java_arguments = 172
    RULE_java_item_expression = 173
    RULE_java_parenthesis_expression = 174
    RULE_java_identifier_expression = 175
    RULE_java_class_identifier_expression = 176
    RULE_java_literal_expression = 177
    RULE_java_identifier = 178
    RULE_csharp_statement = 179
    RULE_csharp_expression = 180
    RULE_csharp_primary_expression = 181
    RULE_csharp_this_expression = 182
    RULE_csharp_selector_expression = 183
    RULE_csharp_method_expression = 184
    RULE_csharp_arguments = 185
    RULE_csharp_item_expression = 186
    RULE_csharp_parenthesis_expression = 187
    RULE_csharp_identifier_expression = 188
    RULE_csharp_literal_expression = 189
    RULE_csharp_identifier = 190

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"getter_method_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"full_argument_list", 
                   u"typed_argument", u"statement", u"method_call_statement", 
                   u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"return_statement", u"expression", 
                   u"unresolved_expression", u"unresolved_selector", u"invocation_expression", 
                   u"invocation_trailer", u"instance_expression", u"instance_selector", 
                   u"document_expression", u"constructor_expression", u"read_expression", 
                   u"write_statement", u"ambiguous_expression", u"fetch_expression", 
                   u"sorted_expression", u"argument_assignment_list", u"with_argument_assignment_list", 
                   u"argument_assignment", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"lfs", 
                   u"lfp", u"indent", u"dedent", u"null_literal", u"declaration_list", 
                   u"declarations", u"declaration", u"resource_declaration", 
                   u"enum_declaration", u"native_symbol_list", u"category_symbol_list", 
                   u"symbol_list", u"attribute_constraint", u"list_literal", 
                   u"set_literal", u"expression_list", u"range_literal", 
                   u"typedef", u"primary_type", u"native_type", u"category_type", 
                   u"code_type", u"document_type", u"category_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"type_identifier", u"symbol_identifier", 
                   u"argument_list", u"argument", u"operator_argument", 
                   u"named_argument", u"code_argument", u"category_or_any_type", 
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"module_token", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"method_declaration", 
                   u"native_statement_list", u"native_statement", u"python_native_statement", 
                   u"javascript_native_statement", u"statement_list", u"assertion_list", 
                   u"switch_case_statement_list", u"catch_statement_list", 
                   u"literal_collection", u"atomic_literal", u"literal_list_literal", 
                   u"selectable_expression", u"this_expression", u"parenthesis_expression", 
                   u"literal_expression", u"collection_literal", u"tuple_literal", 
                   u"dict_literal", u"expression_tuple", u"dict_entry_list", 
                   u"dict_entry", u"slice_arguments", u"assign_variable_statement", 
                   u"assignable_instance", u"is_expression", u"operator", 
                   u"key_token", u"value_token", u"symbols_token", u"assign", 
                   u"multiply", u"divide", u"idivide", u"modulo", u"javascript_statement", 
                   u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_selector_expression", 
                   u"javascript_method_expression", u"javascript_arguments", 
                   u"javascript_item_expression", u"javascript_parenthesis_expression", 
                   u"javascript_identifier_expression", u"javascript_literal_expression", 
                   u"javascript_identifier", u"python_statement", u"python_expression", 
                   u"python_primary_expression", u"python_selector_expression", 
                   u"python_method_expression", u"python_argument_list", 
                   u"python_ordinal_argument_list", u"python_named_argument_list", 
                   u"python_parenthesis_expression", u"python_identifier_expression", 
                   u"python_literal_expression", u"python_identifier", u"java_statement", 
                   u"java_expression", u"java_primary_expression", u"java_this_expression", 
                   u"java_selector_expression", u"java_method_expression", 
                   u"java_arguments", u"java_item_expression", u"java_parenthesis_expression", 
                   u"java_identifier_expression", u"java_class_identifier_expression", 
                   u"java_literal_expression", u"java_identifier", u"csharp_statement", 
                   u"csharp_expression", u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_selector_expression", u"csharp_method_expression", 
                   u"csharp_arguments", u"csharp_item_expression", u"csharp_parenthesis_expression", 
                   u"csharp_identifier_expression", u"csharp_literal_expression", 
                   u"csharp_identifier" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    LF_TAB=3
    LF_MORE=4
    LF=5
    TAB=6
    WS=7
    JAVA=8
    CSHARP=9
    PYTHON2=10
    PYTHON3=11
    JAVASCRIPT=12
    SWIFT=13
    COLON=14
    SEMI=15
    COMMA=16
    RANGE=17
    DOT=18
    LPAR=19
    RPAR=20
    LBRAK=21
    RBRAK=22
    LCURL=23
    RCURL=24
    QMARK=25
    XMARK=26
    AMP=27
    AMP2=28
    PIPE=29
    PIPE2=30
    PLUS=31
    MINUS=32
    STAR=33
    SLASH=34
    BSLASH=35
    PERCENT=36
    GT=37
    GTE=38
    LT=39
    LTE=40
    LTGT=41
    EQ=42
    XEQ=43
    EQ2=44
    TEQ=45
    TILDE=46
    LARROW=47
    RARROW=48
    BOOLEAN=49
    CHARACTER=50
    TEXT=51
    INTEGER=52
    DECIMAL=53
    DATE=54
    TIME=55
    DATETIME=56
    PERIOD=57
    METHOD_T=58
    CODE=59
    DOCUMENT=60
    ABSTRACT=61
    ALL=62
    ALWAYS=63
    AND=64
    ANY=65
    AS=66
    ATTR=67
    ATTRIBUTE=68
    ATTRIBUTES=69
    BINDINGS=70
    CASE=71
    CATCH=72
    CATEGORY=73
    CLASS=74
    CLOSE=75
    CONTAINS=76
    DEF=77
    DEFAULT=78
    DEFINE=79
    DO=80
    DOING=81
    EACH=82
    ELSE=83
    ENUM=84
    ENUMERATED=85
    EXCEPT=86
    EXECUTE=87
    EXPECTING=88
    EXTENDS=89
    FETCH=90
    FINALLY=91
    FOR=92
    FROM=93
    GETTER=94
    IF=95
    IN=96
    INVOKE=97
    IS=98
    MATCHING=99
    METHOD=100
    METHODS=101
    MODULO=102
    MUTABLE=103
    NATIVE=104
    NONE=105
    NOT=106
    NOTHING=107
    NULL=108
    ON=109
    OPEN=110
    OPERATOR=111
    OR=112
    OTHERWISE=113
    PASS=114
    RAISE=115
    READ=116
    RECEIVING=117
    RESOURCE=118
    RETURN=119
    RETURNING=120
    SELF=121
    SETTER=122
    SINGLETON=123
    SORTED=124
    SWITCH=125
    TEST=126
    THIS=127
    THROW=128
    TO=129
    TRY=130
    WITH=131
    WHEN=132
    WHERE=133
    WHILE=134
    WRITE=135
    BOOLEAN_LITERAL=136
    CHAR_LITERAL=137
    MIN_INTEGER=138
    MAX_INTEGER=139
    SYMBOL_IDENTIFIER=140
    TYPE_IDENTIFIER=141
    VARIABLE_IDENTIFIER=142
    NATIVE_IDENTIFIER=143
    DOLLAR_IDENTIFIER=144
    TEXT_LITERAL=145
    INTEGER_LITERAL=146
    HEXA_LITERAL=147
    DECIMAL_LITERAL=148
    DATETIME_LITERAL=149
    TIME_LITERAL=150
    DATE_LITERAL=151
    PERIOD_LITERAL=152
    COMMENT=153

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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


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
            self.state = 382
            self.match(EParser.DEFINE)
            self.state = 383 
            localctx.name = self.type_identifier()
            self.state = 384
            self.match(EParser.AS)
            self.state = 385
            self.match(EParser.COLON)
            self.state = 386
            self.match(EParser.ENUMERATED)
            self.state = 389
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 387
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 388 
                localctx.derived = self.type_identifier()

            else:
                raise NoViableAltException(self)

            self.state = 396
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 391 
                localctx.attrs = self.attribute_list()
                self.state = 392
                self.match(EParser.COMMA)
                self.state = 393
                self.match(EParser.AND)
                pass

            elif la_ == 2:
                self.state = 395
                self.match(EParser.WITH)
                pass


            self.state = 398 
            self.symbols_token()
            self.state = 399
            self.match(EParser.COLON)
            self.state = 400 
            self.indent()
            self.state = 401 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 402 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def ENUMERATED(self):
            return self.getToken(EParser.ENUMERATED, 0)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def symbols_token(self):
            return self.getTypedRuleContext(EParser.Symbols_tokenContext,0)


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
            self.state = 404
            self.match(EParser.DEFINE)
            self.state = 405 
            localctx.name = self.type_identifier()
            self.state = 406
            self.match(EParser.AS)
            self.state = 407
            self.match(EParser.COLON)
            self.state = 408
            self.match(EParser.ENUMERATED)
            self.state = 409 
            localctx.typ = self.native_type()
            self.state = 410
            self.match(EParser.WITH)
            self.state = 411 
            self.symbols_token()
            self.state = 412
            self.match(EParser.COLON)
            self.state = 413 
            self.indent()
            self.state = 414 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 415 
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
            self.state = 417 
            localctx.name = self.symbol_identifier()
            self.state = 418
            self.match(EParser.WITH)
            self.state = 419 
            localctx.exp = self.expression(0)
            self.state = 420
            self.match(EParser.AS)
            self.state = 421 
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423 
            localctx.name = self.symbol_identifier()
            self.state = 424 
            localctx.args = self.with_argument_assignment_list(0)
            self.state = 427
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 425
                self.match(EParser.AND)
                self.state = 426 
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
            self.name = None # Variable_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext

        def DEFINE(self):
            return self.getToken(EParser.DEFINE, 0)

        def AS(self):
            return self.getToken(EParser.AS, 0)

        def COLON(self):
            return self.getToken(EParser.COLON, 0)

        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def attribute_constraint(self):
            return self.getTypedRuleContext(EParser.Attribute_constraintContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(EParser.DEFINE)
            self.state = 430 
            localctx.name = self.variable_identifier()
            self.state = 431
            self.match(EParser.AS)
            self.state = 432
            self.match(EParser.COLON)
            self.state = 433 
            localctx.typ = self.typedef(0)
            self.state = 434
            self.match(EParser.ATTRIBUTE)
            self.state = 436
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 435 
                localctx.match = self.attribute_constraint()


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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

        def derived_list(self):
            return self.getTypedRuleContext(EParser.Derived_listContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(EParser.DEFINE)
            self.state = 439 
            localctx.name = self.type_identifier()
            self.state = 440
            self.match(EParser.AS)
            self.state = 441
            self.match(EParser.COLON)
            self.state = 444
            token = self._input.LA(1)
            if token in [EParser.CATEGORY]:
                self.state = 442
                self.match(EParser.CATEGORY)

            elif token in [EParser.TYPE_IDENTIFIER]:
                self.state = 443 
                localctx.derived = self.derived_list()

            else:
                raise NoViableAltException(self)

            self.state = 464
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 446 
                localctx.attrs = self.attribute_list()
                self.state = 455
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 447
                    self.match(EParser.COMMA)
                    self.state = 448
                    self.match(EParser.AND)
                    self.state = 449
                    self.match(EParser.METHODS)
                    self.state = 450
                    self.match(EParser.COLON)
                    self.state = 451 
                    self.indent()
                    self.state = 452 
                    localctx.methods = self.member_method_declaration_list(0)
                    self.state = 453 
                    self.dedent()



            elif la_ == 2:
                self.state = 457
                self.match(EParser.WITH)
                self.state = 458
                self.match(EParser.METHODS)
                self.state = 459
                self.match(EParser.COLON)
                self.state = 460 
                self.indent()
                self.state = 461 
                localctx.methods = self.member_method_declaration_list(0)
                self.state = 462 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def SINGLETON(self):
            return self.getToken(EParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def WITH(self):
            return self.getToken(EParser.WITH, 0)

        def METHODS(self):
            return self.getToken(EParser.METHODS, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(EParser.DEFINE)
            self.state = 467 
            localctx.name = self.type_identifier()
            self.state = 468
            self.match(EParser.AS)
            self.state = 469
            self.match(EParser.COLON)
            self.state = 470
            self.match(EParser.SINGLETON)
            self.state = 489
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 471 
                localctx.attrs = self.attribute_list()
                self.state = 480
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 472
                    self.match(EParser.COMMA)
                    self.state = 473
                    self.match(EParser.AND)
                    self.state = 474
                    self.match(EParser.METHODS)
                    self.state = 475
                    self.match(EParser.COLON)
                    self.state = 476 
                    self.indent()
                    self.state = 477 
                    localctx.methods = self.member_method_declaration_list(0)
                    self.state = 478 
                    self.dedent()



            elif la_ == 2:
                self.state = 482
                self.match(EParser.WITH)
                self.state = 483
                self.match(EParser.METHODS)
                self.state = 484
                self.match(EParser.COLON)
                self.state = 485 
                self.indent()
                self.state = 486 
                localctx.methods = self.member_method_declaration_list(0)
                self.state = 487 
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



    def derived_list(self):

        localctx = EParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.state = 496
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = EParser.DerivedListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 491 
                localctx.items = self.type_identifier_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.DerivedListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 492 
                localctx.items = self.type_identifier_list(0)
                self.state = 493
                self.match(EParser.AND)
                self.state = 494 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def OPERATOR(self):
            return self.getToken(EParser.OPERATOR, 0)

        def RECEIVING(self):
            return self.getToken(EParser.RECEIVING, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

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
            self.state = 498
            self.match(EParser.DEFINE)
            self.state = 499 
            localctx.op = self.operator()
            self.state = 500
            self.match(EParser.AS)
            self.state = 501
            self.match(EParser.COLON)
            self.state = 502
            self.match(EParser.OPERATOR)
            self.state = 503
            self.match(EParser.RECEIVING)
            self.state = 504
            self.match(EParser.COLON)
            self.state = 505 
            localctx.arg = self.operator_argument()
            self.state = 509
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 506
                self.match(EParser.RETURNING)
                self.state = 507
                self.match(EParser.COLON)
                self.state = 508 
                localctx.typ = self.typedef(0)


            self.state = 511
            self.match(EParser.DOING)
            self.state = 512
            self.match(EParser.COLON)
            self.state = 513 
            self.indent()
            self.state = 514 
            localctx.stmts = self.statement_list(0)
            self.state = 515 
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
            self.state = 517
            self.match(EParser.DEFINE)
            self.state = 518 
            localctx.name = self.variable_identifier()
            self.state = 519
            self.match(EParser.SETTER)
            self.state = 520
            self.match(EParser.DOING)
            self.state = 521
            self.match(EParser.COLON)
            self.state = 522 
            self.indent()
            self.state = 523 
            localctx.stmts = self.statement_list(0)
            self.state = 524 
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
        self.enterRule(localctx, 20, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(EParser.DEFINE)
            self.state = 527 
            localctx.name = self.variable_identifier()
            self.state = 528
            self.match(EParser.GETTER)
            self.state = 529
            self.match(EParser.DOING)
            self.state = 530
            self.match(EParser.COLON)
            self.state = 531 
            self.indent()
            self.state = 532 
            localctx.stmts = self.statement_list(0)
            self.state = 533 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(EParser.CATEGORY, 0)

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
            return EParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = EParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(EParser.DEFINE)
            self.state = 536 
            localctx.name = self.type_identifier()
            self.state = 537
            self.match(EParser.AS)
            self.state = 538
            self.match(EParser.COLON)
            self.state = 539
            self.match(EParser.NATIVE)
            self.state = 540
            self.match(EParser.CATEGORY)
            self.state = 548
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 541 
                localctx.attrs = self.attribute_list()
                self.state = 542
                self.match(EParser.COMMA)
                self.state = 543
                self.match(EParser.AND)
                self.state = 544
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 546
                self.match(EParser.WITH)
                self.state = 547
                self.match(EParser.BINDINGS)
                pass


            self.state = 550
            self.match(EParser.COLON)
            self.state = 551 
            self.indent()
            self.state = 552 
            localctx.bindings = self.native_category_bindings()
            self.state = 553 
            self.dedent()
            self.state = 562
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 554 
                self.lfp()
                self.state = 555
                self.match(EParser.AND)
                self.state = 556
                self.match(EParser.METHODS)
                self.state = 557
                self.match(EParser.COLON)
                self.state = 558 
                self.indent()
                self.state = 559 
                localctx.methods = self.native_member_method_declaration_list(0)
                self.state = 560 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(EParser.RESOURCE, 0)

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
        self.enterRule(localctx, 24, self.RULE_native_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(EParser.DEFINE)
            self.state = 565 
            localctx.name = self.type_identifier()
            self.state = 566
            self.match(EParser.AS)
            self.state = 567
            self.match(EParser.COLON)
            self.state = 568
            self.match(EParser.NATIVE)
            self.state = 569
            self.match(EParser.RESOURCE)
            self.state = 577
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 570 
                localctx.attrs = self.attribute_list()
                self.state = 571
                self.match(EParser.COMMA)
                self.state = 572
                self.match(EParser.AND)
                self.state = 573
                self.match(EParser.BINDINGS)
                pass

            elif la_ == 2:
                self.state = 575
                self.match(EParser.WITH)
                self.state = 576
                self.match(EParser.BINDINGS)
                pass


            self.state = 579
            self.match(EParser.COLON)
            self.state = 580 
            self.indent()
            self.state = 581 
            localctx.bindings = self.native_category_bindings()
            self.state = 582 
            self.dedent()
            self.state = 591
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 583 
                self.lfp()
                self.state = 584
                self.match(EParser.AND)
                self.state = 585
                self.match(EParser.METHODS)
                self.state = 586
                self.match(EParser.COLON)
                self.state = 587 
                self.indent()
                self.state = 588 
                localctx.methods = self.native_member_method_declaration_list(0)
                self.state = 589 
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
        self.enterRule(localctx, 26, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(EParser.DEFINE)
            self.state = 594
            self.match(EParser.CATEGORY)
            self.state = 595
            self.match(EParser.BINDINGS)
            self.state = 596
            self.match(EParser.AS)
            self.state = 597
            self.match(EParser.COLON)
            self.state = 598 
            self.indent()
            self.state = 599 
            localctx.items = self.native_category_binding_list(0)
            self.state = 600 
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



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 603 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 611
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryBindingListItemContext(self, EParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 605
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 606 
                    self.lfp()
                    self.state = 607 
                    localctx.item = self.native_category_binding() 
                self.state = 613
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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



    class AttributeListItemContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTES(self):
            return self.getToken(EParser.ATTRIBUTES, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)

        def AND(self):
            return self.getToken(EParser.AND, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeListItem(self)


    class AttributeListContext(Attribute_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Attribute_listContext)
            super(EParser.AttributeListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(EParser.WITH, 0)
        def ATTRIBUTE(self):
            return self.getToken(EParser.ATTRIBUTE, 0)
        def COLON(self):
            return self.getToken(EParser.COLON, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeList(self)



    def attribute_list(self):

        localctx = EParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attribute_list)
        try:
            self.state = 626
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.match(EParser.WITH)
                self.state = 615
                self.match(EParser.ATTRIBUTE)
                self.state = 616
                self.match(EParser.COLON)
                self.state = 617 
                localctx.item = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.AttributeListItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 618
                self.match(EParser.WITH)
                self.state = 619
                self.match(EParser.ATTRIBUTES)
                self.state = 620
                self.match(EParser.COLON)
                self.state = 621 
                localctx.items = self.variable_identifier_list(0)
                self.state = 624
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 622
                    self.match(EParser.AND)
                    self.state = 623 
                    localctx.item = self.variable_identifier()


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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

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
        self.enterRule(localctx, 32, self.RULE_abstract_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(EParser.DEFINE)
            self.state = 629 
            localctx.name = self.method_identifier()
            self.state = 630
            self.match(EParser.AS)
            self.state = 631
            self.match(EParser.COLON)
            self.state = 632
            self.match(EParser.ABSTRACT)
            self.state = 633
            self.match(EParser.METHOD)
            self.state = 637
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 634
                self.match(EParser.RECEIVING)
                self.state = 635
                self.match(EParser.COLON)
                self.state = 636 
                localctx.args = self.full_argument_list()


            self.state = 642
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 639
                self.match(EParser.RETURNING)
                self.state = 640
                self.match(EParser.COLON)
                self.state = 641 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

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
        self.enterRule(localctx, 34, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.match(EParser.DEFINE)
            self.state = 645 
            localctx.name = self.method_identifier()
            self.state = 646
            self.match(EParser.AS)
            self.state = 647
            self.match(EParser.COLON)
            self.state = 648
            self.match(EParser.METHOD)
            self.state = 652
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 649
                self.match(EParser.RECEIVING)
                self.state = 650
                self.match(EParser.COLON)
                self.state = 651 
                localctx.args = self.full_argument_list()


            self.state = 657
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 654
                self.match(EParser.RETURNING)
                self.state = 655
                self.match(EParser.COLON)
                self.state = 656 
                localctx.typ = self.typedef(0)


            self.state = 659
            self.match(EParser.DOING)
            self.state = 660
            self.match(EParser.COLON)
            self.state = 661 
            self.indent()
            self.state = 662 
            localctx.stmts = self.statement_list(0)
            self.state = 663 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def NATIVE(self):
            return self.getToken(EParser.NATIVE, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

        def indent(self):
            return self.getTypedRuleContext(EParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(EParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(EParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)


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
        self.enterRule(localctx, 36, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.match(EParser.DEFINE)
            self.state = 666 
            localctx.name = self.method_identifier()
            self.state = 667
            self.match(EParser.AS)
            self.state = 668
            self.match(EParser.COLON)
            self.state = 669
            self.match(EParser.NATIVE)
            self.state = 670
            self.match(EParser.METHOD)
            self.state = 674
            _la = self._input.LA(1)
            if _la==EParser.RECEIVING:
                self.state = 671
                self.match(EParser.RECEIVING)
                self.state = 672
                self.match(EParser.COLON)
                self.state = 673 
                localctx.args = self.full_argument_list()


            self.state = 679
            _la = self._input.LA(1)
            if _la==EParser.RETURNING:
                self.state = 676
                self.match(EParser.RETURNING)
                self.state = 677
                self.match(EParser.COLON)
                self.state = 678 
                localctx.typ = self.category_or_any_type()


            self.state = 681
            self.match(EParser.DOING)
            self.state = 682
            self.match(EParser.COLON)
            self.state = 683 
            self.indent()
            self.state = 684 
            localctx.stmts = self.native_statement_list(0)
            self.state = 685 
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

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(EParser.COLON)
            else:
                return self.getToken(EParser.COLON, i)

        def TEST(self):
            return self.getToken(EParser.TEST, 0)

        def METHOD(self):
            return self.getToken(EParser.METHOD, 0)

        def DOING(self):
            return self.getToken(EParser.DOING, 0)

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

        def EXPECTING(self):
            return self.getToken(EParser.EXPECTING, 0)

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
        self.enterRule(localctx, 38, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.match(EParser.DEFINE)
            self.state = 688
            localctx.name = self.match(EParser.TEXT_LITERAL)
            self.state = 689
            self.match(EParser.AS)
            self.state = 690
            self.match(EParser.COLON)
            self.state = 691
            self.match(EParser.TEST)
            self.state = 692
            self.match(EParser.METHOD)
            self.state = 693
            self.match(EParser.DOING)
            self.state = 694
            self.match(EParser.COLON)
            self.state = 695 
            self.indent()
            self.state = 696 
            localctx.stmts = self.statement_list(0)
            self.state = 697 
            self.dedent()
            self.state = 698 
            self.lfp()
            self.state = 699
            self.match(EParser.AND)
            self.state = 700
            self.match(EParser.EXPECTING)
            self.state = 701
            self.match(EParser.COLON)
            self.state = 707
            token = self._input.LA(1)
            if token in [EParser.LF]:
                self.state = 702 
                self.indent()
                self.state = 703 
                localctx.exps = self.assertion_list(0)
                self.state = 704 
                self.dedent()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                self.state = 706 
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
        self.enterRule(localctx, 40, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709 
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
        self.enterRule(localctx, 42, self.RULE_full_argument_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711 
            localctx.items = self.argument_list(0)
            self.state = 714
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 712
                self.match(EParser.AND)
                self.state = 713 
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
        self.enterRule(localctx, 44, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716 
            localctx.typ = self.category_or_any_type()
            self.state = 717 
            localctx.name = self.variable_identifier()
            self.state = 719
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 718 
                localctx.attrs = self.attribute_list()


            self.state = 723
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 721
                self.match(EParser.EQ)
                self.state = 722 
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



    def statement(self):

        localctx = EParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 740
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = EParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 725 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 2:
                localctx = EParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 726 
                localctx.stmt = self.method_call_statement()
                pass

            elif la_ == 3:
                localctx = EParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 727 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = EParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 728 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 5:
                localctx = EParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 729 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 6:
                localctx = EParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 730 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 7:
                localctx = EParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 731 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 8:
                localctx = EParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 732 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 9:
                localctx = EParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 733 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 10:
                localctx = EParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 734 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 11:
                localctx = EParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 735 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 12:
                localctx = EParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 736 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 13:
                localctx = EParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 737 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 14:
                localctx = EParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 738 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 15:
                localctx = EParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 739 
                localctx.decl = self.concrete_method_declaration()
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



    def method_call_statement(self):

        localctx = EParser.Method_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_call_statement)
        try:
            self.state = 747
            token = self._input.LA(1)
            if token in [EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.UnresolvedWithArgsStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 742 
                localctx.exp = self.unresolved_expression(0)
                self.state = 744
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 743 
                    localctx.args = self.argument_assignment_list()



            elif token in [EParser.INVOKE]:
                localctx = EParser.InvokeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 746 
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
        self.enterRule(localctx, 50, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            self.match(EParser.WITH)
            self.state = 750 
            localctx.stmt = self.assign_variable_statement()
            self.state = 751
            self.match(EParser.COMMA)
            self.state = 752
            self.match(EParser.DO)
            self.state = 753
            self.match(EParser.COLON)
            self.state = 754 
            self.indent()
            self.state = 755 
            localctx.stmts = self.statement_list(0)
            self.state = 756 
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
        self.enterRule(localctx, 52, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            self.match(EParser.WITH)
            self.state = 759 
            localctx.typ = self.type_identifier()
            self.state = 760
            self.match(EParser.COMMA)
            self.state = 761
            self.match(EParser.DO)
            self.state = 762
            self.match(EParser.COLON)
            self.state = 763 
            self.indent()
            self.state = 764 
            localctx.stmts = self.statement_list(0)
            self.state = 765 
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
        self.enterRule(localctx, 54, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 767
            self.match(EParser.SWITCH)
            self.state = 768
            self.match(EParser.ON)
            self.state = 769 
            localctx.exp = self.expression(0)
            self.state = 770
            self.match(EParser.COLON)
            self.state = 771 
            self.indent()
            self.state = 772 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 780
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 773 
                self.lfp()
                self.state = 774
                self.match(EParser.OTHERWISE)
                self.state = 775
                self.match(EParser.COLON)
                self.state = 776 
                self.indent()
                self.state = 777 
                localctx.stmts = self.statement_list(0)
                self.state = 778 
                self.dedent()


            self.state = 782 
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
        self.enterRule(localctx, 56, self.RULE_switch_case_statement)
        try:
            self.state = 799
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = EParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 784
                self.match(EParser.WHEN)
                self.state = 785 
                localctx.exp = self.atomic_literal()
                self.state = 786
                self.match(EParser.COLON)
                self.state = 787 
                self.indent()
                self.state = 788 
                localctx.stmts = self.statement_list(0)
                self.state = 789 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = EParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 791
                self.match(EParser.WHEN)
                self.state = 792
                self.match(EParser.IN)
                self.state = 793 
                localctx.exp = self.literal_collection()
                self.state = 794
                self.match(EParser.COLON)
                self.state = 795 
                self.indent()
                self.state = 796 
                localctx.stmts = self.statement_list(0)
                self.state = 797 
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
        self.enterRule(localctx, 58, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 801
            self.match(EParser.FOR)
            self.state = 802
            self.match(EParser.EACH)
            self.state = 803 
            localctx.name1 = self.variable_identifier()
            self.state = 806
            _la = self._input.LA(1)
            if _la==EParser.COMMA:
                self.state = 804
                self.match(EParser.COMMA)
                self.state = 805 
                localctx.name2 = self.variable_identifier()


            self.state = 808
            self.match(EParser.IN)
            self.state = 809 
            localctx.source = self.expression(0)
            self.state = 810
            self.match(EParser.COLON)
            self.state = 811 
            self.indent()
            self.state = 812 
            localctx.stmts = self.statement_list(0)
            self.state = 813 
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
        self.enterRule(localctx, 60, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.match(EParser.DO)
            self.state = 816
            self.match(EParser.COLON)
            self.state = 817 
            self.indent()
            self.state = 818 
            localctx.stmts = self.statement_list(0)
            self.state = 819 
            self.dedent()
            self.state = 820 
            self.lfp()
            self.state = 821
            self.match(EParser.WHILE)
            self.state = 822 
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
        self.enterRule(localctx, 62, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 824
            self.match(EParser.WHILE)
            self.state = 825 
            localctx.exp = self.expression(0)
            self.state = 826
            self.match(EParser.COLON)
            self.state = 827 
            self.indent()
            self.state = 828 
            localctx.stmts = self.statement_list(0)
            self.state = 829 
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
        self.enterRule(localctx, 64, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 831
            self.match(EParser.IF)
            self.state = 832 
            localctx.exp = self.expression(0)
            self.state = 833
            self.match(EParser.COLON)
            self.state = 834 
            self.indent()
            self.state = 835 
            localctx.stmts = self.statement_list(0)
            self.state = 836 
            self.dedent()
            self.state = 840
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 837 
                self.lfp()
                self.state = 838 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 849
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 842 
                self.lfp()
                self.state = 843
                self.match(EParser.ELSE)
                self.state = 844
                self.match(EParser.COLON)
                self.state = 845 
                self.indent()
                self.state = 846 
                localctx.elseStmts = self.statement_list(0)
                self.state = 847 
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 852
            self.match(EParser.ELSE)
            self.state = 853
            self.match(EParser.IF)
            self.state = 854 
            localctx.exp = self.expression(0)
            self.state = 855
            self.match(EParser.COLON)
            self.state = 856 
            self.indent()
            self.state = 857 
            localctx.stmts = self.statement_list(0)
            self.state = 858 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 872
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ElseIfStatementListItemContext(self, EParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 860
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 861 
                    self.lfp()
                    self.state = 862
                    self.match(EParser.ELSE)
                    self.state = 863
                    self.match(EParser.IF)
                    self.state = 864 
                    localctx.exp = self.expression(0)
                    self.state = 865
                    self.match(EParser.COLON)
                    self.state = 866 
                    self.indent()
                    self.state = 867 
                    localctx.stmts = self.statement_list(0)
                    self.state = 868 
                    self.dedent() 
                self.state = 874
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 875
            self.match(EParser.RAISE)
            self.state = 876 
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
        self.enterRule(localctx, 70, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            self.match(EParser.SWITCH)
            self.state = 879
            self.match(EParser.ON)
            self.state = 880 
            localctx.name = self.variable_identifier()
            self.state = 881
            self.match(EParser.DOING)
            self.state = 882
            self.match(EParser.COLON)
            self.state = 883 
            self.indent()
            self.state = 884 
            localctx.stmts = self.statement_list(0)
            self.state = 885 
            self.dedent()
            self.state = 886 
            self.lfs()
            self.state = 888
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 887 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 901
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 893
                token = self._input.LA(1)
                if token in [EParser.OTHERWISE]:
                    self.state = 890
                    self.match(EParser.OTHERWISE)

                elif token in [EParser.WHEN]:
                    self.state = 891
                    self.match(EParser.WHEN)
                    self.state = 892
                    self.match(EParser.ANY)

                else:
                    raise NoViableAltException(self)

                self.state = 895
                self.match(EParser.COLON)
                self.state = 896 
                self.indent()
                self.state = 897 
                localctx.anyStmts = self.statement_list(0)
                self.state = 898 
                self.dedent()
                self.state = 899 
                self.lfs()


            self.state = 910
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 903
                self.match(EParser.ALWAYS)
                self.state = 904
                self.match(EParser.COLON)
                self.state = 905 
                self.indent()
                self.state = 906 
                localctx.finalStmts = self.statement_list(0)
                self.state = 907 
                self.dedent()
                self.state = 908 
                self.lfs()


            self.state = 912 
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
        self.enterRule(localctx, 72, self.RULE_catch_statement)
        try:
            self.state = 933
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = EParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 914
                self.match(EParser.WHEN)
                self.state = 915 
                localctx.name = self.symbol_identifier()
                self.state = 916
                self.match(EParser.COLON)
                self.state = 917 
                self.indent()
                self.state = 918 
                localctx.stmts = self.statement_list(0)
                self.state = 919 
                self.dedent()
                self.state = 920 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = EParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 922
                self.match(EParser.WHEN)
                self.state = 923
                self.match(EParser.IN)
                self.state = 924
                self.match(EParser.LBRAK)
                self.state = 925 
                localctx.exp = self.symbol_list(0)
                self.state = 926
                self.match(EParser.RBRAK)
                self.state = 927
                self.match(EParser.COLON)
                self.state = 928 
                self.indent()
                self.state = 929 
                localctx.stmts = self.statement_list(0)
                self.state = 930 
                self.dedent()
                self.state = 931 
                self.lfs()
                pass


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
        self.enterRule(localctx, 74, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 935
            self.match(EParser.RETURN)
            self.state = 937
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 936 
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


    class ReadExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(EParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitReadExpression(self)


    class FetchExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a EParser.ExpressionContext)
            super(EParser.FetchExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_expressionContext
            self.copyFrom(ctx)

        def fetch_expression(self):
            return self.getTypedRuleContext(EParser.Fetch_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetchExpression(self)


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



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 965
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = EParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 940
                self.match(EParser.MINUS)
                self.state = 941 
                localctx.exp = self.expression(38)
                pass

            elif la_ == 2:
                localctx = EParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 942
                self.match(EParser.NOT)
                self.state = 943 
                localctx.exp = self.expression(37)
                pass

            elif la_ == 3:
                localctx = EParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 944
                self.match(EParser.CODE)
                self.state = 945
                self.match(EParser.COLON)
                self.state = 946 
                localctx.exp = self.expression(10)
                pass

            elif la_ == 4:
                localctx = EParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 947 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 5:
                localctx = EParser.UnresolvedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 948 
                localctx.exp = self.unresolved_expression(0)
                pass

            elif la_ == 6:
                localctx = EParser.MethodCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 949 
                localctx.exp = self.unresolved_expression(0)
                self.state = 950 
                localctx.args = self.argument_assignment_list()
                pass

            elif la_ == 7:
                localctx = EParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 952
                self.match(EParser.EXECUTE)
                self.state = 953
                self.match(EParser.COLON)
                self.state = 954 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 8:
                localctx = EParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 955
                self.match(EParser.METHOD_T)
                self.state = 956
                self.match(EParser.COLON)
                self.state = 957 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 9:
                localctx = EParser.DocumentExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 958 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 10:
                localctx = EParser.ConstructorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 959 
                localctx.exp = self.constructor_expression()
                pass

            elif la_ == 11:
                localctx = EParser.FetchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 960 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 12:
                localctx = EParser.ReadExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 961 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 13:
                localctx = EParser.SortedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 962 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 14:
                localctx = EParser.AmbiguousExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 963 
                localctx.exp = self.ambiguous_expression()
                pass

            elif la_ == 15:
                localctx = EParser.InvocationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 964 
                localctx.exp = self.invocation_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1063
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1061
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = EParser.MultiplyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 967
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 968 
                        self.multiply()
                        self.state = 969 
                        localctx.right = self.expression(37)
                        pass

                    elif la_ == 2:
                        localctx = EParser.DivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 971
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 972 
                        self.divide()
                        self.state = 973 
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 3:
                        localctx = EParser.ModuloExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 975
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 976 
                        self.modulo()
                        self.state = 977 
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 4:
                        localctx = EParser.IntDivideExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 979
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 980 
                        self.idivide()
                        self.state = 981 
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 5:
                        localctx = EParser.AddExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 983
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 984
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==EParser.PLUS or _la==EParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 985 
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 6:
                        localctx = EParser.LessThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 986
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 987
                        self.match(EParser.LT)
                        self.state = 988 
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 7:
                        localctx = EParser.LessThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 989
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 990
                        self.match(EParser.LTE)
                        self.state = 991 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 8:
                        localctx = EParser.GreaterThanExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 992
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 993
                        self.match(EParser.GT)
                        self.state = 994 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 9:
                        localctx = EParser.GreaterThanOrEqualExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 995
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 996
                        self.match(EParser.GTE)
                        self.state = 997 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 10:
                        localctx = EParser.EqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 998
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 999
                        self.match(EParser.EQ)
                        self.state = 1000 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 11:
                        localctx = EParser.NotEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1001
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1002
                        self.match(EParser.LTGT)
                        self.state = 1003 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 12:
                        localctx = EParser.RoughlyEqualsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1004
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1005
                        self.match(EParser.TILDE)
                        self.state = 1006 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 13:
                        localctx = EParser.OrExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1007
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1008
                        self.match(EParser.OR)
                        self.state = 1009 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 14:
                        localctx = EParser.AndExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1010
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1011
                        self.match(EParser.AND)
                        self.state = 1012 
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 15:
                        localctx = EParser.TernaryExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1013
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1014
                        self.match(EParser.IF)
                        self.state = 1015 
                        localctx.test = self.expression(0)
                        self.state = 1016
                        self.match(EParser.ELSE)
                        self.state = 1017 
                        localctx.ifFalse = self.expression(21)
                        pass

                    elif la_ == 16:
                        localctx = EParser.InExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1019
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1020
                        self.match(EParser.IN)
                        self.state = 1021 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 17:
                        localctx = EParser.ContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1022
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1023
                        self.match(EParser.CONTAINS)
                        self.state = 1024 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 18:
                        localctx = EParser.ContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1025
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1026
                        self.match(EParser.CONTAINS)
                        self.state = 1027
                        self.match(EParser.ALL)
                        self.state = 1028 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 19:
                        localctx = EParser.ContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1029
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1030
                        self.match(EParser.CONTAINS)
                        self.state = 1031
                        self.match(EParser.ANY)
                        self.state = 1032 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 20:
                        localctx = EParser.NotInExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1033
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1034
                        self.match(EParser.NOT)
                        self.state = 1035
                        self.match(EParser.IN)
                        self.state = 1036 
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 21:
                        localctx = EParser.NotContainsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1037
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1038
                        self.match(EParser.NOT)
                        self.state = 1039
                        self.match(EParser.CONTAINS)
                        self.state = 1040 
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 22:
                        localctx = EParser.NotContainsAllExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1041
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1042
                        self.match(EParser.NOT)
                        self.state = 1043
                        self.match(EParser.CONTAINS)
                        self.state = 1044
                        self.match(EParser.ALL)
                        self.state = 1045 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 23:
                        localctx = EParser.NotContainsAnyExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1046
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1047
                        self.match(EParser.NOT)
                        self.state = 1048
                        self.match(EParser.CONTAINS)
                        self.state = 1049
                        self.match(EParser.ANY)
                        self.state = 1050 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 24:
                        localctx = EParser.IsNotExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1051
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1052
                        self.match(EParser.IS)
                        self.state = 1053
                        self.match(EParser.NOT)
                        self.state = 1054 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 25:
                        localctx = EParser.IsExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1055
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1056
                        self.match(EParser.IS)
                        self.state = 1057 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = EParser.CastExpressionContext(self, EParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1058
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1059
                        self.match(EParser.AS)
                        self.state = 1060 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1065
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_unresolved_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.UnresolvedIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1067 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1073
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.UnresolvedSelectorContext(self, EParser.Unresolved_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unresolved_expression)
                    self.state = 1069
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1070 
                    localctx.selector = self.unresolved_selector() 
                self.state = 1075
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_unresolved_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1076
            if not self.wasNot(EParser.WS):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
            self.state = 1077
            self.match(EParser.DOT)
            self.state = 1078 
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
        self.enterRule(localctx, 82, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1080
            self.match(EParser.INVOKE)
            self.state = 1081
            self.match(EParser.COLON)
            self.state = 1082 
            localctx.name = self.variable_identifier()
            self.state = 1083 
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
        self.enterRule(localctx, 84, self.RULE_invocation_trailer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1085
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



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1088 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1094
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SelectorExpressionContext(self, EParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1090
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1091 
                    localctx.selector = self.instance_selector() 
                self.state = 1096
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_instance_selector)
        try:
            self.state = 1110
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1097
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1098
                self.match(EParser.DOT)
                self.state = 1099 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1100
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1101
                self.match(EParser.LBRAK)
                self.state = 1102 
                localctx.xslice = self.slice_arguments()
                self.state = 1103
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1105
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1106
                self.match(EParser.LBRAK)
                self.state = 1107 
                localctx.exp = self.expression(0)
                self.state = 1108
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

        def document_type(self):
            return self.getTypedRuleContext(EParser.Document_typeContext,0)


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
        self.enterRule(localctx, 90, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1112 
            self.document_type()
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



    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Category_typeContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)
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


    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Constructor_expressionContext)
            super(EParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Category_typeContext
            self.firstArg = None # ExpressionContext
            self.args = None # With_argument_assignment_listContext
            self.arg = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)
        def category_type(self):
            return self.getTypedRuleContext(EParser.Category_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)

        def MUTABLE(self):
            return self.getToken(EParser.MUTABLE, 0)
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



    def constructor_expression(self):

        localctx = EParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1141
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = EParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1115
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1114
                    self.match(EParser.MUTABLE)


                self.state = 1117 
                localctx.typ = self.category_type()
                self.state = 1118
                self.match(EParser.FROM)
                self.state = 1119 
                localctx.firstArg = self.expression(0)
                self.state = 1128
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 1121
                    _la = self._input.LA(1)
                    if _la==EParser.COMMA:
                        self.state = 1120
                        self.match(EParser.COMMA)


                    self.state = 1123 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1126
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        self.state = 1124
                        self.match(EParser.AND)
                        self.state = 1125 
                        localctx.arg = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1131
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1130
                    self.match(EParser.MUTABLE)


                self.state = 1133 
                localctx.typ = self.category_type()
                self.state = 1139
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 1134 
                    localctx.args = self.with_argument_assignment_list(0)
                    self.state = 1137
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        self.state = 1135
                        self.match(EParser.AND)
                        self.state = 1136 
                        localctx.arg = self.argument_assignment()




                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(EParser.READ, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = EParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1143
            self.match(EParser.READ)
            self.state = 1144
            self.match(EParser.FROM)
            self.state = 1145 
            localctx.source = self.expression(0)
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
        self.enterRule(localctx, 96, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1147
            self.match(EParser.WRITE)
            self.state = 1148 
            localctx.what = self.expression(0)
            self.state = 1149
            self.match(EParser.TO)
            self.state = 1150 
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
        self.enterRule(localctx, 98, self.RULE_ambiguous_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152 
            localctx.method = self.unresolved_expression(0)
            self.state = 1153
            self.match(EParser.MINUS)
            self.state = 1154 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Fetch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext

        def FETCH(self):
            return self.getToken(EParser.FETCH, 0)

        def ANY(self):
            return self.getToken(EParser.ANY, 0)

        def FROM(self):
            return self.getToken(EParser.FROM, 0)

        def WHERE(self):
            return self.getToken(EParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EParser.RULE_fetch_expression

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterFetch_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitFetch_expression(self)




    def fetch_expression(self):

        localctx = EParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_fetch_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156
            self.match(EParser.FETCH)
            self.state = 1157
            self.match(EParser.ANY)
            self.state = 1158 
            localctx.name = self.variable_identifier()
            self.state = 1159
            self.match(EParser.FROM)
            self.state = 1160 
            localctx.source = self.expression(0)
            self.state = 1161
            self.match(EParser.WHERE)
            self.state = 1162 
            localctx.xfilter = self.expression(0)
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
        self.enterRule(localctx, 102, self.RULE_sorted_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1164
            self.match(EParser.SORTED)
            self.state = 1165 
            localctx.source = self.instance_expression(0)
            self.state = 1171
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 1166
                self.match(EParser.WITH)
                self.state = 1167 
                localctx.key = self.instance_expression(0)
                self.state = 1168
                self.match(EParser.AS)
                self.state = 1169 
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
        self.enterRule(localctx, 104, self.RULE_argument_assignment_list)
        try:
            self.state = 1187
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = EParser.ArgumentAssignmentListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1173
                if not self.was(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.was(EParser.WS)")
                self.state = 1174 
                localctx.exp = self.expression(0)
                self.state = 1180
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 1175 
                    localctx.items = self.with_argument_assignment_list(0)
                    self.state = 1178
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        self.state = 1176
                        self.match(EParser.AND)
                        self.state = 1177 
                        localctx.item = self.argument_assignment()




                pass

            elif la_ == 2:
                localctx = EParser.ArgumentAssignmentListNoExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1182 
                localctx.items = self.with_argument_assignment_list(0)
                self.state = 1185
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 1183
                    self.match(EParser.AND)
                    self.state = 1184 
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_with_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentAssignmentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1190
            self.match(EParser.WITH)
            self.state = 1191 
            localctx.item = self.argument_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentAssignmentListItemContext(self, EParser.With_argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_with_argument_assignment_list)
                    self.state = 1193
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1194
                    self.match(EParser.COMMA)
                    self.state = 1195 
                    localctx.item = self.argument_assignment() 
                self.state = 1200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

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
        self.enterRule(localctx, 108, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1201 
            localctx.exp = self.expression(0)
            self.state = 1202
            self.match(EParser.AS)
            self.state = 1203 
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
        self.enterRule(localctx, 110, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205 
            localctx.inst = self.assignable_instance(0)
            self.state = 1206 
            self.assign()
            self.state = 1207 
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
        self.enterRule(localctx, 112, self.RULE_child_instance)
        try:
            self.state = 1217
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = EParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1209
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1210
                self.match(EParser.DOT)
                self.state = 1211 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = EParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1212
                if not self.wasNot(EParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(EParser.WS)")
                self.state = 1213
                self.match(EParser.LBRAK)
                self.state = 1214 
                localctx.exp = self.expression(0)
                self.state = 1215
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
        self.enterRule(localctx, 114, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1219 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1220 
            self.assign()
            self.state = 1221 
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
        self.enterRule(localctx, 116, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1223
                    self.match(EParser.LF) 
                self.state = 1228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
        self.enterRule(localctx, 118, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1230 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1229
                self.match(EParser.LF)
                self.state = 1232 
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
        self.enterRule(localctx, 120, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1234
                self.match(EParser.LF)
                self.state = 1237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EParser.LF):
                    break

            self.state = 1239
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
        self.enterRule(localctx, 122, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EParser.LF:
                self.state = 1241
                self.match(EParser.LF)
                self.state = 1246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1247
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
        self.enterRule(localctx, 124, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1249
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
            self.items = None # DeclarationsContext
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
        self.enterRule(localctx, 126, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = EParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1252
            _la = self._input.LA(1)
            if _la==EParser.DEFINE:
                self.state = 1251 
                localctx.items = self.declarations(0)


            self.state = 1254 
            self.lfs()
            self.state = 1255
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


        def getRuleIndex(self):
            return EParser.RULE_declarations

     
        def copyFrom(self, ctx):
            super(EParser.DeclarationsContext, self).copyFrom(ctx)


    class DeclarationListContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationsContext)
            super(EParser.DeclarationListContext, self).__init__(parser)
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(EParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclarationList(self)


    class DeclarationListItemContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationsContext)
            super(EParser.DeclarationListItemContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def declarations(self):
            return self.getTypedRuleContext(EParser.DeclarationsContext,0)

        def declaration(self):
            return self.getTypedRuleContext(EParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDeclarationListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDeclarationListItem(self)



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1258 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DeclarationListItemContext(self, EParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1260
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1261 
                    self.lfp()
                    self.state = 1262 
                    localctx.item = self.declaration() 
                self.state = 1268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_declaration

     
        def copyFrom(self, ctx):
            super(EParser.DeclarationContext, self).copyFrom(ctx)



    class CategoryDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.CategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Category_declarationContext
            self.copyFrom(ctx)

        def category_declaration(self):
            return self.getTypedRuleContext(EParser.Category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryDeclaration(self)


    class ResourceDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.ResourceDeclarationContext, self).__init__(parser)
            self.decl = None # Resource_declarationContext
            self.copyFrom(ctx)

        def resource_declaration(self):
            return self.getTypedRuleContext(EParser.Resource_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterResourceDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitResourceDeclaration(self)


    class AttributeDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.AttributeDeclarationContext, self).__init__(parser)
            self.decl = None # Attribute_declarationContext
            self.copyFrom(ctx)

        def attribute_declaration(self):
            return self.getTypedRuleContext(EParser.Attribute_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAttributeDeclaration(self)


    class MethodDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.MethodDeclarationContext, self).__init__(parser)
            self.decl = None # Method_declarationContext
            self.copyFrom(ctx)

        def method_declaration(self):
            return self.getTypedRuleContext(EParser.Method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodDeclaration(self)


    class EnumDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx): # actually a EParser.DeclarationContext)
            super(EParser.EnumDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_declarationContext
            self.copyFrom(ctx)

        def enum_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnumDeclaration(self)



    def declaration(self):

        localctx = EParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_declaration)
        try:
            self.state = 1274
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                localctx = EParser.AttributeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1269 
                localctx.decl = self.attribute_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.CategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1270 
                localctx.decl = self.category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.ResourceDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1271 
                localctx.decl = self.resource_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.EnumDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1272 
                localctx.decl = self.enum_declaration()
                pass

            elif la_ == 5:
                localctx = EParser.MethodDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1273 
                localctx.decl = self.method_declaration()
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
            self.decl = None # Native_resource_declarationContext

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
        self.enterRule(localctx, 132, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1276 
            localctx.decl = self.native_resource_declaration()
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


        def getRuleIndex(self):
            return EParser.RULE_enum_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Enum_declarationContext, self).copyFrom(ctx)



    class EnumNativeDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Enum_declarationContext)
            super(EParser.EnumNativeDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_native_declarationContext
            self.copyFrom(ctx)

        def enum_native_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_native_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnumNativeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnumNativeDeclaration(self)


    class EnumCategoryDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Enum_declarationContext)
            super(EParser.EnumCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_category_declarationContext
            self.copyFrom(ctx)

        def enum_category_declaration(self):
            return self.getTypedRuleContext(EParser.Enum_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterEnumCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitEnumCategoryDeclaration(self)



    def enum_declaration(self):

        localctx = EParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_enum_declaration)
        try:
            self.state = 1280
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = EParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1278 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1279 
                localctx.decl = self.enum_native_declaration()
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


        def getRuleIndex(self):
            return EParser.RULE_native_symbol_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_symbol_listContext, self).copyFrom(ctx)


    class NativeSymbolListContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_symbol_listContext)
            super(EParser.NativeSymbolListContext, self).__init__(parser)
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def native_symbol(self):
            return self.getTypedRuleContext(EParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeSymbolList(self)


    class NativeSymbolListItemContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_symbol_listContext)
            super(EParser.NativeSymbolListItemContext, self).__init__(parser)
            self.items = None # Native_symbol_listContext
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_symbol_list(self):
            return self.getTypedRuleContext(EParser.Native_symbol_listContext,0)

        def native_symbol(self):
            return self.getTypedRuleContext(EParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeSymbolListItem(self)



    def native_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1283 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeSymbolListItemContext(self, EParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1285
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1286 
                    self.lfp()
                    self.state = 1287 
                    localctx.item = self.native_symbol() 
                self.state = 1293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_category_symbol_list

     
        def copyFrom(self, ctx):
            super(EParser.Category_symbol_listContext, self).copyFrom(ctx)


    class CategorySymbolListItemContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_symbol_listContext)
            super(EParser.CategorySymbolListItemContext, self).__init__(parser)
            self.items = None # Category_symbol_listContext
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def category_symbol_list(self):
            return self.getTypedRuleContext(EParser.Category_symbol_listContext,0)

        def category_symbol(self):
            return self.getTypedRuleContext(EParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategorySymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategorySymbolListItem(self)


    class CategorySymbolListContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_symbol_listContext)
            super(EParser.CategorySymbolListContext, self).__init__(parser)
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def category_symbol(self):
            return self.getTypedRuleContext(EParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategorySymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategorySymbolList(self)



    def category_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Category_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1295 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategorySymbolListItemContext(self, EParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1297
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1298 
                    self.lfp()
                    self.state = 1299 
                    localctx.item = self.category_symbol() 
                self.state = 1305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_symbol_list

     
        def copyFrom(self, ctx):
            super(EParser.Symbol_listContext, self).copyFrom(ctx)


    class SymbolListContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Symbol_listContext)
            super(EParser.SymbolListContext, self).__init__(parser)
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolList(self)


    class SymbolListItemContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Symbol_listContext)
            super(EParser.SymbolListItemContext, self).__init__(parser)
            self.items = None # Symbol_listContext
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(EParser.Symbol_listContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(EParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSymbolListItem(self)



    def symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1307 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SymbolListItemContext(self, EParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1309
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1310
                    self.match(EParser.COMMA)
                    self.state = 1311 
                    localctx.item = self.symbol_identifier() 
                self.state = 1316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(EParser.Attribute_constraintContext, self).copyFrom(ctx)



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



    def attribute_constraint(self):

        localctx = EParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_attribute_constraint)
        try:
            self.state = 1327
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                localctx = EParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1317
                self.match(EParser.IN)
                self.state = 1318 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = EParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1319
                self.match(EParser.IN)
                self.state = 1320 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = EParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1321
                self.match(EParser.IN)
                self.state = 1322 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = EParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1323
                self.match(EParser.MATCHING)
                self.state = 1324
                localctx.text = self.match(EParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = EParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1325
                self.match(EParser.MATCHING)
                self.state = 1326 
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
            self.items = None # Expression_listContext

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)

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
        self.enterRule(localctx, 144, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1329
            self.match(EParser.LBRAK)
            self.state = 1331
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1330 
                localctx.items = self.expression_list(0)


            self.state = 1333
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
            self.items = None # Expression_listContext

        def LT(self):
            return self.getToken(EParser.LT, 0)

        def GT(self):
            return self.getToken(EParser.GT, 0)

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
        self.enterRule(localctx, 146, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1335
            self.match(EParser.LT)
            self.state = 1337
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1336 
                localctx.items = self.expression_list(0)


            self.state = 1339
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


        def getRuleIndex(self):
            return EParser.RULE_expression_list

     
        def copyFrom(self, ctx):
            super(EParser.Expression_listContext, self).copyFrom(ctx)


    class ValueListItemContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_listContext)
            super(EParser.ValueListItemContext, self).__init__(parser)
            self.items = None # Expression_listContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def expression_list(self):
            return self.getTypedRuleContext(EParser.Expression_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueListItem(self)


    class ValueListContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_listContext)
            super(EParser.ValueListContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueList(self)



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1342 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueListItemContext(self, EParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1344
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1345
                    self.match(EParser.COMMA)
                    self.state = 1346 
                    localctx.item = self.expression(0) 
                self.state = 1351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 150, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1352
            self.match(EParser.LBRAK)
            self.state = 1353 
            localctx.low = self.expression(0)
            self.state = 1354
            self.match(EParser.RANGE)
            self.state = 1355 
            localctx.high = self.expression(0)
            self.state = 1356
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



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 152
        self.enterRecursionRule(localctx, 152, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1359 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1369
                    la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                    if la_ == 1:
                        localctx = EParser.SetTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1361
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1362
                        self.match(EParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = EParser.ListTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1363
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1364
                        self.match(EParser.LBRAK)
                        self.state = 1365
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = EParser.DictTypeContext(self, EParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1366
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1367
                        self.match(EParser.LCURL)
                        self.state = 1368
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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



    def primary_type(self):

        localctx = EParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_primary_type)
        try:
            self.state = 1376
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE]:
                localctx = EParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1374 
                localctx.n = self.native_type()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1375 
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



    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(EParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateTimeType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TimeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(EParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTimeType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.TextTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(EParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTextType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CodeTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(EParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCodeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.IntegerTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(EParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitIntegerType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DecimalTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(EParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDecimalType(self)


    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.PeriodTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(EParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPeriodType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.DateTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(EParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDateType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.CharacterTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(EParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCharacterType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_typeContext)
            super(EParser.BooleanTypeContext, self).__init__(parser)
            self.t1 = None # Token
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(EParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitBooleanType(self)



    def native_type(self):

        localctx = EParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_native_type)
        try:
            self.state = 1388
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN]:
                localctx = EParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1378
                localctx.t1 = self.match(EParser.BOOLEAN)

            elif token in [EParser.CHARACTER]:
                localctx = EParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1379
                localctx.t1 = self.match(EParser.CHARACTER)

            elif token in [EParser.TEXT]:
                localctx = EParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1380
                localctx.t1 = self.match(EParser.TEXT)

            elif token in [EParser.INTEGER]:
                localctx = EParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1381
                localctx.t1 = self.match(EParser.INTEGER)

            elif token in [EParser.DECIMAL]:
                localctx = EParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1382
                localctx.t1 = self.match(EParser.DECIMAL)

            elif token in [EParser.DATE]:
                localctx = EParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1383
                localctx.t1 = self.match(EParser.DATE)

            elif token in [EParser.DATETIME]:
                localctx = EParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1384
                localctx.t1 = self.match(EParser.DATETIME)

            elif token in [EParser.TIME]:
                localctx = EParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1385
                localctx.t1 = self.match(EParser.TIME)

            elif token in [EParser.PERIOD]:
                localctx = EParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1386
                localctx.t1 = self.match(EParser.PERIOD)

            elif token in [EParser.CODE]:
                localctx = EParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1387
                localctx.t1 = self.match(EParser.CODE)

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
        self.enterRule(localctx, 158, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1390
            localctx.t1 = self.match(EParser.TYPE_IDENTIFIER)
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
        self.enterRule(localctx, 160, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1392
            localctx.t1 = self.match(EParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Document_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def DOCUMENT(self):
            return self.getToken(EParser.DOCUMENT, 0)

        def getRuleIndex(self):
            return EParser.RULE_document_type

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDocument_type(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDocument_type(self)




    def document_type(self):

        localctx = EParser.Document_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_document_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1394
            localctx.t1 = self.match(EParser.DOCUMENT)
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
        self.enterRule(localctx, 164, self.RULE_category_declaration)
        try:
            self.state = 1399
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                localctx = EParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1396 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1397 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1398 
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


        def getRuleIndex(self):
            return EParser.RULE_type_identifier_list

     
        def copyFrom(self, ctx):
            super(EParser.Type_identifier_listContext, self).copyFrom(ctx)


    class TypeIdentifierListItemContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Type_identifier_listContext)
            super(EParser.TypeIdentifierListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(EParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifierListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifierListItem(self)


    class TypeIdentifierListContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Type_identifier_listContext)
            super(EParser.TypeIdentifierListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifierList(self)



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 166
        self.enterRecursionRule(localctx, 166, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1402 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.TypeIdentifierListItemContext(self, EParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1404
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1405
                    self.match(EParser.COMMA)
                    self.state = 1406 
                    localctx.item = self.type_identifier() 
                self.state = 1411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_identifier

     
        def copyFrom(self, ctx):
            super(EParser.Method_identifierContext, self).copyFrom(ctx)



    class MethodVariableIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_identifierContext)
            super(EParser.MethodVariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodVariableIdentifier(self)


    class MethodTypeIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_identifierContext)
            super(EParser.MethodTypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterMethodTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitMethodTypeIdentifier(self)



    def method_identifier(self):

        localctx = EParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_method_identifier)
        try:
            self.state = 1414
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1412 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1413 
                localctx.name = self.type_identifier()

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



    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.SymbolIdentifierContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
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
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableIdentifier(self)


    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a EParser.IdentifierContext)
            super(EParser.TypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(EParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypeIdentifier(self)



    def identifier(self):

        localctx = EParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_identifier)
        try:
            self.state = 1419
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1416 
                localctx.name = self.variable_identifier()

            elif token in [EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1417 
                localctx.name = self.type_identifier()

            elif token in [EParser.SYMBOL_IDENTIFIER]:
                localctx = EParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1418 
                localctx.name = self.symbol_identifier()

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
        self.enterRule(localctx, 172, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1421
            self.match(EParser.VARIABLE_IDENTIFIER)
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
        self.enterRule(localctx, 174, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1423
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
        self.enterRule(localctx, 176, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1425
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


        def getRuleIndex(self):
            return EParser.RULE_argument_list

     
        def copyFrom(self, ctx):
            super(EParser.Argument_listContext, self).copyFrom(ctx)


    class ArgumentListItemContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_listContext)
            super(EParser.ArgumentListItemContext, self).__init__(parser)
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def argument_list(self):
            return self.getTypedRuleContext(EParser.Argument_listContext,0)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentListItem(self)


    class ArgumentListContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Argument_listContext)
            super(EParser.ArgumentListContext, self).__init__(parser)
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(EParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitArgumentList(self)



    def argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 178
        self.enterRecursionRule(localctx, 178, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1428 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ArgumentListItemContext(self, EParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1430
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1431
                    self.match(EParser.COMMA)
                    self.state = 1432 
                    localctx.item = self.argument() 
                self.state = 1437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 180, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1443
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                localctx = EParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1438 
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = EParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1440
                _la = self._input.LA(1)
                if _la==EParser.MUTABLE:
                    self.state = 1439
                    self.match(EParser.MUTABLE)


                self.state = 1442 
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


        def getRuleIndex(self):
            return EParser.RULE_operator_argument

     
        def copyFrom(self, ctx):
            super(EParser.Operator_argumentContext, self).copyFrom(ctx)



    class NamedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a EParser.Operator_argumentContext)
            super(EParser.NamedArgumentContext, self).__init__(parser)
            self.arg = None # Named_argumentContext
            self.copyFrom(ctx)

        def named_argument(self):
            return self.getTypedRuleContext(EParser.Named_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNamedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNamedArgument(self)


    class TypedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a EParser.Operator_argumentContext)
            super(EParser.TypedArgumentContext, self).__init__(parser)
            self.arg = None # Typed_argumentContext
            self.copyFrom(ctx)

        def typed_argument(self):
            return self.getTypedRuleContext(EParser.Typed_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTypedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTypedArgument(self)



    def operator_argument(self):

        localctx = EParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_operator_argument)
        try:
            self.state = 1447
            token = self._input.LA(1)
            if token in [EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1445 
                localctx.arg = self.named_argument()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.ANY, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1446 
                localctx.arg = self.typed_argument()

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
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

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
        self.enterRule(localctx, 184, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1449 
            localctx.name = self.variable_identifier()
            self.state = 1452
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.state = 1450
                self.match(EParser.EQ)
                self.state = 1451 
                localctx.value = self.literal_expression()


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
        self.enterRule(localctx, 186, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1454 
            self.code_type()
            self.state = 1455 
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


        def getRuleIndex(self):
            return EParser.RULE_category_or_any_type

     
        def copyFrom(self, ctx):
            super(EParser.Category_or_any_typeContext, self).copyFrom(ctx)



    class AnyArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_or_any_typeContext)
            super(EParser.AnyArgumentTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyArgumentType(self)


    class CategoryArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Category_or_any_typeContext)
            super(EParser.CategoryArgumentTypeContext, self).__init__(parser)
            self.typ = None # TypedefContext
            self.copyFrom(ctx)

        def typedef(self):
            return self.getTypedRuleContext(EParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryArgumentType(self)



    def category_or_any_type(self):

        localctx = EParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_category_or_any_type)
        try:
            self.state = 1459
            token = self._input.LA(1)
            if token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.CODE, EParser.TYPE_IDENTIFIER]:
                localctx = EParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1457 
                localctx.typ = self.typedef(0)

            elif token in [EParser.ANY]:
                localctx = EParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1458 
                localctx.typ = self.any_type(0)

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


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyListTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAnyListType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a EParser.Any_typeContext)
            super(EParser.AnyDictTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)
        def any_type(self):
            return self.getTypedRuleContext(EParser.Any_typeContext,0)


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
        _startState = 190
        self.enterRecursionRule(localctx, 190, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1462
            self.match(EParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1470
                    la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
                    if la_ == 1:
                        localctx = EParser.AnyListTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1464
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1465
                        self.match(EParser.LBRAK)
                        self.state = 1466
                        self.match(EParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = EParser.AnyDictTypeContext(self, EParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1467
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1468
                        self.match(EParser.LCURL)
                        self.state = 1469
                        self.match(EParser.RCURL)
                        pass

             
                self.state = 1474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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


        def getRuleIndex(self):
            return EParser.RULE_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Member_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Member_method_declaration_listContext)
            super(EParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryMethodList(self)


    class CategoryMethodListItemContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Member_method_declaration_listContext)
            super(EParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Member_method_declaration_listContext,0)

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCategoryMethodListItem(self)



    def member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 192
        self.enterRecursionRule(localctx, 192, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1476 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1484
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,95,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CategoryMethodListItemContext(self, EParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1478
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1479 
                    self.lfp()
                    self.state = 1480 
                    localctx.item = self.member_method_declaration() 
                self.state = 1486
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,95,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 194, self.RULE_member_method_declaration)
        try:
            self.state = 1492
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1487 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1488 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1489 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1490 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1491 
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


        def getRuleIndex(self):
            return EParser.RULE_native_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_member_method_declaration_listContext, self).copyFrom(ctx)


    class NativeCategoryMethodListContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_member_method_declaration_listContext)
            super(EParser.NativeCategoryMethodListContext, self).__init__(parser)
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryMethodList(self)


    class NativeCategoryMethodListItemContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_member_method_declaration_listContext)
            super(EParser.NativeCategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Native_member_method_declaration_listContext
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declaration_listContext,0)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeCategoryMethodListItem(self)



    def native_member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 196
        self.enterRecursionRule(localctx, 196, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1495 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeCategoryMethodListItemContext(self, EParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1497
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1498 
                    self.lfp()
                    self.state = 1499 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self):
            return self.getTypedRuleContext(EParser.Member_method_declarationContext,0)


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
        self.enterRule(localctx, 198, self.RULE_native_member_method_declaration)
        try:
            self.state = 1508
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1506 
                self.member_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1507 
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



    def native_category_binding(self):

        localctx = EParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_native_category_binding)
        try:
            self.state = 1520
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1510
                self.match(EParser.JAVA)
                self.state = 1511 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1512
                self.match(EParser.CSHARP)
                self.state = 1513 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1514
                self.match(EParser.PYTHON2)
                self.state = 1515 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1516
                self.match(EParser.PYTHON3)
                self.state = 1517 
                localctx.binding = self.python_category_binding()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1518
                self.match(EParser.JAVASCRIPT)
                self.state = 1519 
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
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

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
        self.enterRule(localctx, 202, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1522 
            localctx.id_ = self.identifier()
            self.state = 1524
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.state = 1523 
                localctx.module = self.python_module()


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
        self.enterRule(localctx, 204, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1526
            self.match(EParser.FROM)
            self.state = 1527 
            self.module_token()
            self.state = 1528
            self.match(EParser.COLON)
            self.state = 1529 
            self.identifier()
            self.state = 1534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1530
                    self.match(EParser.DOT)
                    self.state = 1531 
                    self.identifier() 
                self.state = 1536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

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
        self.enterRule(localctx, 206, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1537
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1538
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

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

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
        self.enterRule(localctx, 208, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1540 
            localctx.id_ = self.identifier()
            self.state = 1542
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1541 
                localctx.module = self.javascript_module()


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
        self.enterRule(localctx, 210, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1544
            self.match(EParser.FROM)
            self.state = 1545 
            self.module_token()
            self.state = 1546
            self.match(EParser.COLON)
            self.state = 1548
            _la = self._input.LA(1)
            if _la==EParser.SLASH:
                self.state = 1547
                self.match(EParser.SLASH)


            self.state = 1550 
            self.javascript_identifier()
            self.state = 1555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,104,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1551
                    self.match(EParser.SLASH)
                    self.state = 1552 
                    self.javascript_identifier() 
                self.state = 1557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

            self.state = 1560
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 1558
                self.match(EParser.DOT)
                self.state = 1559 
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


        def getRuleIndex(self):
            return EParser.RULE_variable_identifier_list

     
        def copyFrom(self, ctx):
            super(EParser.Variable_identifier_listContext, self).copyFrom(ctx)


    class VariableListContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Variable_identifier_listContext)
            super(EParser.VariableListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableList(self)


    class VariableListItemContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Variable_identifier_listContext)
            super(EParser.VariableListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(EParser.Variable_identifier_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterVariableListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitVariableListItem(self)



    def variable_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Variable_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 212
        self.enterRecursionRule(localctx, 212, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1563 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1570
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.VariableListItemContext(self, EParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1565
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1566
                    self.match(EParser.COMMA)
                    self.state = 1567 
                    localctx.item = self.variable_identifier() 
                self.state = 1572
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_method_declaration

     
        def copyFrom(self, ctx):
            super(EParser.Method_declarationContext, self).copyFrom(ctx)



    class ConcreteMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.ConcreteMethodContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(EParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterConcreteMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitConcreteMethod(self)


    class TestMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.TestMethodContext, self).__init__(parser)
            self.decl = None # Test_method_declarationContext
            self.copyFrom(ctx)

        def test_method_declaration(self):
            return self.getTypedRuleContext(EParser.Test_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTestMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTestMethod(self)


    class AbstractMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.AbstractMethodContext, self).__init__(parser)
            self.decl = None # Abstract_method_declarationContext
            self.copyFrom(ctx)

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(EParser.Abstract_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAbstractMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAbstractMethod(self)


    class NativeMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a EParser.Method_declarationContext)
            super(EParser.NativeMethodContext, self).__init__(parser)
            self.decl = None # Native_method_declarationContext
            self.copyFrom(ctx)

        def native_method_declaration(self):
            return self.getTypedRuleContext(EParser.Native_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeMethod(self)



    def method_declaration(self):

        localctx = EParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_method_declaration)
        try:
            self.state = 1577
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                localctx = EParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1573 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = EParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1574 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = EParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1575 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = EParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1576 
                localctx.decl = self.test_method_declaration()
                pass


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


        def getRuleIndex(self):
            return EParser.RULE_native_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Native_statement_listContext, self).copyFrom(ctx)


    class NativeStatementListContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statement_listContext)
            super(EParser.NativeStatementListContext, self).__init__(parser)
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def native_statement(self):
            return self.getTypedRuleContext(EParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeStatementList(self)


    class NativeStatementListItemContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statement_listContext)
            super(EParser.NativeStatementListItemContext, self).__init__(parser)
            self.items = None # Native_statement_listContext
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def native_statement_list(self):
            return self.getTypedRuleContext(EParser.Native_statement_listContext,0)

        def native_statement(self):
            return self.getTypedRuleContext(EParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterNativeStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitNativeStatementListItem(self)



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 216
        self.enterRecursionRule(localctx, 216, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1580 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1588
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,108,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.NativeStatementListItemContext(self, EParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1582
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1583 
                    self.lfp()
                    self.state = 1584 
                    localctx.item = self.native_statement() 
                self.state = 1590
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(EParser.Native_statementContext, self).copyFrom(ctx)



    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python2NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
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


    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.CSharpNativeStatementContext, self).__init__(parser)
            self.stmt = None # Csharp_statementContext
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
            self.stmt = None # Java_statementContext
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
            self.stmt = None # Javascript_native_statementContext
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


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a EParser.Native_statementContext)
            super(EParser.Python3NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
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
        self.enterRule(localctx, 218, self.RULE_native_statement)
        try:
            self.state = 1601
            token = self._input.LA(1)
            if token in [EParser.JAVA]:
                localctx = EParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1591
                self.match(EParser.JAVA)
                self.state = 1592 
                localctx.stmt = self.java_statement()

            elif token in [EParser.CSHARP]:
                localctx = EParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1593
                self.match(EParser.CSHARP)
                self.state = 1594 
                localctx.stmt = self.csharp_statement()

            elif token in [EParser.PYTHON2]:
                localctx = EParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1595
                self.match(EParser.PYTHON2)
                self.state = 1596 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.PYTHON3]:
                localctx = EParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1597
                self.match(EParser.PYTHON3)
                self.state = 1598 
                localctx.stmt = self.python_native_statement()

            elif token in [EParser.JAVASCRIPT]:
                localctx = EParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1599
                self.match(EParser.JAVASCRIPT)
                self.state = 1600 
                localctx.stmt = self.javascript_native_statement()

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
            self.stmt = None # Python_statementContext
            self.module = None # Python_moduleContext

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
        self.enterRule(localctx, 220, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1603 
            localctx.stmt = self.python_statement()
            self.state = 1605
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 1604
                self.match(EParser.SEMI)


            self.state = 1608
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.state = 1607 
                localctx.module = self.python_module()


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
            self.stmt = None # Javascript_statementContext
            self.module = None # Javascript_moduleContext

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
        self.enterRule(localctx, 222, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1610 
            localctx.stmt = self.javascript_statement()
            self.state = 1612
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.state = 1611
                self.match(EParser.SEMI)


            self.state = 1615
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 1614 
                localctx.module = self.javascript_module()


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


        def getRuleIndex(self):
            return EParser.RULE_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Statement_listContext, self).copyFrom(ctx)


    class StatementListItemContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Statement_listContext)
            super(EParser.StatementListItemContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(EParser.Statement_listContext,0)

        def statement(self):
            return self.getTypedRuleContext(EParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStatementListItem(self)


    class StatementListContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Statement_listContext)
            super(EParser.StatementListContext, self).__init__(parser)
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(EParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitStatementList(self)



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1618 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1626
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.StatementListItemContext(self, EParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1620
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1621 
                    self.lfp()
                    self.state = 1622 
                    localctx.item = self.statement() 
                self.state = 1628
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_assertion_list

     
        def copyFrom(self, ctx):
            super(EParser.Assertion_listContext, self).copyFrom(ctx)


    class AssertionListItemContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Assertion_listContext)
            super(EParser.AssertionListItemContext, self).__init__(parser)
            self.items = None # Assertion_listContext
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def assertion_list(self):
            return self.getTypedRuleContext(EParser.Assertion_listContext,0)

        def assertion(self):
            return self.getTypedRuleContext(EParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertionListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertionListItem(self)


    class AssertionListContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Assertion_listContext)
            super(EParser.AssertionListContext, self).__init__(parser)
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def assertion(self):
            return self.getTypedRuleContext(EParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAssertionList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAssertionList(self)



    def assertion_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assertion_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 226
        self.enterRecursionRule(localctx, 226, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1630 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1638
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.AssertionListItemContext(self, EParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1632
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1633 
                    self.lfp()
                    self.state = 1634 
                    localctx.item = self.assertion() 
                self.state = 1640
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,115,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_switch_case_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Switch_case_statement_listContext, self).copyFrom(ctx)


    class SwitchCaseStatementListItemContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statement_listContext)
            super(EParser.SwitchCaseStatementListItemContext, self).__init__(parser)
            self.items = None # Switch_case_statement_listContext
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def switch_case_statement_list(self):
            return self.getTypedRuleContext(EParser.Switch_case_statement_listContext,0)

        def switch_case_statement(self):
            return self.getTypedRuleContext(EParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchCaseStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchCaseStatementListItem(self)


    class SwitchCaseStatementListContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Switch_case_statement_listContext)
            super(EParser.SwitchCaseStatementListContext, self).__init__(parser)
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def switch_case_statement(self):
            return self.getTypedRuleContext(EParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSwitchCaseStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSwitchCaseStatementList(self)



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1642 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1650
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,116,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.SwitchCaseStatementListItemContext(self, EParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1644
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1645 
                    self.lfp()
                    self.state = 1646 
                    localctx.item = self.switch_case_statement() 
                self.state = 1652
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,116,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_catch_statement_list

     
        def copyFrom(self, ctx):
            super(EParser.Catch_statement_listContext, self).copyFrom(ctx)


    class CatchStatementListContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statement_listContext)
            super(EParser.CatchStatementListContext, self).__init__(parser)
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def catch_statement(self):
            return self.getTypedRuleContext(EParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchStatementList(self)


    class CatchStatementListItemContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Catch_statement_listContext)
            super(EParser.CatchStatementListItemContext, self).__init__(parser)
            self.items = None # Catch_statement_listContext
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(EParser.LfpContext,0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(EParser.Catch_statement_listContext,0)

        def catch_statement(self):
            return self.getTypedRuleContext(EParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCatchStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCatchStatementListItem(self)



    def catch_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Catch_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 230
        self.enterRecursionRule(localctx, 230, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1654 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1662
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CatchStatementListItemContext(self, EParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1656
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1657 
                    self.lfp()
                    self.state = 1658 
                    localctx.item = self.catch_statement() 
                self.state = 1664
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(EParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralSetLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(EParser.LT, 0)
        def GT(self):
            return self.getToken(EParser.GT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralSetLiteral(self)


    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_collectionContext)
            super(EParser.LiteralListLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(EParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(EParser.RBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)


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



    def literal_collection(self):

        localctx = EParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_literal_collection)
        try:
            self.state = 1679
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                localctx = EParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1665
                self.match(EParser.LBRAK)
                self.state = 1666 
                localctx.low = self.atomic_literal()
                self.state = 1667
                self.match(EParser.RANGE)
                self.state = 1668 
                localctx.high = self.atomic_literal()
                self.state = 1669
                self.match(EParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = EParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1671
                self.match(EParser.LBRAK)
                self.state = 1672 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1673
                self.match(EParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = EParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1675
                self.match(EParser.LT)
                self.state = 1676 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1677
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



    def atomic_literal(self):

        localctx = EParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_atomic_literal)
        try:
            self.state = 1694
            token = self._input.LA(1)
            if token in [EParser.MIN_INTEGER]:
                localctx = EParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1681
                localctx.t = self.match(EParser.MIN_INTEGER)

            elif token in [EParser.MAX_INTEGER]:
                localctx = EParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1682
                localctx.t = self.match(EParser.MAX_INTEGER)

            elif token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1683
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.HEXA_LITERAL]:
                localctx = EParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1684
                localctx.t = self.match(EParser.HEXA_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1685
                localctx.t = self.match(EParser.CHAR_LITERAL)

            elif token in [EParser.DATE_LITERAL]:
                localctx = EParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1686
                localctx.t = self.match(EParser.DATE_LITERAL)

            elif token in [EParser.TIME_LITERAL]:
                localctx = EParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1687
                localctx.t = self.match(EParser.TIME_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1688
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1689
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.DATETIME_LITERAL]:
                localctx = EParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1690
                localctx.t = self.match(EParser.DATETIME_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1691
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.PERIOD_LITERAL]:
                localctx = EParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1692
                localctx.t = self.match(EParser.PERIOD_LITERAL)

            elif token in [EParser.NOTHING]:
                localctx = EParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1693 
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


        def getRuleIndex(self):
            return EParser.RULE_literal_list_literal

     
        def copyFrom(self, ctx):
            super(EParser.Literal_list_literalContext, self).copyFrom(ctx)


    class LiteralListContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_list_literalContext)
            super(EParser.LiteralListContext, self).__init__(parser)
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralList(self)


    class LiteralListItemContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_list_literalContext)
            super(EParser.LiteralListItemContext, self).__init__(parser)
            self.items = None # Literal_list_literalContext
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(EParser.Literal_list_literalContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterLiteralListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitLiteralListItem(self)



    def literal_list_literal(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Literal_list_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 236
        self.enterRecursionRule(localctx, 236, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1697 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1704
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,120,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.LiteralListItemContext(self, EParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1699
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1700
                    self.match(EParser.COMMA)
                    self.state = 1701 
                    localctx.item = self.atomic_literal() 
                self.state = 1706
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,120,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(EParser.Selectable_expressionContext, self).copyFrom(ctx)



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



    def selectable_expression(self):

        localctx = EParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_selectable_expression)
        try:
            self.state = 1711
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                localctx = EParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1707 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1708 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = EParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1709 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = EParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1710 
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
        self.enterRule(localctx, 240, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1713
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
            self.exp = None # ExpressionContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


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
        self.enterRule(localctx, 242, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1715
            self.match(EParser.LPAR)
            self.state = 1716 
            localctx.exp = self.expression(0)
            self.state = 1717
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


        def getRuleIndex(self):
            return EParser.RULE_literal_expression

     
        def copyFrom(self, ctx):
            super(EParser.Literal_expressionContext, self).copyFrom(ctx)



    class CollectionLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_expressionContext)
            super(EParser.CollectionLiteralContext, self).__init__(parser)
            self.exp = None # Collection_literalContext
            self.copyFrom(ctx)

        def collection_literal(self):
            return self.getTypedRuleContext(EParser.Collection_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCollectionLiteral(self)


    class AtomicLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Literal_expressionContext)
            super(EParser.AtomicLiteralContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(EParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterAtomicLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitAtomicLiteral(self)



    def literal_expression(self):

        localctx = EParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_literal_expression)
        try:
            self.state = 1721
            token = self._input.LA(1)
            if token in [EParser.NOTHING, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.MIN_INTEGER, EParser.MAX_INTEGER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.HEXA_LITERAL, EParser.DECIMAL_LITERAL, EParser.DATETIME_LITERAL, EParser.TIME_LITERAL, EParser.DATE_LITERAL, EParser.PERIOD_LITERAL]:
                localctx = EParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1719 
                localctx.exp = self.atomic_literal()

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.LCURL, EParser.LT]:
                localctx = EParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1720 
                localctx.exp = self.collection_literal()

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


        def getRuleIndex(self):
            return EParser.RULE_collection_literal

     
        def copyFrom(self, ctx):
            super(EParser.Collection_literalContext, self).copyFrom(ctx)



    class TupleLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.TupleLiteralContext, self).__init__(parser)
            self.exp = None # Tuple_literalContext
            self.copyFrom(ctx)

        def tuple_literal(self):
            return self.getTypedRuleContext(EParser.Tuple_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterTupleLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitTupleLiteral(self)


    class ListLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.ListLiteralContext, self).__init__(parser)
            self.exp = None # List_literalContext
            self.copyFrom(ctx)

        def list_literal(self):
            return self.getTypedRuleContext(EParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitListLiteral(self)


    class DictLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.DictLiteralContext, self).__init__(parser)
            self.exp = None # Dict_literalContext
            self.copyFrom(ctx)

        def dict_literal(self):
            return self.getTypedRuleContext(EParser.Dict_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictLiteral(self)


    class RangeLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.RangeLiteralContext, self).__init__(parser)
            self.exp = None # Range_literalContext
            self.copyFrom(ctx)

        def range_literal(self):
            return self.getTypedRuleContext(EParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRangeLiteral(self)


    class SetLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a EParser.Collection_literalContext)
            super(EParser.SetLiteralContext, self).__init__(parser)
            self.exp = None # Set_literalContext
            self.copyFrom(ctx)

        def set_literal(self):
            return self.getTypedRuleContext(EParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitSetLiteral(self)



    def collection_literal(self):

        localctx = EParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_collection_literal)
        try:
            self.state = 1728
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                localctx = EParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1723 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = EParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1724 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = EParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1725 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = EParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1726 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = EParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1727 
                localctx.exp = self.tuple_literal()
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
            self.items = None # Expression_tupleContext

        def LPAR(self):
            return self.getToken(EParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(EParser.RPAR, 0)

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
        self.enterRule(localctx, 248, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1730
            self.match(EParser.LPAR)
            self.state = 1732
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1731 
                localctx.items = self.expression_tuple(0)


            self.state = 1734
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
            self.items = None # Dict_entry_listContext

        def LCURL(self):
            return self.getToken(EParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(EParser.RCURL, 0)

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
        self.enterRule(localctx, 250, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1736
            self.match(EParser.LCURL)
            self.state = 1738
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.LCURL) | (1 << EParser.MINUS) | (1 << EParser.LT) | (1 << EParser.METHOD_T) | (1 << EParser.CODE) | (1 << EParser.DOCUMENT))) != 0) or ((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & ((1 << (EParser.EXECUTE - 87)) | (1 << (EParser.FETCH - 87)) | (1 << (EParser.INVOKE - 87)) | (1 << (EParser.MUTABLE - 87)) | (1 << (EParser.NOT - 87)) | (1 << (EParser.NOTHING - 87)) | (1 << (EParser.READ - 87)) | (1 << (EParser.SELF - 87)) | (1 << (EParser.SORTED - 87)) | (1 << (EParser.THIS - 87)) | (1 << (EParser.BOOLEAN_LITERAL - 87)) | (1 << (EParser.CHAR_LITERAL - 87)) | (1 << (EParser.MIN_INTEGER - 87)) | (1 << (EParser.MAX_INTEGER - 87)) | (1 << (EParser.SYMBOL_IDENTIFIER - 87)) | (1 << (EParser.TYPE_IDENTIFIER - 87)) | (1 << (EParser.VARIABLE_IDENTIFIER - 87)) | (1 << (EParser.TEXT_LITERAL - 87)) | (1 << (EParser.INTEGER_LITERAL - 87)) | (1 << (EParser.HEXA_LITERAL - 87)) | (1 << (EParser.DECIMAL_LITERAL - 87)) | (1 << (EParser.DATETIME_LITERAL - 87)) | (1 << (EParser.TIME_LITERAL - 87)))) != 0) or _la==EParser.DATE_LITERAL or _la==EParser.PERIOD_LITERAL:
                self.state = 1737 
                localctx.items = self.dict_entry_list(0)


            self.state = 1740
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


        def getRuleIndex(self):
            return EParser.RULE_expression_tuple

     
        def copyFrom(self, ctx):
            super(EParser.Expression_tupleContext, self).copyFrom(ctx)


    class ValueTupleItemContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_tupleContext)
            super(EParser.ValueTupleItemContext, self).__init__(parser)
            self.items = None # Expression_tupleContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def expression_tuple(self):
            return self.getTypedRuleContext(EParser.Expression_tupleContext,0)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueTupleItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueTupleItem(self)


    class ValueTupleContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a EParser.Expression_tupleContext)
            super(EParser.ValueTupleContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(EParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterValueTuple(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitValueTuple(self)



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 252
        self.enterRecursionRule(localctx, 252, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1743 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1750
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ValueTupleItemContext(self, EParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1745
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1746
                    self.match(EParser.COMMA)
                    self.state = 1747 
                    localctx.item = self.expression(0) 
                self.state = 1752
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EParser.RULE_dict_entry_list

     
        def copyFrom(self, ctx):
            super(EParser.Dict_entry_listContext, self).copyFrom(ctx)


    class DictEntryListContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Dict_entry_listContext)
            super(EParser.DictEntryListContext, self).__init__(parser)
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def dict_entry(self):
            return self.getTypedRuleContext(EParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictEntryList(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictEntryList(self)


    class DictEntryListItemContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a EParser.Dict_entry_listContext)
            super(EParser.DictEntryListItemContext, self).__init__(parser)
            self.items = None # Dict_entry_listContext
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(EParser.COMMA, 0)
        def dict_entry_list(self):
            return self.getTypedRuleContext(EParser.Dict_entry_listContext,0)

        def dict_entry(self):
            return self.getTypedRuleContext(EParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterDictEntryListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitDictEntryListItem(self)



    def dict_entry_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Dict_entry_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 254
        self.enterRecursionRule(localctx, 254, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1754 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1761
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.DictEntryListItemContext(self, EParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1756
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1757
                    self.match(EParser.COMMA)
                    self.state = 1758 
                    localctx.item = self.dict_entry() 
                self.state = 1763
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 256, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1764 
            localctx.key = self.expression(0)
            self.state = 1765
            self.match(EParser.COLON)
            self.state = 1766 
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



    def slice_arguments(self):

        localctx = EParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_slice_arguments)
        try:
            self.state = 1777
            la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
            if la_ == 1:
                localctx = EParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1768 
                localctx.first = self.expression(0)
                self.state = 1769
                self.match(EParser.COLON)
                self.state = 1770 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = EParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1772 
                localctx.first = self.expression(0)
                self.state = 1773
                self.match(EParser.COLON)
                pass

            elif la_ == 3:
                localctx = EParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1775
                self.match(EParser.COLON)
                self.state = 1776 
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
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(EParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


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
        self.enterRule(localctx, 260, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1779 
            localctx.name = self.variable_identifier()
            self.state = 1780 
            self.assign()
            self.state = 1781 
            localctx.exp = self.expression(0)
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


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.RootInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(EParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitRootInstance(self)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a EParser.Assignable_instanceContext)
            super(EParser.ChildInstanceContext, self).__init__(parser)
            self.parent = None # Assignable_instanceContext
            self.child = None # Child_instanceContext
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



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 262
        self.enterRecursionRule(localctx, 262, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1784 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1790
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.ChildInstanceContext(self, EParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1786
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1787 
                    localctx.child = self.child_instance() 
                self.state = 1792
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

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
            self.typ = None # Category_or_any_typeContext
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
            self.exp = None # ExpressionContext
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
        self.enterRule(localctx, 264, self.RULE_is_expression)
        try:
            self.state = 1797
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                localctx = EParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1793
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1794
                self.match(EParser.VARIABLE_IDENTIFIER)
                self.state = 1795 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = EParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1796 
                localctx.exp = self.expression(0)
                pass


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



    def operator(self):

        localctx = EParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_operator)
        try:
            self.state = 1805
            token = self._input.LA(1)
            if token in [EParser.PLUS]:
                localctx = EParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1799
                self.match(EParser.PLUS)

            elif token in [EParser.MINUS]:
                localctx = EParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1800
                self.match(EParser.MINUS)

            elif token in [EParser.STAR]:
                localctx = EParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1801 
                self.multiply()

            elif token in [EParser.SLASH]:
                localctx = EParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1802 
                self.divide()

            elif token in [EParser.BSLASH]:
                localctx = EParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1803 
                self.idivide()

            elif token in [EParser.PERCENT, EParser.MODULO]:
                localctx = EParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1804 
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
        self.enterRule(localctx, 268, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1807
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1808
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
        self.enterRule(localctx, 270, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1810
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1811
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
        self.enterRule(localctx, 272, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1813
            localctx.i1 = self.match(EParser.VARIABLE_IDENTIFIER)
            self.state = 1814
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
        self.enterRule(localctx, 274, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1816
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
        self.enterRule(localctx, 276, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1818
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
        self.enterRule(localctx, 278, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1820
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
        self.enterRule(localctx, 280, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1822
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
        self.enterRule(localctx, 282, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1824
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



    def javascript_statement(self):

        localctx = EParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_javascript_statement)
        try:
            self.state = 1833
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1826
                self.match(EParser.RETURN)
                self.state = 1827 
                localctx.exp = self.javascript_expression(0)
                self.state = 1828
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.LBRAK, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1830 
                localctx.exp = self.javascript_expression(0)
                self.state = 1831
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



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 286
        self.enterRecursionRule(localctx, 286, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1836 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1842
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptSelectorExpressionContext(self, EParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1838
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1839 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1844
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

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
        self.enterRule(localctx, 288, self.RULE_javascript_primary_expression)
        try:
            self.state = 1851
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1845 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1846 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1847 
                self.javascript_identifier_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1848 
                self.javascript_literal_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1849 
                self.javascript_method_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1850 
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
        self.enterRule(localctx, 290, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1853 
            self.this_expression()
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



    def javascript_selector_expression(self):

        localctx = EParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_javascript_selector_expression)
        try:
            self.state = 1860
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                localctx = EParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1855
                self.match(EParser.DOT)
                self.state = 1856 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = EParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1857
                self.match(EParser.DOT)
                self.state = 1858 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = EParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1859 
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
        self.enterRule(localctx, 294, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1862 
            localctx.name = self.javascript_identifier()
            self.state = 1863
            self.match(EParser.LPAR)
            self.state = 1865
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.LBRAK) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1864 
                localctx.args = self.javascript_arguments(0)


            self.state = 1867
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



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 296
        self.enterRecursionRule(localctx, 296, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1870 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1877
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavascriptArgumentListItemContext(self, EParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1872
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1873
                    self.match(EParser.COMMA)
                    self.state = 1874 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1879
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

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
        self.enterRule(localctx, 298, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880
            self.match(EParser.LBRAK)
            self.state = 1881 
            localctx.exp = self.javascript_expression(0)
            self.state = 1882
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
        self.enterRule(localctx, 300, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            self.match(EParser.LPAR)
            self.state = 1885 
            localctx.exp = self.javascript_expression(0)
            self.state = 1886
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
        self.enterRule(localctx, 302, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888 
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



    def javascript_literal_expression(self):

        localctx = EParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_javascript_literal_expression)
        try:
            self.state = 1895
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1890
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1891
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1892
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1893
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1894
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
        self.enterRule(localctx, 306, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1897
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)))) != 0)):
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



    def python_statement(self):

        localctx = EParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_python_statement)
        try:
            self.state = 1902
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1899
                self.match(EParser.RETURN)
                self.state = 1900 
                localctx.exp = self.python_expression(0)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1901 
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



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1905 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1911
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonSelectorExpressionContext(self, EParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1907
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1908 
                    localctx.child = self.python_selector_expression() 
                self.state = 1913
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

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



    def python_primary_expression(self):

        localctx = EParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_python_primary_expression)
        try:
            self.state = 1918
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1914 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = EParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1915 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1916 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = EParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1917 
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



    def python_selector_expression(self):

        localctx = EParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_python_selector_expression)
        try:
            self.state = 1926
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1920
                self.match(EParser.DOT)
                self.state = 1921 
                localctx.exp = self.python_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1922
                self.match(EParser.LBRAK)
                self.state = 1923 
                localctx.exp = self.python_expression(0)
                self.state = 1924
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
        self.enterRule(localctx, 316, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1928 
            localctx.name = self.python_identifier()
            self.state = 1929
            self.match(EParser.LPAR)
            self.state = 1931
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 1930 
                localctx.args = self.python_argument_list()


            self.state = 1933
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



    def python_argument_list(self):

        localctx = EParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_python_argument_list)
        try:
            self.state = 1941
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                localctx = EParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1935 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = EParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1936 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = EParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1937 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1938
                self.match(EParser.COMMA)
                self.state = 1939 
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



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1944 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1951
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonOrdinalArgumentListItemContext(self, EParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1946
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1947
                    self.match(EParser.COMMA)
                    self.state = 1948 
                    localctx.item = self.python_expression(0) 
                self.state = 1953
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

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



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1955 
            localctx.name = self.python_identifier()
            self.state = 1956
            self.match(EParser.EQ)
            self.state = 1957 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1967
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonNamedArgumentListItemContext(self, EParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1959
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1960
                    self.match(EParser.COMMA)
                    self.state = 1961 
                    localctx.name = self.python_identifier()
                    self.state = 1962
                    self.match(EParser.EQ)
                    self.state = 1963 
                    localctx.exp = self.python_expression(0) 
                self.state = 1969
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

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
        self.enterRule(localctx, 324, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1970
            self.match(EParser.LPAR)
            self.state = 1971 
            localctx.exp = self.python_expression(0)
            self.state = 1972
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


    class PythonPrestoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Python_identifier_expressionContext)
            super(EParser.PythonPrestoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterPythonPrestoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitPythonPrestoIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1977
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.PythonPrestoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1975
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1976 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1984
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,148,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.PythonChildIdentifierContext(self, EParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1979
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1980
                    self.match(EParser.DOT)
                    self.state = 1981 
                    localctx.name = self.python_identifier() 
                self.state = 1986
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,148,self._ctx)

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



    def python_literal_expression(self):

        localctx = EParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_python_literal_expression)
        try:
            self.state = 1992
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1987
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1988
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1989
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1990
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1991
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
        self.enterRule(localctx, 330, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1994
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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



    def java_statement(self):

        localctx = EParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_java_statement)
        try:
            self.state = 2003
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1996
                self.match(EParser.RETURN)
                self.state = 1997 
                localctx.exp = self.java_expression(0)
                self.state = 1998
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2000 
                localctx.exp = self.java_expression(0)
                self.state = 2001
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



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2006 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2012
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaSelectorExpressionContext(self, EParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2008
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2009 
                    localctx.child = self.java_selector_expression() 
                self.state = 2014
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

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
        self.enterRule(localctx, 336, self.RULE_java_primary_expression)
        try:
            self.state = 2019
            token = self._input.LA(1)
            if token in [EParser.SELF, EParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2015 
                self.java_this_expression()

            elif token in [EParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2016 
                self.java_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.NATIVE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2017 
                self.java_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2018 
                self.java_literal_expression()

            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 338, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2021 
            self.this_expression()
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
        self.enterRule(localctx, 340, self.RULE_java_selector_expression)
        try:
            self.state = 2026
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2023
                self.match(EParser.DOT)
                self.state = 2024 
                localctx.exp = self.java_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2025 
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
        self.enterRule(localctx, 342, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2028 
            localctx.name = self.java_identifier()
            self.state = 2029
            self.match(EParser.LPAR)
            self.state = 2031
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.NATIVE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 2030 
                localctx.args = self.java_arguments(0)


            self.state = 2033
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



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2036 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2043
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,155,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaArgumentListItemContext(self, EParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2038
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2039
                    self.match(EParser.COMMA)
                    self.state = 2040 
                    localctx.item = self.java_expression(0) 
                self.state = 2045
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

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
        self.enterRule(localctx, 346, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2046
            self.match(EParser.LBRAK)
            self.state = 2047 
            localctx.exp = self.java_expression(0)
            self.state = 2048
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
        self.enterRule(localctx, 348, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2050
            self.match(EParser.LPAR)
            self.state = 2051 
            localctx.exp = self.java_expression(0)
            self.state = 2052
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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2055 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2062
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildIdentifierContext(self, EParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2057
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2058
                    self.match(EParser.DOT)
                    self.state = 2059 
                    localctx.name = self.java_identifier() 
                self.state = 2064
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

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



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2066 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2072
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.JavaChildClassIdentifierContext(self, EParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2068
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2069
                    localctx.name = self.match(EParser.DOLLAR_IDENTIFIER) 
                self.state = 2074
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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



    def java_literal_expression(self):

        localctx = EParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_java_literal_expression)
        try:
            self.state = 2080
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2075
                localctx.t = self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2076
                localctx.t = self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2077
                localctx.t = self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2078
                localctx.t = self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2079
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
        self.enterRule(localctx, 356, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2082
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.NATIVE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)))) != 0)):
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



    def csharp_statement(self):

        localctx = EParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_csharp_statement)
        try:
            self.state = 2091
            token = self._input.LA(1)
            if token in [EParser.RETURN]:
                localctx = EParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2084
                self.match(EParser.RETURN)
                self.state = 2085 
                localctx.exp = self.csharp_expression(0)
                self.state = 2086
                self.match(EParser.SEMI)

            elif token in [EParser.LPAR, EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.SELF, EParser.TEST, EParser.THIS, EParser.WRITE, EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2088 
                localctx.exp = self.csharp_expression(0)
                self.state = 2089
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



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2094 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpSelectorExpressionContext(self, EParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2096
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2097 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

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
        self.enterRule(localctx, 362, self.RULE_csharp_primary_expression)
        try:
            self.state = 2107
            token = self._input.LA(1)
            if token in [EParser.SELF, EParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2103 
                self.csharp_this_expression()

            elif token in [EParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2104 
                self.csharp_parenthesis_expression()

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER, EParser.DOLLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2105 
                self.csharp_identifier_expression(0)

            elif token in [EParser.BOOLEAN_LITERAL, EParser.CHAR_LITERAL, EParser.TEXT_LITERAL, EParser.INTEGER_LITERAL, EParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2106 
                self.csharp_literal_expression()

            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 364, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2109 
            self.this_expression()
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



    def csharp_selector_expression(self):

        localctx = EParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_csharp_selector_expression)
        try:
            self.state = 2114
            token = self._input.LA(1)
            if token in [EParser.DOT]:
                localctx = EParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2111
                self.match(EParser.DOT)
                self.state = 2112 
                localctx.exp = self.csharp_method_expression()

            elif token in [EParser.LBRAK]:
                localctx = EParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2113 
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
        self.enterRule(localctx, 368, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2116 
            localctx.name = self.csharp_identifier()
            self.state = 2117
            self.match(EParser.LPAR)
            self.state = 2119
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.LPAR) | (1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.SELF - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.THIS - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.BOOLEAN_LITERAL - 116)) | (1 << (EParser.CHAR_LITERAL - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)) | (1 << (EParser.DOLLAR_IDENTIFIER - 116)) | (1 << (EParser.TEXT_LITERAL - 116)) | (1 << (EParser.INTEGER_LITERAL - 116)) | (1 << (EParser.DECIMAL_LITERAL - 116)))) != 0):
                self.state = 2118 
                localctx.args = self.csharp_arguments(0)


            self.state = 2121
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
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = EParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2124 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,164,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpArgumentListItemContext(self, EParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2126
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2127
                    self.match(EParser.COMMA)
                    self.state = 2128 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,164,self._ctx)

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
        self.enterRule(localctx, 372, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2134
            self.match(EParser.LBRAK)
            self.state = 2135 
            localctx.exp = self.csharp_expression(0)
            self.state = 2136
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
        self.enterRule(localctx, 374, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2138
            self.match(EParser.LPAR)
            self.state = 2139 
            localctx.exp = self.csharp_expression(0)
            self.state = 2140
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


    class CSharpPrestoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a EParser.Csharp_identifier_expressionContext)
            super(EParser.CSharpPrestoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(EParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.enterCSharpPrestoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, EParserListener ):
                listener.exitCSharpPrestoIdentifier(self)


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



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2145
            token = self._input.LA(1)
            if token in [EParser.DOLLAR_IDENTIFIER]:
                localctx = EParser.CSharpPrestoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2143
                self.match(EParser.DOLLAR_IDENTIFIER)

            elif token in [EParser.BOOLEAN, EParser.CHARACTER, EParser.TEXT, EParser.INTEGER, EParser.DECIMAL, EParser.DATE, EParser.TIME, EParser.DATETIME, EParser.PERIOD, EParser.READ, EParser.TEST, EParser.WRITE, EParser.SYMBOL_IDENTIFIER, EParser.TYPE_IDENTIFIER, EParser.VARIABLE_IDENTIFIER]:
                localctx = EParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2144 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EParser.CSharpChildIdentifierContext(self, EParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2147
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2148
                    self.match(EParser.DOT)
                    self.state = 2149 
                    localctx.name = self.csharp_identifier() 
                self.state = 2154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

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
        self.enterRule(localctx, 378, self.RULE_csharp_literal_expression)
        try:
            self.state = 2160
            token = self._input.LA(1)
            if token in [EParser.INTEGER_LITERAL]:
                localctx = EParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2155
                self.match(EParser.INTEGER_LITERAL)

            elif token in [EParser.DECIMAL_LITERAL]:
                localctx = EParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2156
                self.match(EParser.DECIMAL_LITERAL)

            elif token in [EParser.TEXT_LITERAL]:
                localctx = EParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2157
                self.match(EParser.TEXT_LITERAL)

            elif token in [EParser.BOOLEAN_LITERAL]:
                localctx = EParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2158
                self.match(EParser.BOOLEAN_LITERAL)

            elif token in [EParser.CHAR_LITERAL]:
                localctx = EParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2159
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
        self.enterRule(localctx, 380, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EParser.BOOLEAN) | (1 << EParser.CHARACTER) | (1 << EParser.TEXT) | (1 << EParser.INTEGER) | (1 << EParser.DECIMAL) | (1 << EParser.DATE) | (1 << EParser.TIME) | (1 << EParser.DATETIME) | (1 << EParser.PERIOD))) != 0) or ((((_la - 116)) & ~0x3f) == 0 and ((1 << (_la - 116)) & ((1 << (EParser.READ - 116)) | (1 << (EParser.TEST - 116)) | (1 << (EParser.WRITE - 116)) | (1 << (EParser.SYMBOL_IDENTIFIER - 116)) | (1 << (EParser.TYPE_IDENTIFIER - 116)) | (1 << (EParser.VARIABLE_IDENTIFIER - 116)))) != 0)):
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
        self._predicates[14] = self.native_category_binding_list_sempred
        self._predicates[33] = self.else_if_statement_list_sempred
        self._predicates[38] = self.expression_sempred
        self._predicates[39] = self.unresolved_expression_sempred
        self._predicates[40] = self.unresolved_selector_sempred
        self._predicates[42] = self.invocation_trailer_sempred
        self._predicates[43] = self.instance_expression_sempred
        self._predicates[44] = self.instance_selector_sempred
        self._predicates[52] = self.argument_assignment_list_sempred
        self._predicates[53] = self.with_argument_assignment_list_sempred
        self._predicates[56] = self.child_instance_sempred
        self._predicates[64] = self.declarations_sempred
        self._predicates[68] = self.native_symbol_list_sempred
        self._predicates[69] = self.category_symbol_list_sempred
        self._predicates[70] = self.symbol_list_sempred
        self._predicates[74] = self.expression_list_sempred
        self._predicates[76] = self.typedef_sempred
        self._predicates[83] = self.type_identifier_list_sempred
        self._predicates[89] = self.argument_list_sempred
        self._predicates[95] = self.any_type_sempred
        self._predicates[96] = self.member_method_declaration_list_sempred
        self._predicates[98] = self.native_member_method_declaration_list_sempred
        self._predicates[103] = self.module_token_sempred
        self._predicates[106] = self.variable_identifier_list_sempred
        self._predicates[108] = self.native_statement_list_sempred
        self._predicates[112] = self.statement_list_sempred
        self._predicates[113] = self.assertion_list_sempred
        self._predicates[114] = self.switch_case_statement_list_sempred
        self._predicates[115] = self.catch_statement_list_sempred
        self._predicates[118] = self.literal_list_literal_sempred
        self._predicates[126] = self.expression_tuple_sempred
        self._predicates[127] = self.dict_entry_list_sempred
        self._predicates[131] = self.assignable_instance_sempred
        self._predicates[132] = self.is_expression_sempred
        self._predicates[134] = self.key_token_sempred
        self._predicates[135] = self.value_token_sempred
        self._predicates[136] = self.symbols_token_sempred
        self._predicates[143] = self.javascript_expression_sempred
        self._predicates[148] = self.javascript_arguments_sempred
        self._predicates[155] = self.python_expression_sempred
        self._predicates[160] = self.python_ordinal_argument_list_sempred
        self._predicates[161] = self.python_named_argument_list_sempred
        self._predicates[163] = self.python_identifier_expression_sempred
        self._predicates[167] = self.java_expression_sempred
        self._predicates[172] = self.java_arguments_sempred
        self._predicates[175] = self.java_identifier_expression_sempred
        self._predicates[176] = self.java_class_identifier_expression_sempred
        self._predicates[180] = self.csharp_expression_sempred
        self._predicates[185] = self.csharp_arguments_sempred
        self._predicates[188] = self.csharp_identifier_expression_sempred
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
                return self.precpred(self._ctx, 36)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 35)
         

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
                return self.precpred(self._ctx, 29)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 20)
         

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
                return self.precpred(self._ctx, 27)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 19)
         

    def unresolved_expression_sempred(self, localctx, predIndex):
            if predIndex == 28:
                return self.precpred(self._ctx, 1)
         

    def unresolved_selector_sempred(self, localctx, predIndex):
            if predIndex == 29:
                return self.wasNot(EParser.WS)
         

    def invocation_trailer_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.willBe(EParser.LF)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.wasNot(EParser.WS)
         

            if predIndex == 33:
                return self.wasNot(EParser.WS)
         

            if predIndex == 34:
                return self.wasNot(EParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.was(EParser.WS)
         

    def with_argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.wasNot(EParser.WS)
         

            if predIndex == 38:
                return self.wasNot(EParser.WS)
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def assertion_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.willBeAOrAn()
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 78:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 79:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 80:
                return self.precpred(self._ctx, 1)
         



