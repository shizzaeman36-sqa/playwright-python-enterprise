from playwright.sync_api import Page, expect

# -------------------------------------------------------------
# SCENARIO 1: NETWORK MOCKING (API Response Change Karna)
# -------------------------------------------------------------
def test_mock_api_response(page: Page):
    # Har us API call ko pakdo jo /api/v1/fruits par ja rahi ho
    def handle_route(route):
        # Fake JSON response bhej rahe hain backend ki bajaye
        route.fulfill(
            status=200,
            content_type="application/json",
            json=[{"name": "Shiza Special Mango", "id": 1}]
        )

    # Route interceptor enable karte hain
    page.route("*/**/api/v1/fruits", handle_route)

    # Page load karte hain jo yeh API call karta hai
    page.goto("https://demo.playwright.dev/api-mocking/")

    # Check karte hain ke UI par real data ki jagah HUMARA FAKE DATA nazar aa raha hai
    expect(page.get_by_text("Shiza Special Mango")).to_be_visible()
    print("API Mocking Test Passed Successfully!")


# -------------------------------------------------------------
# SCENARIO 2: DIRECT API REQUEST (Backend Endpoint Verification)
# -------------------------------------------------------------
def test_direct_api_call(page: Page):
    # Direct HTTP GET request
    response = page.request.get("https://reqres.in/api/users/2")
    
    # Status code verify karte hain
    assert response.status == 200
    
    # JSON body verify karte hain
    json_data = response.json()
    assert json_data["data"]["first_name"] == "Janet"
    print("Direct API Test Passed Successfully!")