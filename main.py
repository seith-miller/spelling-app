import time
import random
from gtts import gTTS
import os

words = [
    "the",
    "of",
    "and",
    "to",
    "a",
    "in",
    "for",
    "is",
    "on",
    "that",
    "by",
    "this",
    "with",
    "i",
    "you",
    "it",
    "not",
    "or",
    "be",
    "are",
    "from",
    "at",
    "as",
    "your",
    "all",
    "have",
    "new",
    "more",
    "an",
    "was",
    "we",
    "will",
    "home",
    "can",
    "us",
    "about",
    "if",
    "page",
    "my",
    "has",
    "search",
    "free",
    "but",
    "our",
    "one",
    "other",
    "do",
    "no",
    "information",
    "time",
    "they",
    "site",
    "he",
    "up",
    "may",
    "what",
    "which",
    "their",
    "news",
    "out",
    "use",
    "any",
    "there",
    "see",
    "only",
    "so",
    "his",
    "when",
    "contact",
    "here",
    "business",
    "who",
    "web",
    "also",
    "now",
    "help",
    "get",
    "pm",
    "view",
    "online",
    "first",
    "am",
    "been",
    "would",
    "how",
    "were",
    "me",
    "services",
    "some",
    "these",
    "click",
    "its",
    "like",
    "service",
    "than",
    "find",
    "price",
    "date",
    "back",
    "top",
    "people",
    "had",
    "list",
    "name",
    "just",
    "over",
    "state",
    "year",
    "day",
    "into",
    "email",
    "two",
    "health",
    "world",
    "re",
    "next",
    "used",
    "go",
    "work",
    "last",
    "most",
    "products",
    "music",
    "buy",
    "data",
    "make",
    "them",
    "should",
    "product",
    "system",
    "post",
    "city",
    "policy",
    "number",
    "such",
    "please",
    "available",
    "copyright",
    "support",
    "message",
    "after",
    "best",
    "software",
    "then",
    "jan",
    "good",
    "video",
    "well",
    "where",
    "info",
    "rights",
    "public",
    "books",
    "high",
    "school",
    "through",
    "each",
    "links",
    "she",
    "review",
    "years",
    "order",
    "very",
    "privacy",
    "book",
    "items",
    "company",
    "read",
    "group",
    "need",
    "many",
    "user",
    "said",
    "does",
    "set",
    "under",
    "general",
    "research",
    "university",
    "january",
    "mail",
    "full",
    "map",
    "reviews",
    "program",
    "life",
    "know",
    "games",
    "way",
    "days",
    "management",
    "part",
    "could",
    "great",
    "united",
    "hotel",
    "real",
    "item",
    "international",
    "center",
    "must",
    "store",
    "travel",
    "comments",
    "made",
    "development",
    "report",
    "member",
    "details",
    "line",
    "terms",
    "before",
    "hotels",
    "did",
    "send",
    "right",
    "type",
    "because",
    "local",
    "those",
    "using",
    "results",
    "office",
    "education",
    "national",
    "car",
    "design",
    "take",
    "posted",
    "internet",
    "address",
    "community",
    "within",
    "states",
    "area",
    "want",
    "phone",
    "shipping",
    "reserved",
    "subject",
    "between",
    "forum",
    "family",
    "long",
    "based",
    "code",
    "show",
    "even",
    "black",
    "check",
    "special",
    "prices",
    "website",
    "index",
    "being",
    "women",
    "much",
    "sign",
    "file",
    "link",
    "open",
    "today",
    "technology",
    "south",
    "case",
    "project",
    "same",
    "pages",
    "uk",
    "version",
    "section",
    "own",
    "found",
    "sports",
    "house",
    "related",
    "security",
    "both",
    "county",
    "american",
    "photo",
    "game",
    "members",
    "power",
    "while",
    "care",
    "network",
    "down",
    "computer",
    "systems",
    "three",
    "total",
    "place",
    "end",
    "following",
    "download",
    "him",
    "without",
    "per",
    "access",
    "think",
    "north",
    "resources",
    "current",
    "posts",
    "big",
    "media",
    "law",
    "control",
    "water",
    "history",
    "pictures",
    "size",
    "art",
    "personal",
    "since",
    "including",
    "guide",
    "shop",
    "directory",
    "board",
    "location",
    "change",
    "white",
    "text",
    "small",
    "rating",
    "rate",
    "government",
    "children",
    "during",
    "return",
    "students",
    "shopping",
    "account",
    "times",
    "sites",
    "level",
    "digital",
    "profile",
    "previous",
    "form",
    "events",
    "love",
    "old",
    "john",
    "main",
    "call",
    "hours",
    "image",
    "department",
    "title",
    "description",
    "non",
    "insurance",
    "another",
    "why",
    "shall",
    "property",
    "class",
    "still",
    "money",
    "quality",
    "every",
    "listing",
    "content",
    "country",
    "private",
    "little",
    "visit",
    "save",
    "tools",
    "low",
    "reply",
    "customer",
    "december",
    "compare",
    "movies",
    "include",
    "college",
    "value",
    "article",
    "york",
    "man",
    "card",
    "jobs",
    "provide",
    "food",
    "source",
    "author",
    "different",
    "press",
    "learn",
    "sale",
    "around",
    "print",
    "course",
    "job",
    "canada",
    "process",
    "teen",
    "room",
    "stock",
    "training",
    "too",
    "credit",
    "point",
    "join",
    "science",
    "men",
    "categories",
    "advanced",
    "west",
    "sales",
    "look",
    "english",
    "left",
    "team",
    "estate",
    "box",
    "conditions",
    "select",
    "windows",
    "photos",
    "gay",
    "thread",
    "week",
    "category",
    "note",
    "live",
    "large",
    "gallery",
    "table",
    "register",
    "however",
    "june",
    "october",
    "november",
    "market",
    "library",
    "really",
    "action",
    "start",
    "series",
    "model",
    "features",
    "air",
    "industry",
    "plan",
    "human",
    "provided",
    "tv",
    "yes",
    "required",
    "second",
    "hot",
    "accessories",
    "cost",
    "movie",
    "forums",
    "march",
    "september",
    "better",
    "say",
    "questions",
    "july",
    "yahoo",
    "going",
    "medical",
    "test",
    "friend",
    "come",
    "server",
    "study",
    "application",
    "cart",
    "staff",
    "articles",
    "san",
    "feedback",
    "again",
    "play",
    "looking",
    "issues",
    "april",
    "never",
    "users",
    "complete",
    "street",
    "topic",
    "comment",
    "financial",
    "things",
    "working",
    "against",
    "standard",
    "tax",
    "person",
    "below",
    "mobile",
    "less",
    "got",
    "blog",
    "party",
    "payment",
    "equipment",
    "login",
    "student",
    "let",
    "programs",
    "offers",
    "legal",
    "above",
    "recent",
    "park",
    "stores",
    "side",
    "act",
    "problem",
    "red",
    "give",
    "memory",
    "performance",
    "social",
    "august",
    "quote",
    "language",
    "story",
    "sell",
    "options",
    "experience",
    "rates",
    "create",
    "key",
    "body",
    "young",
    "america",
    "important",
    "field",
    "few",
    "east",
    "paper",
    "single",
    "activities",
    "club",
    "example",
    "girls",
    "additional",
    "password",
    "latest",
    "something",
    "road",
    "gift",
    "question",
    "changes",
    "night",
    "hard",
    "texas",
    "pay",
    "four",
    "poker",
    "status",
    "browse",
    "issue",
    "range",
    "building",
    "seller",
    "court",
    "february",
    "always",
    "result",
    "audio",
    "light",
    "write",
    "war",
    "offer",
    "blue",
    "groups",
    "easy",
    "given",
    "files",
    "event",
    "release",
    "analysis",
    "request",
    "china",
    "making",
    "picture",
    "needs",
    "possible",
    "might",
    "professional",
    "yet",
    "month",
    "major",
    "star",
    "areas",
    "future",
    "space",
    "committee",
    "hand",
    "sun",
    "cards",
    "problems",
    "london",
    "washington",
    "meeting",
    "become",
    "interest",
    "child",
    "keep",
    "enter",
    "california",
    "share",
    "similar",
    "garden",
    "schools",
    "million",
    "added",
    "reference",
    "companies",
    "listed",
    "baby",
    "learning",
    "energy",
    "run",
    "delivery",
    "net",
    "popular",
    "term",
    "film",
    "stories",
    "put",
    "computers",
    "journal",
    "reports",
    "try",
    "welcome",
    "central",
    "images",
    "president",
    "notice",
    "original",
    "head",
    "radio",
    "until",
    "cell",
    "color",
    "self",
    "council",
    "away",
    "includes",
    "track",
    "australia",
    "discussion",
    "archive",
    "once",
    "others",
    "entertainment",
    "agreement",
    "format",
    "least",
    "society",
    "months",
    "log",
    "safety",
    "friends",
    "sure",
    "trade",
    "edition",
    "cars",
    "messages",
    "marketing",
    "tell",
    "further",
    "updated",
    "association",
    "able",
    "having",
    "provides",
    "david",
    "fun",
    "already",
    "green",
    "studies",
    "close",
    "common",
    "drive",
    "specific",
    "several",
    "gold",
    "living",
    "collection",
    "called",
    "short",
    "arts",
    "lot",
    "ask",
    "display",
    "limited",
    "powered",
    "solutions",
    "means",
    "director",
    "daily",
    "beach",
    "past",
    "natural",
    "whether",
    "due",
    "et",
    "electronics",
    "five",
    "upon",
    "period",
    "planning",
    "database",
    "says",
    "official",
    "weather",
    "mar",
    "land",
    "average",
    "done",
    "technical",
    "window",
    "france",
    "pro",
    "region",
    "island",
    "record",
    "direct",
    "microsoft",
    "conference",
    "environment",
    "records",
    "district",
    "calendar",
    "costs",
    "style",
    "url",
    "front",
    "statement",
    "update",
    "parts",
    "ever",
    "downloads",
    "early",
    "miles",
    "sound",
    "resource",
    "present",
    "applications",
    "either",
    "ago",
    "document",
    "word",
    "works",
    "material",
    "bill",
    "written",
    "talk",
    "federal",
    "hosting",
    "rules",
    "final",
    "adult",
    "tickets",
    "thing",
    "centre",
    "requirements",
    "via",
    "cheap",
    "kids",
    "finance",
    "true",
    "minutes",
    "else",
    "mark",
    "third",
    "rock",
    "gifts",
    "europe",
    "reading",
    "topics",
    "bad",
    "individual",
    "tips",
    "plus",
    "auto",
    "cover",
    "usually",
    "edit",
    "together",
    "videos",
    "percent",
    "fast",
    "function",
    "fact",
    "unit",
    "getting",
    "global",
    "tech",
    "meet",
    "far",
    "economic",
    "player",
    "projects",
    "lyrics",
    "often",
    "subscribe",
    "submit",
    "germany",
    "amount",
    "watch",
    "included",
    "feel",
    "though",
    "bank",
    "risk",
    "thanks",
    "everything",
    "deals",
    "various",
    "words",
    "linux",
    "production",
    "commercial",
    "james",
    "weight",
    "town",
    "heart",
    "advertising",
    "received",
    "choose",
    "treatment",
    "newsletter",
    "archives",
    "points",
    "knowledge",
    "magazine",
    "error",
    "camera",
    "girl",
    "currently",
    "construction",
    "toys",
    "registered",
    "clear",
    "golf",
    "receive",
    "domain",
    "methods",
    "chapter",
    "makes",
    "protection",
    "policies",
    "loan",
    "wide",
    "beauty",
    "manager",
    "india",
    "position",
    "taken",
    "sort",
    "listings",
    "models",
    "michael",
    "known",
    "half",
    "cases",
    "step",
    "engineering",
    "florida",
    "simple",
    "quick",
    "none",
    "wireless",
    "license",
    "paul",
    "friday",
    "lake",
    "whole",
    "annual",
    "published",
    "later",
    "basic",
    "sony",
    "shows",
    "corporate",
    "google",
    "church",
    "method",
    "purchase",
    "customers",
    "active",
    "response",
    "practice",
    "hardware",
    "figure",
    "materials",
    "fire",
    "holiday",
    "chat",
    "enough",
    "designed",
    "along",
    "among",
    "death",
    "writing",
    "speed",
    "html",
    "countries",
    "loss",
    "face",
    "brand",
    "discount",
    "higher",
    "effects",
    "created",
    "remember",
    "standards",
    "oil",
    "bit",
    "yellow",
    "political",
    "increase",
    "advertise",
    "kingdom",
    "base",
    "near",
    "environmental",
    "thought",
    "stuff",
    "french",
    "storage",
    "japan",
    "doing",
    "loans",
    "shoes",
    "entry",
    "stay",
    "nature",
    "orders",
    "availability",
    "africa",
    "summary",
    "turn",
    "mean",
    "growth",
    "notes",
    "agency",
    "king",
    "monday",
    "european",
    "activity",
    "copy",
    "although",
    "drug",
    "pics",
    "western",
    "income",
    "force",
    "cash",
    "employment",
    "overall",
    "bay",
    "river",
    "commission",
    "ad",
    "package",
    "contents",
    "seen",
    "players",
    "engine",
    "port",
    "album",
    "regional",
    "stop",
    "supplies",
    "started",
    "administration",
    "bar",
    "institute",
    "views",
    "plans",
    "double",
    "dog",
    "build",
    "screen",
    "exchange",
    "types",
    "soon",
    "sponsored",
    "lines",
    "electronic",
    "continue",
    "across",
    "benefits",
    "needed",
    "season",
    "apply",
    "someone",
    "held",
    "ny",
    "anything",
    "printer",
    "condition",
    "effective",
    "believe",
    "organization",
    "effect",
    "asked",
    "mind",
    "sunday",
    "selection",
    "casino",
    "lost",
    "tour",
    "menu",
    "volume",
    "cross",
    "anyone",
    "mortgage",
    "hope",
    "silver",
    "corporation",
    "wish",
    "inside",
    "solution",
    "mature",
    "role",
    "rather",
    "weeks",
    "addition",
    "came",
    "supply",
    "nothing",
    "certain",
    "executive",
    "running",
    "lower",
    "necessary",
    "union",
    "jewelry",
    "according",
    "dc",
    "clothing",
    "mon",
    "com",
    "particular",
    "fine",
    "names",
    "robert",
    "homepage",
    "hour",
    "gas",
    "skills",
    "six",
    "bush",
    "islands",
    "advice",
    "career",
    "military",
    "rental",
    "decision",
    "leave",
    "british",
    "teens",
    "pre",
    "huge",
    "sat",
    "woman",
    "facilities",
    "zip",
    "bid",
    "kind",
    "sellers",
    "middle",
    "move",
    "cable",
    "opportunities",
    "taking",
    "values",
    "division",
    "coming",
    "tuesday",
    "object",
    "lesbian",
    "appropriate",
    "machine",
    "logo",
    "length",
    "actually",
    "nice",
    "score",
    "statistics",
    "client",
    "returns",
    "capital",
    "follow",
    "sample",
    "investment",
    "sent",
    "shown",
    "saturday",
    "christmas",
    "england",
    "culture",
    "band",
    "flash",
    "lead",
    "george",
    "choice",
    "went",
    "starting",
    "registration",
    "fri",
    "thursday",
    "courses",
    "consumer",
    "hi",
    "airport",
    "foreign",
    "artist",
    "outside",
    "furniture",
    "levels",
    "channel",
    "letter",
    "mode",
    "phones",
    "ideas",
    "wednesday",
    "structure",
    "fund",
    "summer",
    "allow",
    "degree",
    "contract",
    "button",
    "releases",
    "wed",
    "homes",
    "super",
    "male",
    "matter",
    "custom",
    "virginia",
    "almost",
    "took",
    "located",
    "multiple",
    "asian",
    "distribution",
    "editor",
    "inn",
    "industrial",
    "cause",
    "potential",
    "song",
    "cnet",
    "ltd",
    "los",
    "hp",
    "focus",
    "late",
    "fall",
    "featured",
    "idea",
    "rooms",
    "female",
    "responsible",
    "inc",
    "communications",
    "win",
    "associated",
    "thomas",
    "primary",
    "cancer",
    "numbers",
    "reason",
    "tool",
    "browser",
    "spring",
    "foundation",
    "answer",
    "voice",
    "friendly",
    "schedule",
    "documents",
    "communication",
    "purpose",
    "feature",
    "bed",
    "comes",
    "police",
    "everyone",
    "independent",
    "ip",
    "approach",
    "cameras",
    "brown",
    "physical",
    "operating",
    "hill",
    "maps",
    "medicine",
    "deal",
    "hold",
    "ratings",
    "chicago",
    "forms",
    "glass",
    "happy",
    "tue",
    "smith",
    "wanted",
    "developed",
    "thank",
    "safe",
    "unique",
    "survey",
    "prior",
    "telephone",
    "sport",
    "ready",
    "feed",
    "animal",
    "sources",
    "mexico",
    "population",
    "pa",
    "regular",
    "secure",
    "navigation",
    "operations",
    "therefore",
    "simply",
    "evidence",
    "station",
    "christian",
    "round",
    "paypal",
    "favorite",
    "understand",
    "option",
    "master",
    "valley",
    "recently",
    "probably",
    "thu",
    "rentals",
    "sea",
    "built",
    "publications",
    "blood",
]


