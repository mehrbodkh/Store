class Message:
    success_edit_store_address = "آدرس فروشگاه شما با موفقیت تنظیم شد."
    enter_store_address = "*آدرس* فروشگاه خود را وارد کنید:"
    success_edit_store_description = "توضیحات فروشگاه شما با موفقیت تنظیم شد."
    enter_store_description = "*توضیحات* فروشگاه را وارد کنید:"
    success_edit_store_name = "نام فروشگاه شما با موفقیت تنظیم شد."
    not_valid_card_number = "فرمت کارت بانکی اشتباه است!"
    input_error = "ورودی صحیح *نمی باشد!*"
    send_photo = "*عکس* فروشگاه را بارگزاری نمایید:"
    enter_store_card_number = "*شماره کارت بانکی* خود را وارد کنید:"
    enter_store_name = "*نام* فروشگاه را وارد کنید:"
    no_products = "فعلا هیچ محصولی موجود نیست!"
    start_conversation = "سلام!\nبه بازوی مدیریت فروشگاه خود خوش آمدید.\n" \
                         "با استفاده از این بازو می‌توانید اجناس داخل " \
                         "فروشگاه خود را به آدرس @BazovanStore_Bot مدیریت کنید. "
    choose_menu = "برای مدیریت اجناس فروشگاه یکی از گزینه‌های زیر را انتخاب کنید:"
    end_add_conversation = "محصول شما با موفقیت به فروشگاه اضافه شد."

    add_item_name_tutorial = "نام محصول خود را وارد کنید:"
    add_item_price_tutorial = "قیمت محصول خود را به ریال وارد کنید:"
    add_item_photo_tutorial = "تصویر محصول را ارسال کنید:"
    add_item_description_tutorial = "توضیحات محصول خود را وارد کنید:"
    add_item_tag_tutorial = "دسته‌ی محصول خود را انتخاب کنید:\nبرای افزودن دسته‌ی جدید نام *دسته‌ی جدید* را ارسال " \
                            "کنید. "
    add_item_inventory_tutorial = "تعداد باقیمانده‌ی محصول را وارد کنید:"

    remove_item_name_tutorial = "نام محصول مورد نظر را وارد کنید:\n(با وارد کردن بخشی از نام محصول تمام محصولات با " \
                                "نام مشابه نیز نمایش داده خواهند شد.) "
    remove_item_not_found = "محصول مورد نظر در لیست محصولات فروشگاه شما موجود نمی‌باشد."
    remove_item_deleted = "محصول مورد نظر با موفقیت از لیست محصولات حذف شد."

    edit_store_card_tutorial = "شماره کارت فروشگاه خود را وارد کنید:"
    edit_store_card_success = "شماره کارت فروشگاه شما با موفقیت تنظیم شد."
    edit_store_card_fail = "شماره کارت شما باید ۱۶ رقمی باشد."

    help_message = "سلام! به بازو مدیریت فروشگاهتان خوش‌آمدید.\nبا استفاده از این بازو می‌توانید فروشگاه خود به آدرس " \
                   "@BazoveanStore_Bot را مدیریت کنید.\n\n-با انتخاب گزینه‌ی [افزودن محصول](send:افزودن محصول) " \
                   "می‌توانید محصول جدید را به " \
                   "فروشگاه خود اضافه کنید.\n\n-با انتخاب گزینه‌ی [حذف کردن محصول](send:حذف کردن محصول) می‌توانید " \
                   "محصولات موجود در فروشگاه " \
                   "را حذف کنید.\n\n-بااستفاده از گزینه‌ی [نمایش تمام محصولات](send:نمایش تمام محصولات) می‌توانید " \
                   "لیست تمامی محصولات موجود " \
                   "در فروشگاه را ملاحظه کنید.\n\n- با استفاده از گزینه‌ی [تنظیم شماره‌ کارت فروشگاه](send:تنظیم " \
                   "شماره کارت فروشگاه) می‌توانید " \
                   "برای فروشگاه خود شماره کارتی تنظیم کنید یا آن‌را تغییر دهید. توجه داشته باشید که مبلغ خرید‌ها از " \
                   "فروشگاه به این کارت واریز خواهد شد. "

    charge_remaining_times_title = "افزایش تعداد دفعات افزودن"
    charge_remaining_times_description = "افزودن ۲۰ عدد تعداد دفعات باقی‌مانده اضافه کردن محصول"
    payment_done = "تعداد دفعات افزودن محصول با موفقیت شارژ شد."
    product_caption = "نام محصول: {name}" \
                      "\n" \
                      "توضیحات:‌ {description}" \
                      "\n" \
                      "قیمت: {price} ریال"


class Keyboards:
    back_to_main_menu = "بازگشت به منو اصلی"
    back = "بازگشت"
    add_item = "افزودن محصول"
    remove_item = "حذف کردن محصول"
    show_all_items = "نمایش تمام محصولات"
    edit_store_card_number = "تنظیم شماره کارت فروشگاه"
    edit_store_name = "تنظیم نام فروشگاه"
    edit_store_address = "تنظیم آدرس فروشگاه"
    edit_store_description = "تنظیم توضیحات فروشگاه"
    edit_store = "تنظیمات فروشگاه"
    get_orders_list = "لیست سفارش‌ها"
    return_to_main_menu = "/start"


class ConversationStates:
    NAME, PRICE, PHOTO, DESCRIPTION, INVENTORY, TAG, DELETE_PRODUCT_ID, CARD_NUMBER, PAYMENT, ADDRESS = range(10)
