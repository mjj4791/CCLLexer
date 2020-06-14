from pygments.lexer import RegexLexer
from pygments.token import *

#/*
#    Comment
#    String
#*/
class CCLLexer(RegexLexer):
    name = 'Cerner Command Language'
    aliases = ['ccl']
    filenames = ['*.ccl', '*.inc', '*.prg']
    mimetypes = ['application/x-ccl', 'text/x-ccl']

    tokens = {
        'root': [
            # compiler directives
            (r'\s+', Text),
            (r'(?i)^%#(DEF|DEFINE|IFDEF|IFNDEF|UNDEF)\s+\S+', Comment.Preproc),
            (r'(?i)^%#(ELSE|ENDIF)', Comment.Preproc),

            # includes, etc:
            (r'^%((?i)B|BANNER|C|CLEAR|D|DISPLAY|E|EDIT|H|HELP|I|INCLUDE|J|JOURNAL|K|KEDIT|L|LEDIT|M|MODULE|O|OUTPUT|P|PRINT|R|RUN|S|SHOW|T|TERMINAL|V|VERSIONs)\s+\S+', Comment.Preproc),

             # Comments:
            (r';.*', Comment),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'/', Text),

            # punctuation (not operators):
            (r'[,.<>/\[\]{}]', Punctuation),
            (r'(->)', Punctuation),

            # Operators
            (r'[~!%^&*+=|:-]', Operator),
            (r'\b(or|not|and)\b', Operator.Word),


            # string
            (r'@"(""|[^"])*"', String),
            (r'"(\\\\|\\"|[^"\n])*["\n]', String),
            (r"'(\\\\|\\'|[^'\n])*['\n]", String),

            # numbers:
            (r"\b[0-9]+(\.[0-9]*)?([eE][+-][0-9]+)?\b"
                 r"\b[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?\b", Number),

            # keywords
            (r'(?i)\b(call|case|create|declare|define|drop|else|elseif|end|endcase|endfor|endif|endmacro|endwhile|execute|for|free|go|if|of|program|range|record|return|set|subroutine|to|translate|while|'
                 r'and|by|commit|delete|dummyt|from|group|insert|into|join|left|maxrec|merge|none|not|or|order|outerjoin|plan|prompt|rdb|rollback|select|seq|union|update|where|with|'
                 r'break|col|detail|foot|head|macro|report|row|'
                 r'ABS|AESDECRYPT|AESDECRYPTFILE|AESENCRYPT|AESENCRYPTFILE|ALTER|ALTER2|ALTERLIST|ASIS|ASSIGN|ASSIGN2|ASSIGN3|AVG|BAND|BLOBGET|BLOBGETLEN|BNOT|BOR|BTEST|BUILD|BUILD2|BUILD2CHK|BXOR|CALCPOS|CALLPRG|CCLFMT|CCLIO|CEIL|CHAR|CHECK|CHECKDIC|CHECKFUN|CHECKPRG|CHECKQUEUE|CNVTACC|CNVTAGE|CNVTAGE2|CNVTAGEDATETIME|CNVTALIAS|CNVTALPHANUM|CNVTB10B16|CNVTB10B36|CNVTB16B10|CNVTB36B10|CNVTBOOL|CNVTCAP|CNVTDATE|CNVTDATE2|CNVTDATETIME|CNVTDATETIME2|CNVTDATETIMERDB|CNVTDATETIMEUTC|CNVTDATETIMEUTC2|CNVTDATETIMEUTC3|CNVTHEXRAW|CNVTINT|CNVTJSONTOREC|CNVTLOOKAHEAD|CNVTLOOKBEHIND|CNVTLOWER|CNVTMIN|CNVTMIN2|CNVTNLS|CNVTNLSSORT|CNVTPHONE|CNVTRAWHEX|CNVTREAL|CNVTRECTOJSON|CNVTRECTOXML|CNVTSTRING|CNVTSTRINGCHK|CNVTTIME|CNVTTIME2|CNVTTIMESTAMP|CNVTUPPER|CNVTXMLTOREC|CONCAT|COST|COUNT|CUBE|CURCODECOVER|CURFILE|CURLOCALE|CURPROG|DATETIMEADD|DATETIMECMP|DATETIMECMPUTC|DATETIMEDIFF|DATETIMEFIND|DATETIMEPART|DATETIMETRUNC|DATETIMEZONE|DATETIMEZONEBYINDEX|DATETIMEZONEBYNAME|DATETIMEZONEFORMAT|DATETIMEZONEUTC|DAY|DECODE|ECHO|ECHORECORD|ECHOJSON|ECHOXML|ERROR|EVALUATE|EVALUATE2|EVEN|EXP|EXPAND|FILLSTRING|FINDFILE|FINDSTRING|FLOOR|FORMAT|GREATEST|HOUR|ICHAR|INITARRAY|INITREC|ISNUMERIC|JULIAN|LEAST|LIST|LOCATEVAL|LOCATEVALSORT|LOG|LOG10|LOGICAL|MAX|MAXREC|MAXVAL|MEDIAN|MEMALLOC|MEMFREE|MEMREALLOC|MIN|MINUTE|MINVAL|MOD|MODCHECK|MODIFY|MONTH|MOVEREC|MOVERECLIST|MOVESTRING|NEGATE|NOPATSTRING|NORDBBIND|NOTRIM|NULL|NULLCHECK|NULLIND|NULLTERM|NULLVAL|OPERATOR|OUTERJOIN|PARAMETER|PARAMETER2|PARSER|PATSTRING|PERCENT|PERCENTILE|PIECE|PROXYUSER|RAND|RDBBIND|REFLECT|REMOVE|RENAMEREC|REPLACE|REPORTINFO|REPORTMOVE|REPORTROW|ROLLUP|ROUND|SELECTIVITY|SEQ|SIZE|SORT|SORTSEARCH|SOUND|SOUNDEX|SQLPASSTHRU|STDDEV|SUBSTRING|SUM|TDBEXECUTE|TEXT|TEXTLEN|TRACE|TRIM|TRIMBIND|TYPE|VALIDATE|VALUE|VARIANCE|WEEKDAY|WTMODCHECK|YEAR|UAR_GET_CODE_BY|UAR_GET_CODE_DESCRIPTION|UAR_GET_CODE_DISPLAY|UAR_GET_CODE_MEANING|UAR_GET_MEANING_BY_CODESET|UAR_RTF|UAR_RTF2|UAR_RTF3|UAR_OCF_UNCOMPRESS|UAR_CLOSEHANDLE|UAR_CREATEPROPLIST|UAR_SETPROPSTRING|UAR_TIMER_CREATE|UAR_TIMER_DESTROY|UAR_TIMER_STOP|'
                 r'CURACCEPT|CURBATCH|CURBEDROCK|CURCCLREV|CURCCLVER|CURCLIENTID|CURCLK|CURDATE|CURDOMAIN|CURECHO|CURENDREPORT|CURENV|CURGROUP|CURHELP|CURIMAGE|CURLOCALE|CURMEM|CURNETDOMAIN|CURNODE|CURPAGE|CURPRCNAME|CURPROG|CURQUAL|CURRDB|CURRDBACCESS|CURRDBHANDLE|CURRDBLINK|CURRDBNAME|CURRDBOPT|CURRDBSYS|CURRDBUSER|CURRETURN|CURREV|CURREF|CURREVHNAM|CURREVMINOR|CURREVMINOR2|CURSCROLL|CURSERVER|CURSOURCE|CURSYS|CURSYS2|CURTIME|CURTIME2|CURTIME3|CURTIMEZONE|CURTIMEZONEAPP|CURTIMEZONEDEF|CURTIMEZONESYS|CURUSER|CURUTC|CURUTCDIFF|CURWORK|null|SYSDATE|SYSTIMESTAMP|'
                 r'constant|noconstant|protect|public|private|privateprotect|persistscript)\b', Keyword),

            # variable types
            (r'\b(c1|c2|c3|c4|c5|c6|c7|c8|c9|c10|c11|c12|c13|c14|c15|c16|c17|c18|c19|c20|c21|c22|c23|c24|c25|c26|c27|c28|c29|c30|c31|c32|c80|c40|c45|c50|c55|c60|c64|c65|c70|c75|c80|c85|c90|c95|c100|c150|c160|c128|c125|c175|c200|c225|c250|c255|c275|c300|c1000|c2000|c3000|c4000|c32000|dq8|f8|i1|i2|i3|i4|i5|i6|i7|i8|i9|i10|i11|i12|q8|vc)\b', Keyword.Type),

            # all the rest is just text:
            (r'.', Text)
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ]
    }