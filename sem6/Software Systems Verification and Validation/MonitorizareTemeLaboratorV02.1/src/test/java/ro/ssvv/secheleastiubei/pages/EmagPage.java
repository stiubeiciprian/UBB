package ro.ssvv.secheleastiubei.pages;

import net.thucydides.core.annotations.DefaultUrl;
import org.openqa.selenium.By;
import net.serenitybdd.core.pages.WebElementFacade;

import net.serenitybdd.core.annotations.findby.FindBy;

import net.thucydides.core.pages.PageObject;

@DefaultUrl("https://www.emag.ro/")
public class EmagPage extends PageObject {

    @FindBy(name="query")
    private WebElementFacade searchQuery;

    @FindBy(className="searchbox-submit-button")
    private WebElementFacade searchButton;


    public void enterQueryInSearchBar(String query) {
        searchQuery.type(query);
    }

    public void searchProduct() {
        searchButton.click();
    }
    
    public String getProductName() {
        WebElementFacade resultList = find(By.id("card_grid"));
        return resultList.findElement(By.className("card-item"))
                .findElement(By.className("product-title")).getText();
    }

    public void addToCart() {
        find(By.id("card_grid")).findElement(By.className("card-item"))
                .findElement(By.className("yeahIWantThisProduct"))
                .click();
    }

    public String confirmAddedProduct() {
        WebElementFacade resultList = find(By.className("modal-header"));
        return resultList.findElement(By.tagName("h4")).getText();
    }
}