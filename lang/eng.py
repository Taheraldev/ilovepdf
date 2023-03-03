# copyright ©️ 2021 nabilanavab
file_name = "lang/eng.py"


from configs.config   import settings

# REPLY MESSAGE FOR BROKEN WORKS
RESTART = {
    "msg" : """☠ `𝐎𝐕𝐄𝐑𝐋𝐎𝐀𝐃 𝐃𝐄𝐂𝐓𝐄𝐂𝐓𝐄𝐃`☠:\n__تحديث الخادم__ \n
لاحظت أن عملك كان أيضا في قائمة الانتظار
هل يمكنك المحاولة مرة أخرى من فضلك..!""",
    "btn" : { "🚶 أغلق 🚶" : "close|mee" }
}

# PM WELCOME MESSAGE (HOME A, B, C, D...)
HOME = {
    "HomeA" : "مرحبا بك {}..!!\n"
"في بوت {}.!\n\n"

"يمكن لهذا البوت تحويل الصور الPDF وكذلك تعديل علىPDF من قص ودمج وضغط وتشفير ودمج سلادين وغيرها…\n\n"  
"لمعرفة المزيد من خصائص البوت إضغط **⚠️ المساعدة ⚠️**",
    "HomeACB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        " 🌟تقييم 🌟": f"{str(settings.SOURCE_CODE)}",
        "🚶 اغلق 🚶": "close|mee"
    } ,
    "HomeAdminCB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        "🌟تقييم 🌟": f"{str(settings.SOURCE_CODE)}",
        "🗽 الحالة 🗽": "status|home", "🚶 قريب 🚶": "close|mee"
    } ,
    "HomeB" : """صفحة الإعدادات⚙️

اسم المستخدم   : {}
معرف المستخدم           : {}
اسم مستخدم    : {}
تاريخ الانضمام      : {}

لغة    : {}
API                    : {}
واجهة            : {}
تعليق         : {}
اسم الملف      : {}""",
    "HomeBCB" : {
        "📍 واجهك 📍" : "set|thumb",
        "📈 الاسم 📈" : "set|fname",
        "💩 API 💩" : "set|api",
        "📅 تعليق 📅" : "set|capt",
        "« العودة الرئيسية «" : "Home|B2A"
    },
    "HomeC": """🪂 ** رسالة مساعدة **:

``` بعض الميزات الرئيسية هي:
 ◍ تحويل الصور إلى PDF \n ◍ Manupultions PDF \n ◍ العديد من برامج الترميز الشائعة إلى pdf
 
تعديل ملف pdf:
 ◍ PDF⥃ الصور [الكل , النطاق , الصفحات] \n ◍ المستندات إلى PDF [png , jpg , jpeg] \n ◍ الصور PDF \n ◍ بيانات PDF الوصفية \n ◍ PDF⥃TEXT \n ◍ TEXT⥃PDF \n ◍ ضغط ملف pdf
 ◍ انقسام PDF [النطاق , الصفحات] \n ◍ دمج PDF \n ◍ إضافة طابع \n ◍ إعادة تسمية PDF \n ◍ تدوير PDF \n ◍ ENCRYPT / DECRYPT PDF \n ◍ PDF FORMATTER \n ◍ PDF⥃JSON / TXT FILE
 ◍ PDF⥃HTML [عرض الويب] \n ◍ URL⥃PDF \n ◍ PDF⥃ZIP / TAR / RAR [الكل , النطاق , الصفحات] \n وأكثر من ذلك بكثير .. """ ,
    "HomeCCB": {"« BACK HOME «": "Home|A", "🛈 INSTRUCTIONS 🛈": "Home|D"},
    "HomeD": """` نظرًا لأن هذه خدمة مجانية , لا يمكنني ضمان المدة التي يمكنني خلالها الحفاظ على هذه الخدمة ..`😝
 
⚠️ تعليمات ⚠️:
🛈 __يرجى عدم محاولة إساءة استخدام إدارة Bot__ 😒
🛈 __لا ترسل بريدًا عشوائيًا هنا , فقد يؤدي ذلك إلى حظر دائم 🎲__.
🛈 __محتويات الاباحيه ايضا ستمنحك حظر دائم 💯__

** أرسل أي صورة لتبدأ: ** 😁 """,
    "HomeDCB": {"⚠️ مساعدة ⚠️": "Home|C", "» عودة للرئيسية »": "Home|A"}
}

