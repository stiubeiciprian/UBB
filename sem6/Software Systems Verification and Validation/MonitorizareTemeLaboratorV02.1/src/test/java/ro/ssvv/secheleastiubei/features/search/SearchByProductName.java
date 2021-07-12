package ro.ssvv.secheleastiubei.features.search;

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
public class SearchByProductName {
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
    public void searchEmagByKeywordTestDDT() {
        endUser.is_the_home_page();
        endUser.search_product(getQuery());

        endUser.should_see_products(getProduct());
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