def speak_word(word):
    tts = gTTS(text=word, lang="en")
    tts.save("temp.mp3")
    os.system("afplay temp.mp3")  # This works on macOS
    os.remove("temp.mp3")


def run_spelling_test(num_words):
    print("Welcome to the Handwritten Spelling Assessment Program!")
    print(f"You will hear {num_words} words, one at a time.")
    print("Write each word on your paper. You'll have 15 seconds per word.")
    print("After the test, you'll grade your own responses.")
    input("Press Enter when you're ready to begin...")

    test_words = random.sample(words, num_words)
    for i, word in enumerate(test_words, 1):
        print(f"\nWord {i}:")
        speak_word(word)
        time.sleep(2)
        speak_word(word)
        time.sleep(8)  # Time to write on paper

    print("\nTest complete! Please grade your responses now.")
    input("Press Enter when you're ready to input your results...")
    return test_words


def grade_test(test_words):
    correct = 0
    incorrect = []
    for i, word in enumerate(test_words, 1):
        print(f"\nWord {i}: {word}")
        is_correct = input("Did you spell it correctly? (y/n): ").lower().strip()
        if is_correct == "y":
            correct += 1
        else:
            incorrect.append(word)

    return correct, incorrect


def main():
    while True:
        try:
            num_words = int(
                input("How many words would you like in this test? (1-100): ")
            )
            if 1 <= num_words <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    test_words = run_spelling_test(num_words)
    correct, incorrect = grade_test(test_words)

    percentage = (correct / num_words) * 100
    print(f"\nYour score: {correct}/{num_words}")
    print(f"Percentage: {percentage:.2f}%")

    if incorrect:
        print("\nWords spelled incorrectly:")
        for word in incorrect:
            print(word)


if __name__ == "__main__":
    main()