# GROUP WELCOME MESSAGE
HomeG = {
    "HomeA" : HOME['HomeA'],
    "HomeACB" : {
        "🌍 اللغة 🌍" : "set|lang",
        "🛡️ المساعدة 🛡️": "Home|C",
        "📢 القناة 📢" : f"{str(settings.OWNED_CHANNEL)}",
        "🌟 التقييم 🌟": f"{settings.SOURCE_CODE}",
        "🚶 اغلق 🚶" : "close|mee",
    }
}

SETTINGS = {
    "lang" : "الآن، اختر أي لغة..",
    "default" : ["الافتراضي ❌", "CUSTOM ✅"],
    "cant" : "لا يمكن استخدام هذه الميزة ❌",
    "wait" : { "في انتظار.. 🥱" : "nabilanavab" },
    "feedbtn" : { "أبلغ عن أي أخطاء تجدها!" : settings.REPORT },
    "chgLang" : {"الإعداد ⚙️ » تغيير لانج 🌐" : "nabilanavab"},
    "askApi" : "\n\nافتح الرابط **أدناه** وأرسل لي الرمز السري:",
    "waitApi" : { "افتح الرابط ✅" : "https://www.convertapi.com/a/signin" },
    "error" : "حدث خطأ ما أثناء استرداد البيانات من قاعدة البيانات",
    "result" : ["لا يمكن تحديث الإعدادات ❌", "تم تحديث الإعدادات بنجاح ✅"],
    "back" : [{ "« الرئيسية «" : "Home|B2S" }, { "« الرئيسية «" : "Home|B2A" }],
    "feedback" : "تحذير من الأخطاء! إذا كانت رسائلي تبدو غريبة، فمن المحتمل أن يكون خطأ ترجمة جوجل."
                 "\n\nأبلغ عن خطأ في {} Lang:\n`• حدد Lang\n• رسالة خطأ\n• رسالة جديدة`",
    "ask" : [
        "الآن، أرسل لي..",
        "الآن، أرسل لي.. 😅\n\nبعيد.! ليس لدي المزيد من الوقت لمراجعة النص.. 😏\n\n/cancel: للإلغاء"
    ],
    "thumb" : [
        {
            "الاعدادات ⚙️ » THUMBNAIL 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|thumb+",
            "« الرئيسية «" : "Home|B"
        },
        {
            "الاعدادات ⚙️ » THUMBNAIL 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|thumb+",
            "🗑 حذف 🗑" : "set|thumb-",
            "«  الرئيسية«" : "Home|B2S"
        }
    ],
    "fname" : [
        {
            "الاعدادات ⚙️ » FNAME 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|fname+",
            "« الرئيسية «" : "Home|B2S"
        },
        {
            "الاعدادات ⚙️ » FNAME 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|fname+",
            "🗑 حذف 🗑" : "set|fname-",
            "« الرئيسية «" : "Home|B2S"
        }
    ],
    "api" : [
        {
            "الاعدادات ⚙️ » API 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|api+",
            "« الرئيسية «" : "Home|B2S"
        },
        {
            "الاعدادات ⚙️ » API 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|api+",
            "🗑 حذف 🗑" : "set|api-",
            "« الرئيسية «" : "Home|B2S"
        }
    ],
    "capt" : [
        {
            "الاعدادات ⚙️ » CAPTION 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|capt+",
            "« الرئيسية «" : "Home|B2S"
        },
        {
            "الاعدادات ⚙️ » CAPTION 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|capt+",
            "🗑 حذف 🗑" : "set|capt-",
            "« الرئيسية «" : "Home|B2S"
        }
    ]
}

BOT_COMMAND = {"start": "رسالة ترحيب ..", "txt2pdf": "إنشاء ملف PDF نصي"}

STATUS_MSG = {
    "HOME": "الآن , حدد أي خيار أدناه للحصول على الحالة الحالية 💱 ..` ",
    "_HOME" : {
        "📊 ↓ SERVER ↓ 📊": "nabilanavab", "📶 STORAGE 📶": "status|server",
        "🥥 قاعدة البيانات 🥥": "status|db" , "🌝 ↓ الحصول على قائمة ↓ 🌝": "nabilanavab",
        "💎 المشرف 💎": "status|admin", "👤 المستخدمون 👤": "status|users",
        "« رجوع  «": "Home|A"
    } ,
    "DB": """📂 قاعدة البيانات: \n \n ** ◍ مستخدمو قاعدة البيانات: **` {} `📍 \n ** ◍ محادثات قاعدة البيانات: **` {} `📍""" ,
    "SERVER": """** ◍ المساحة الإجمالية: **` {} `
** ◍ المساحة المستخدمة: ** `{} ({}٪)` \n ** ◍ مساحة حرة: ** `{}`
** ◍ استخدام وحدة المعالجة المركزية: ** "{}`٪ \n ** ◍ استخدام ذاكرة الوصول العشوائي: ** `{}`٪
** ◍ العمل الحالي: ** `{}` \n ** ◍ معرف الرسالة: ** `{}""" ,
    "BACK": {"« BACK «": "status|home"}, "ADMIN": "** Total ADMIN: ** __ {} __ \n",
    "USERS": "المستخدمون: \n\n" , "NO_DB": "لم يتم تعيين قاعدة البيانات بعد 💩"
}

