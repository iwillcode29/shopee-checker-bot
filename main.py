import requests

SHOP_ID = "apple_flagshipstore"  # รหัสร้าน Shopee
SEARCH_KEYWORD = "iphone 17"

# 🔧 ตั้งค่าของ Telegram Bot
BOT_TOKEN = "8438307071:AAEPJsqfj259KcFQpmYd3n0sRxrs6iK2HEM"
CHAT_ID = "1911426257"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_products():
    url = f"https://shopee.co.th/api/v4/search/search_items?by=relevancy&limit=30&match_id={SHOP_ID}&newest=0&order=desc&page_type=shop"
    r = requests.get(url)
    data = r.json()
    for item in data.get("items", []):
        name = item["item_basic"]["name"].lower()
        if SEARCH_KEYWORD in name:
            product_url = f"https://shopee.co.th/product/{SHOP_ID}/{item['item_basic']['itemid']}"
            send_telegram(f"📱 พบ {SEARCH_KEYWORD} ในร้าน!\n{product_url}")
            print("เจอแล้ว:", name)
            return True
    print("ยังไม่เจอสินค้า")
    return False

if __name__ == "__main__":
    check_products()
