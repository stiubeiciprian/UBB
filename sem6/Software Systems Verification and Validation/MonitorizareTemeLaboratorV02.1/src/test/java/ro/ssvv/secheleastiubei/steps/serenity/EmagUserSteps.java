package ro.ssvv.secheleastiubei.steps.serenity;


import net.thucydides.core.annotations.Step;
import ro.ssvv.secheleastiubei.pages.EmagPage;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;


public class EmagUserSteps {

    EmagPage emagPage;

    @Step
    public void should_see_products(String product) {
        assertThat(emagPage.getProductName(), containsString(product));
    }

    @Step
    public void is_the_home_page() {
        emagPage.open();
    }

    @Step
    public void search_product(String query) {
        emagPage.enterQueryInSearchBar(query);
        emagPage.searchProduct();
    }

    @Step
    public void add_to_cart(String query) {
        emagPage.enterQueryInSearchBar(query);
        emagPage.searchProduct();
        emagPage.addToCart();
    }

    @Step
    public void should_see_product_in_cart(String product) {
        assertThat(emagPage.confirmAddedProduct(), notNullValue());
    }


}