feedbackMsg = f"[اكتب تعليقًا 📋]({settings.FEEDBACK})"

BAN = {
    "UCantUse" : """مرحبا {}

لسبب ما لا يمكنك استخدام هذا الروبوت:(""",
    "UCantUseDB" : """مرحبا {}

لسبب ما لا يمكنك استخدام هذا الروبوت :(

سبب: {}""",
    "GroupCantUse" : """{} لا تتوقع أبدا استجابة جيدة مني
منعني المشرفون من العمل هنا.. 🤭""",
    "GroupCantUseDB" : """{} لا تتوقع أبدا استجابة جيدة مني
منعني المشرفون من العمل هنا.. 🤭

سبب: {}""",
    "cbNotU" : "عفوا، آسف لكسر قلبك، هذه الرسالة ليست لك 💔.\n\nحظا أفضل في المرة القادمة! 😏",
    "Fool" : "من فضلك لا تحاول خداعي.. 🤭",
    "banCB" : {
        "قناة البوت": f"{settings.SOURCE_CODE}",
        "تابع تحديثات": f"{settings.SOURCE_CODE}",
        "انضم": "https://telegram.dog/i2pdfbotchannel"
    },
    "Force" : """مرحبا [{}](tg://user?id={}) 🤚🏻..!!
🚸| عذرا عزيزي | sorry dear
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه:
🔰|  You have to subscribe to the bot channel to be able to use it:
👇👇👇👇
 @i2pdfbotchannel""",
    "ForceCB" : {
        "🌟أنظم في قناة🌟" : "{0}",
        "♻️ تحديث ♻️" : "refresh{1}"
    },
}

