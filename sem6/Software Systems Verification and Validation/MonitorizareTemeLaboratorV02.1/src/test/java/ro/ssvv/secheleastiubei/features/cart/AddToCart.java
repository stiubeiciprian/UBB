package ro.ssvv.secheleastiubei.features.cart;

import net.serenitybdd.junit.runners.SerenityParameterizedRunner;
import net.thucydides.core.annotations.Managed;
import net.thucydides.core.annotations.ManagedPages;
import net.thucydides.core.annotations.Steps;
import net.thucydides.core.pages.Pages;
import net.thucydides.junit.annotations.Qualifier;
import net.thucydides.junit.annotations.UseTestDataFrom;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import ro.ssvv.secheleastiubei.steps.serenity.EmagUserSteps;


@RunWith(SerenityParameterizedRunner.class)
@UseTestDataFrom("src/test/resources/EmagTestData.csv")
public class AddToCart {
    @Managed(uniqueSession = true)
    public WebDriver webdriver;

    @ManagedPages(defaultUrl = "https://www.emag.ro/")
    public Pages pages;

    public String query;
    public String product;

    @Qualifier
    public String getQualifier() {
        return query;
    }

    @Steps
    public EmagUserSteps endUser;

    @Test
    public void addToCartTest() {
        endUser.is_the_home_page();
        endUser.add_to_cart(getQuery());

        endUser.should_see_product_in_cart(getProduct());
    }

    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }

    public String getProduct() {
        return product;
    }

    public void setProduct(String product) {
        this.product = product;
    }

}
