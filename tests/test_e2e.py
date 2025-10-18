from playwright.sync_api import sync_playwright, expect
def test_error():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://rahulshettyacademy.com/client")
        # Setting a global timeout
        page.set_default_timeout(30000)

        # Wait for and fill the email
        email_field = page.wait_for_selector("input[placeholder='email@example.com']", timeout=10000)
        email_field.fill("kolarnihar@gmail.com")

        # Wait and fill password
        page.wait_for_selector("#userPassword", timeout=20000)
        page.fill("#userPassword", "NihaK10#")

        # Click login button
        login_button = page.locator('input[name="login"]')
        login_button.wait_for(state='visible', timeout=30000)
        login_button.click(timeout=60000)

        async def add_items_to_cart(page):
    # Adding ZARA COAT 3
            zaracoat = page.locator("div.card-body:has-text('ZARA COAT 3')")
            await zaracoat.wait_for(state='visible', timeout=30000)
            add_to_cart_1 = zaracoat.locator('button[name="Add To Cart"]')
            await add_to_cart_1.wait_for(state='visible', timeout=30000)
            await add_to_cart_1.click(timeout=60000)

    # Adding ADIDAS ORIGINAL
            adidas = page.locator("div.card-body:has-text('ADIDAS ORIGINAL')")
            await adidas.wait_for(state='visible', timeout=30000)
            add_to_cart_2 = adidas.locator('button[name="Add To Cart"]')
            await add_to_cart_2.wait_for(state='visible', timeout=30000)
            await add_to_cart_2.click(timeout=60000)

    # Check cart items count
            await page.locator('button[name="Cart"]').click()
            await expect(page.locator(".media-body")).to_have_count(2)