checkPdf = {
    "pg" : "`عدد الصفحات: •{}•` 🌟",
    "pdf" : """`ماذا عليّ أن أفعل بهذا الملف.?`

اسم الملف : `{}`
حجم الملف : `{}`""",
    "pdfCB1" : {
        "⭐ معلومات ⭐" : "metaData",
        "🗳️ عرض 🗳️" : "preview",
        "🖼️ الصور 🖼️" : "pdf|img",
        "✏️ نص ✏️" : "pdf|txt",
        "🔐 تشفير 🔐" : "work|encrypt",
        "🔒 فك تشفير 🔓" : "work|decrypt",
        "🗜️ ضغط 🗜️" : "work|compress",
        "🤸 تدوير 🤸" : "pdf|rotate",
        "✂️ تقسيم ✂️" : "pdf|split",
        "🧬 دمج 🧬" : "merge",
        "™️ ختم ™️" : "pdf|stp",
        "✏️ إعادة تسمية ✏️" : "work|rename",
        "🔗 رابط 🔗" : "link",
        "» 🏴‍☠️ المزيد 🏴‍☠️ »" : "pdf2",
        "🚫 أغلق 🚫" : "close|all"
    },
    "pdfCB2" : {
        " ↓ الصفحة الثانية  ↓ " : "nabilanavab",
        "📝 OCR 📝" : "work|ocr",
        "🥷 A4 تنسيق 🥷" : "work|format", 
        "🖤 أسود/أبيض 🤍" : "baw",
        "🍴 ساتوتيشن 🍴" : "sat",
        "📎 اربع سلايدات 📎" : "comb",
        "🔎 تكبير PDF 🔎" : "zoom",
        "➖ حذف الصفحات ➖": "close|dev",
        "➕ أضف صفحات ➕" : "close|dev",
        "🎨 رسم PDF 🎨" : "draw",
        "😈 سلايدين 😈" : "close|dev",
        "💦 عَلامة مائيّة 💦" : "close|dev",
        "« 🏴‍☠️ عودة 🏴‍☠️ «" : "pdf1",
        "🚫 أغلق 🚫" : "close|all"
    },
    "error" : """__لا يمكنني فعل أي شيء بهذا الملف.__ 😏

🐉  `CODEC ERROR`  🐉""",
    "errorCB" : {
        "❌ خطأ في الترميز ❌" : "error",
        "🔸 آغلق 🔸" : "close|all"
    },
    "encrypt" : """`الملف مشفر.` 🔐

اسم الملف: `{}`
حجم الملف: `{}`""",
    "encryptCB" : {"🔓 فك تشفير 🔓" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """\n**تم✅ : **{0}/{1}
**السرعة🚀:** {2}/s
**الوقت المستغرق ⏳:** {3}""",
    "workInP" : "العمل قيد التقدم.. 🙇",
    "upFile" : "`بدأ التحميل.. `📤",
    "refresh" : { "♻️ تحديث ♻️" : "{}" },
    "dlFile" : "`تنزيل ملفك..` 📥",
    "dlImage" : "`قم بتنزيل صورتك.. ⏳`",
    "upFileCB" : {"📤 .. تحميل.. 📤" : "nabilanavab"},
    "takeTime" : """```⚙️ العمل قيد التقدم..`
`قد يستغرق الأمر بعض الوقت..```💛""",
    "cbPRO_D" : ["📤 تنزيل: {:.2f}% 📤", "🎯 الالغاء 🎯"],
    "cbPRO_U" : ["📤 تحميل: {:.2f}% 📤", "🎯 الالغاء 🎯"]
}

GENERATE = {
    "noQueue" : "`لم يتم العثور على قائمة انتظار..`😲",
    "noImages" : "لم يتم العثور على صورة.!! 😒",
    "currDL" : "تم تنزيل {} صور 🥱",
    "geting" : "اسم الملف: `{}`\nالصفحات: `{}`",
    "getFileNm" : "أرسل لي الآن اسم الملف 😒: ",
    "deleteQueue" : "`تم حذف قائمة الانتظار بنجاح..`🤧",
    "getingCB" : {"📚 إنشاء ملف PDF.." : "nabilanavab"},
}

document = {
    "reply" : checkPdf['pdf'],
    "upFile" : PROGRESS['upFile'],
    "process" : "⚙️ المعالجة..",
    "replyCB" : checkPdf['pdfCB1'],
    "inWork" : PROGRESS['workInP'],
    "download" : PROGRESS['dlFile'],
    "refresh" : PROGRESS['refresh'],
    "dlImage" : PROGRESS['dlImage'],
    "takeTime" : PROGRESS['takeTime'],
    "fromFile" : "`تم التحويل: {} إلى {}`",
    "unsupport" : "ملف غير مدعوم.. 🙄`",
    "cancelCB" : { "⟨ الالغاء ⟩" : "close|me" },
    "generate" : { "الانشاء 📚" : "generate" },
    "generateRN" : {
        "الانشاء 📚" : "generate",
        "إعادة التسمية ✍️" : "generateREN"
    },
    "noAPI" : """`يرجى إضافة واجهة برمجة تطبيقات التحويل.. 💩

/start » الاعدادات » api » إضافة/تغيير`""",
    "error" : """حدث خطأ ما.. 🐉

خطا: `{}`""",
    "setHdImg" : """الآن الصورة إلى PDF في وضع HD 😈""",
    "setDefault" : { "« العودة إلى الجودة الافتراضية «" : "close|hd" },
    "useDOCKER" : "`الملف غير مدعوم، قم بنشر الروبوت باستخدام عامل الميناء`",
    "big" : """بسبب الحمل الزائد، حدود المالك {}MB لملفات pdf 🙇

`من فضلك أرسل لي ملفا أقل من {}MB Size` 🙃""",
    "bigCB" : {
        "💎 قناة البوت 💎" : "https://t.me/i2pdfbotchannel"
    },
    "imageAdded" : """`تمت إضافة {} صفحات إلى ملف PDF الخاص بك..`🤓

اسم الملف: `{}.pdf`"""
}

gDocument = {
    "admin" : """بسبب بعض حدود تيليجرام..
لا يمكنني العمل إلا كمشرف
__من فضلك قم بالترويج لي كمشرف__ ☺️""",
    "notDOC" : "أخي، يرجى الرد على مستند أو صورة.. 🤧",
    "Gadmin" : """يمكن لمسؤولي المجموعة فقط استخدام هذا الروبوت
وإلا تعال إلى جهازي الشخصي 😋""",
    "adminO" : """`يمكن للمشرفين فقط القيام بذلك..`

أو جرب ملفات pdf الخاصة بك(__الرد على رسالتك__)"""
}
gDocument.update(document)

noHelp = f"`لن يساعدك أحد` 😏"

split = {
    "work" : ["Range", "Single"],
    "inWork" : PROGRESS['workInP'],
    "download" : PROGRESS['dlFile'],
    "cancelCB" : document['cancelCB'],
    "exit" : "`تم إلغاء العملية..` 😏",
    "button" : {
        "⚙️ PDF » تقسيم ↓" : "nabilanavab",
        "بنطاق 🦞" : "split|R",
        "صفحات منفصلة 🐛" : "split|S",
        "« عودة «" : "pdf1"
    },
    "over" : "`انتهت 5 محاولات.. تم إلغاء العملية..`😏",
    "pyromodASK_1" : """__PDF تقسيم » تقسيم بنطاق\n
الآن، أدخل النطاق (البداية: النهاية) :__

/exit __للإلغاء__""",
    "completed" : "`اكتمل التنزيل..` ✅",
    "error_1" : "`خطا بنطاق: justNeedStartAndEnd `🚶",
    "error_2" : "`خطا بنطاق: errorInEndingPageNumber `🚶",
    "error_3" : "`خطا بنطاق: errorInStartingPageNumber `🚶",
    "error_4" : "`خطا بنطاق pageNumberMustBeADigit` 🧠",
    "error_5" : "`خطا بنطاق: noEndingPageNumber Or notADigit` 🚶",
    "error_6" : "`لا يمكنني العثور على أي رقم..`😏",
    "error_7" : "`حدث خطأ ما..`😅",
    "error_8" : "`أدخل أرقاما أقل من {}..`😏",
    "error_9" : "`التحقق الأول من عدد الصفحات` 😏",
    "upload" : "⚙️ `بدأت التحميل..` 📤"
}

pdf2IMG = {
    "uploadfile" : split["upload"],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "toImage" : {
        "⚙️ PDF » صور ↓" : "nabilanavab",
        "🖼 صور 🖼" : "pdf|img|img",
        "📂 ملف 📂" : "pdf|img|doc",
        "🤐 ZIP 🤐" : "pdf|img|zip",
        "🎯 TAR 🎯" : "pdf|img|tar",
        "« عودة «" : "pdf1" 
    },
    "imgRange" : {
        "⚙️ PDF » صور » {} ↓" : "nabilanavab",
        "🙄 الكل 🙄" : "p2img|{}A",
        "🤧 بنطاق 🤧" : "p2img|{}R",
        "🌝 صفحات 🌝" : "p2img|{}S",
        "« عودة «" : "pdf|img"
    },
    "over" : "`5 محاولات انتهت.. تم إلغاء العملية..`😏",
    "pyromodASK_1" : """__Pdf - Img›Doc » صفحات:
الآن، أدخل النطاق (البداية: النهاية) :__

/exit __للإلغاء__""",
    "pyromodASK_2" : """"__Pdf - Img›Doc » صفحات:
الآن، أدخل أرقام الصفحات المفصلة بواسطة__ (,) :

/exit __للإلغاء__""",
    "exit" : "`تم إلغاء العملية..` 😏",
    "error_1" : "`خطا بكتابة جملة: justNeedStartAndEnd `🚶",
    "error_2" : "`خطا بكتابة جملة: errorInEndingPageNumber `🚶",
    "error_3" : "`خطا بكتابة جملة: errorInStartingPageNumber `🚶",
    "error_4" : "`خطا بكتابة جملة: pageNumberMustBeADigit` 🧠",
    "error_5" : "`خطا بكتابة جملة: noEndingPageNumber Or notADigit` 🚶",
    "error_6" : "`لا يمكنني العثور على أي رقم..`😏",
    "error_7" : "`حدث خطأ ما..`😅",
    "error_8" : "`يحتوي ملف PDF على {} صفحات فقط` 💩",
    "error_9" : "`التحقق الأول من عدد الصفحات` 😏",
    "error_10" : "__بسبب بعض القيود، يرسل بوت 50 صفحة فقط كرمز البريدي..__😅",
    "total" : "`مجموع الصفحات: {}..⏳`",
    "upload" : "`تحميل: {}/{} الصفحات.. 🐬`",
    "current" : "`حولت: {}/{} الصفحات.. 🤞`",
    "complete" : "`اكتمل التحميل..`🏌️",
    "canceledAT" : "`الغيت {}/{} الصفحات..` 🙄",
    "cbAns" : "⚙️ إلغاء... ",
    "cancelCB" : {"💤 إلغاء 💤" : "close|P2I"},     # EDITABLE: ❌
    "canceledCB" : {"🍄 ملغية 🍄" : "close|P2IDONE"},
    "completed" : {"😎 مكتملة 😎" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "upload" : PROGRESS['upFile'],
    "load" : "__بسبب التحميل الزائد، يمكنك دمج 5 ملفات PDF فقط في كل مرة__",
    "sizeLoad" : "`بسبب التحميل الزائد، يدعم Bot فقط %sMb PDFs..", # removing %s show error
    "pyromodASK" : """__دمج pdfs » إجمالي ملفات PDF في قائمة الانتظار: {}__

/exit __للإلغاء__

/merge __لدمج__""",
    "exit" : "`تم إلغاء العملية..` 😏",
    "total" : "`إجمالي ملفات PDF: {} 💡",
    "current" : "__بدأت في تنزيل ملف PDF: {} 📥__",
    "cancel" : "`تم إلغاء عملية الدمج.. 😏`",
    "started" : "__بدأ الدمج__ 🪄",
    "caption" : "`ملف PDF مدمج 🙂`",
    "error" : """`قد يكون الملف مشفرا..`

سبب: {}"""
}

metaData = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],   # [❌]
    "read" : "يرجى قراءة هذه الرسالة مرة أخرى.. 🥴"
}

preview = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "error" : document['error'],
    "download" : PROGRESS['dlFile'],
    "_" : "يحتوي ملف PDF على {} صفحات فقط 🤓\n\n",
    "__" : "صفحات PDF: {}\n\n",
    "total" : "`مجموع الصفحات: {}..` 🤌",
    "album" : "`إعداد ألبوم..` 🤹",
    "upload" : f"`التحميل: صفحات المعاينة.. 🐬`"
}

stamp = {
    "stamp": {
        "⚙️ PDF» STAMP ↓ ":"nabilanavab",
        "ليس للنشر العام 🤧": "pdf|stp|10",
        "للإصدار العام 🥱": "pdf|stp|8",
        "سري 🤫": "pdf|stp|2", "Departmental 🤝": "pdf|stp|3",
        "التجريبية 🔬": "pdf|stp|4", "انتهاء الصلاحية 🐀": "pdf|stp|5",
        "نهائي 🔧": "pdf|stp|6", "للتعليق 🗯️": "pdf|stp|7",
        "غير معتمد 😒": "pdf|stp|9", "موافق عليه 🥳": "pdf|stp|0",
        "تم البيع ✊": "pdf|stp|11", "سري للغاية 😷": "pdf|stp|12",
        "مسودة 👀": "pdf|stp|13", "AsIs 🤏": "pdf|stp|1",
        "« رجوع «": "pdf"
    } ,
    "stampA": {
        "⚙️ PDF» STAMP »COLOR ↓": "nabilanavab" ,
        "أحمر ❤️": "spP|{}|r", "أزرق 💙": "spP|{}|b" ,
        "أخضر 💚": "spP|{}|g", "Yellow 💛": "spP|{}|c1",
        "الوردي 💜": "spP|{}|c2" , "Hue 💚": "spP|{}|c3" ,
        "أبيض 🤍": "spP|{}|c4", "أسود 🖤": "spP|{}|c5" ,
        "« رجوع «": "pdf|stp"
    } ,
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'] , "upload": PROGRESS['upFile'] ,
    "stamping": "بدء ختم..` 💠", "caption": """pdf مختوم \n اللون:` {} `\n لا:` {} `"""
}

work = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'],
    "button" : document['cancelCB'],
    "rot360" : "لديك بعض **مشكلة كبيرة.. 🙂**",
    "ocrError" : "مالك محضور 😎🤏",
    "largeNo" : "أرسل ملف PDF أقل من 5 صفحات.. 🙄",
    "pyromodASK_1" : """__PDF {} »
الآن، يرجى إدخال كلمة المرور :__

/exit __للإلغاء__""",
    "pyromodASK_2" : """__تمسية PDF »
الآن، يرجى إدخال الاسم الجديد:__

/exit __للإلغاء__""",
    "exit" : "`تم إلغاء العملية..`😏",
    "ren_caption" : "__اسم جديد:__ `{}`", 
    "notENCRYPTED" : "`الملف غير مشفر..` 👀",
    "compress" : """⚙️ ```بدأت في الضغط..🌡️
قد يستغرق ذلك بعض الوقت..```💛""",
    "decrypt" : """⚙️ ```بدأت في فك التشفير.. 🔓
قد يستغرق ذلك بعض الوقت..```💛""",
    "encrypt" : """⚙️ ```بدأت في التشفير.. 🔐
قد يستغرق ذلك بعض الوقت..```💛""",
    "ocr" : """⚙️ ```إضافة طبقة التعرف الضوئي على الحروف.. ✍️
قد يستغرق ذلك بعض الوقت..```💛""",
    "format" : """⚙️ ```بدأت التنسيق.. 🤘
قد يستغرق ذلك بعض الوقت..```💛""",
    "rename" : """⚙️ ```إعادة تسمية PDf..✏️
قد يستغرق ذلك بعض الوقت..```💛""",
    "rot" : """⚙️ ```تدوير PDf.. 🤸
قد يستغرق ذلك بعض الوقت..```💛""",
    "pdfTxt" : """⚙️ ```استخراج النص.. 🐾
قد يستغرق الأمر بعض الوقت..```💛""",
    "fileNm" : """اسم الملف القديم: {}
اسم ملف جديد: {}""",
    "rotate" : {
        "⚙️ PDF » تدوير ↓" : "nabilanavab",
        "90°" : "work|rot90",
        "180°" : "work|rot180",
        "270°" : "work|rot270",
        "360°" : "work|rot360",
        "« عودة «" : "pdf1"
    },
    "txt" : {
        "⚙️ PDF » نص ↓" : "nabilanavab",
        "📜 رسالة 📜" : "work|M",
        "🧾 ملف نصي 🧾" : "work|T",
        "🌐 HTML 🌐" : "work|H",
        "🎀 JSON 🎀" : "work|J",
        "« عودة «" : "pdf1"
    }
}

PROCESS = {
    "ocr" : "OCR added",
    "decryptError" : "__لا يمكن فك تشفير الملف باستخدام__ `{}` 🕸️",
    "decrypted" : "__ملف غير مشفر__",
    "encrypted" : "__رقم الصفحة__: {}\n__المفتاح__ 🔐: ||{}||",
    "compressed" : """`الحجم الأصلي : {}
الحجم المضغوط. : {}

النسبة : {:.2f} %`""",
    "cantCompress" : "لا يمكن ضغط الملف أكثر.. 🤐",
    "pgNoError" : """__لسبب ما يدعم تنسيق A4 فقط ملفات PDF التي تحتوي على أقل من 5 صفحات__

مجموع صفحات: {} ⭐""",
    "ocrError" : "`لديك بالفعل طبقة نصية.. `😏",
    "90" : "__دور ب 90°__",
    "180" : "__دور ب 180°__",
    "270" : "__دور ب 270°__",
    "formatted" : "ملف بتنسيق A4",
    "M" : "♻ صفحات {} مستخرجة ♻",
    "H" : "HTML ملف",
    "T" : "TXT ملف",
    "J" : "JSON ملف"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"],
    "exit" : split['exit'],
    "nothing" : "لا شيء لإنشائه.. 😏",
    "TEXT" : "`قم بإنشاء ملف PDF من الرسائل النصية »`",
    "start" : "بدأت في تحويل النص إلى قوات دي إف.. 🎉",
    "font_btn" : {
        "TXT@PDF » تعيين الخط" : "nabilanavab",
        "Times" : "pdf|font|t",
        "Courier" : "pdf|font|c",
        "Helvetica (Default)" : "pdf|font|h",
        "Symbol" : "pdf|font|s",
        "Zapfdingbats" : "pdf|font|z",
        "🚫 اغلق 🚫" : "close|me"
    },
    "size_btn" : {
        "TXT@PDF » {} » مقياس محدد" : "nabilanavab",
        "Portarate" : "t2p|{}|p",
        "Landscape" : "t2p|{}|l",
        "« عودة «": "pdf|T2P"
    },
    "askT" : """__نص إلى PDF » الآن، يرجى إدخال عنوان:__

/exit __للالغاء__\n/skip __to skip__""",
    "askC" : """__النص إلى PDF » الآن، يرجى إدخال الفقرة{}:__

/exit __للالغاء__\n/create __لإنشاء __"""
}

URL = {
    "notPDF" : "`ليس ملف PDF",
    "close" : { "close" : "close|all" },
    "get" : {"🧭 احصل على ملف PDF 🧭" : "getFile"},
    "error" : """🐉 حدث خطأ ما 🐉,

ERROR: `{}`

NB: In Groups, Bots Can Only fetch documents Send After Joining Group =)""",
    "done" : "```Almost Done.. ✅\nNow, Started Uploading.. 📤```",
    "_error_" : "send me any url or direct telegram pdf links",
    "openCB" : {"Open In Browser" : "{}"},
    "_error" : "`Some Thing Went Wrong =(`\n\n`{}`",
    "_get" : """[Open Chat]({})

**ABOUT CHAT ↓**
Chat Type   : {}
Chat Name : {}
Chat Usr    : @{}
Chat ID        : {}
Date : {}

**ABOUT MEDIA ↓**
Media       : {}
File Name : {}
File Size   : {}
File Type : {}"""
}

getFILE = {
    "wait" : "Wait.. Let me.. 😜",
    "inWork" : PROGRESS['workInP'],
    "big" : "Send PDF url less than {}mb",
    "dl" : {"📥 ..DOWNLOADING.. 📥" : "nabilanavab"},
    "up" : {"📤 ..UPLOADING..  📤" : "nabilanavab"},
    "complete" : {"😎 COMPLETED 😎" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "This feature is Under Development ⛷️",
    "Error annenn paranjille.. then what.. 😏",
    "Process Canceled.. 😏",
    "File Not Encrypted.. 👀",
    "Nothing Official About it.. 😅",
    "🎉 Completed.. 🏃"
]

wa = {
    "exit" : split["exit"],
    "over" : pdf2IMG['over'],
    "upFile" : PROGRESS['upFile'],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "error" : "Something went Wrong 🙂",
    "cancelCB" : {"⟨ Cancel ⟩" : "close|me"},
    "add" : "Adding watermark to PDF File 💩",
    "waDL" : "__Getting watermark File..__ 🙄",
    "type" : {
        "⚙️ PDF » WATERMARK ↓" : "nabilanavab",
        "TEXT" : "pdf|wa|txt",
        "IMAGE" : "pdf|wa|img",
        "PDF" : "pdf|wa|pdf",
        "« BACK «" : "pdf2"
    },
    "op" : {
        "⚙️ PDF » WATERMARK » {} » OPCACiTY ↓" : "nabilanavab",
        "10 %":"pdf|wa|{}|o01",
        "20 %":"pdf|wa|{}|o02",
        "30 %":"pdf|wa|{}|o03",
        "40 %":"pdf|wa|{}|o04",
        "50 %":"pdf|wa|{}|o05",
        "60 %":"pdf|wa|{}|o06",
        "70 %":"pdf|wa|{}|o07",
        "80 %":"pdf|wa|{}|o08",
        "90 %":"pdf|wa|{}|o09",
        "100 %":"pdf|wa|{}|o10",
        "« BACK «" : "pdf|wa"
    },
    "po" : {
        "⚙️ PDF » WATERMARK » POSiTiON ↓" : "nabilanavab",
        "᠎᠎᠎ " : "wa|{0}|{1}|TL",
        "᠎᠎   " : "wa|{0}|{1}|TM",
        "᠎᠎ " : "wa|{0}|{1}|TR",
        "᠎᠎  " : "wa|{0}|{1}|ML",
        "᠎᠎　" : "wa|{0}|{1}|MM",
        "᠎᠎⠀ ⠀" : "wa|{0}|{1}|MR",
        "᠎᠎ " : "wa|{0}|{1}|BL",
        "᠎ ᠎ " : "wa|{0}|{1}|BM",
        "᠎  ᠎ " : "wa|{0}|{1}|BR",
        "« BACK «" : "pdf|wa|{0}"
    }, 
    "txt" : """__Now, Send me any Text Message__

/exit : to cancel""", 
    "pdf" : """__Send me the watermark pdf.__

/exit : to cancel""",
    "img" : """__Send me the watermark Image as file.__
__ Supported Files [png, jpeg, jpg]__

/exit : to cancel""",
}

comb = {
    "upFile" : PROGRESS['upFile'],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "cancelCB" : {"⟨ Cancel ⟩" : "close|me"},
}

inline_query = {
    "capt" : "SET LANGUAGE ⚙️",
    "des" : "By: @nabilanavab ❤",
    "TOP" : { "Now, Select Language ⮷" : "nabilanavab" },
}

LINK = {
    "gen" : "`🔗 Generating..`",
    "_gen" : """```🔗 Generating..
We're working on it!

Please allow a moment for the processing to complete.```""",
    "no" : "Unfortunately, we encountered an error 😓",
    "type" : """`🔗 Generating..`

**Public** 📢:
__The file accessed via this link will be publicly available, allowing anyone to save and forward it__.


**Protect** 🔐:
__Ensures the confidentiality of the message by preventing its forwarding and saving__.""",
    "notify" : "Get Notify when a someone fetch this pdf",
    "notify_pvt" : {
        "🔔 NOTIFY 🔔" : "link-pvt-ntf",
        "🔕 MUTE 🔕" : "link-pvt-mut"
    },
    "notify_pub" : {
        "🔔 NOTIFY 🔔" : "link-pbc-ntf",
        "🔕 MUTE 🔕" : "link-pbc-mut"
    },
    "typeBTN" : {
        "📢 PUBLIC 📢" : "link-pub",
        "🔐 PRIVATE 🔐" : "link-pvt"
    },
    "link" : "**Here it is! This is what you were searching for..**",
    "error" : "Oops, it looks like something went wrong. Please try again later.\n\n`ERROR:` {}"
}

DELETE = {
    "button" : {
        "⚙️ PDF » SPLIT ↓" : "nabilanavab",
        "With In Range 🦞" : "split|dR",
        "Single Page 🐛" : "split|dS",
        "« BACK «" : "pdf1"
    },
}
