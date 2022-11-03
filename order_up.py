<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Order Up</title>
    <link rel="stylesheet" href="order_up_styles.css">
</head>
<body class="page-style">
    <header>
    <h1>Pizza Ordering Page</h1>
    <img src="pizza.png" alt="Pizza Slice">
    </header>

    <main>
    <form id="customerInformationEntry">
        <p><label for="txtName"> First and Last Name: </label>
            <input type="text" id="txtName">

        <p><label for="txtPhoneNumber"> Phone Number: </label>    
            <input type="text" id="txtEmail">

        <h2>Size</h2>
        <p><label for="selPizzaSize"> Which size pizza would you like to order? </label>
            <select id="selPizzaSize">
            <option value="small">Small ($12)</option>
            <option value="medium">Medium ($15)</option>
            <option value="large">Large ($18)</option>
            </select>

        <h3>Toppings ($2.25 each)</h3>
        <p><label for="chkMushroomToppingForPizza"> Mushrooms: </label>
            <input type="checkbox" id="chkMushroomToppingForPizza">
        <p><label for="chkPepperoniToppingForPizza"> Pepperoni: </label>
            <input type="checkbox" id="chkPepperoniToppingForPizza">
        <p><label for="chkSausageToppingForPizza"> Sausage: </label>
            <input type="checkbox" id="chkSausageToppingForPizza">

        <h4>Club Member?</h4>
        <p><label for="chkClubMember"> If you are a club member, you will be given an additional 5% off of every order you make with us. <p> Check this box to join: </label>
            <input type="checkbox" id="chkClubMember">

        <h5>Discount Lottery!</h5>
        <p> When you order today, a random discount will be applied to your order! <p> Please note that only one discount attempt can be made per email address per day.

        <p><button type="button" id="btnOrderPizza" onclick="pizzaOrderResults()"> Make My Pizza! </button> </form>

        <div id="output_summary"> </div> <!-- end of output_summary div --> 

        <script>
            function pizzaOrderResults()
            {
                var name;
                var sizeOfPizza;
                var mushroomTopping, pepperoniTopping, sausageTopping, costOfToppings;
                var didUserJoinClub;
                var discount;
                var originalCostOfPizza;
                var cost;
                var clubMemberDiscount;
                var finalPrice;
                var userInClub;
                var allToppings;

                name = document.getElementById('txtName').value;
                sizeOfPizza = document.getElementById('selPizzaSize').value;

                if (sizeOfPizza == "small")
                {
                    cost = 12;
                }
                else if (sizeOfPizza == "medium")
                {
                    cost = 15;
                }
                else if (sizeOfPizza == "large")
                {
                    cost = 18;
                }

                discount = (Math.random())*3+1;
                discount = parseInt(discount)
                didUserJoinClub = document.getElementById('chkClubMember').checked;
                mushroomTopping = document.getElementById('chkMushroomToppingForPizza').checked == true? 1:0;
                pepperoniTopping = document.getElementById('chkPepperoniToppingForPizza').checked == true? 1:0
                sausageTopping = document.getElementById('chkSausageToppingForPizza').checked == true? 1:0;
                costOfToppings = 2.25;
                allToppings = ""

                if (mushroomTopping == 1) 
                {
                    allToppings += "Mushrooms ";
                }
                if (pepperoniTopping == 1) 
                {
                    allToppings += "Pepperoni ";
                }
                if (sausageTopping == 1) 
                {
                    allToppings += "Sausage";
                }
                originalCostOfPizza = cost + (mushroomTopping + pepperoniTopping + sausageTopping) * costOfToppings;
                if (didUserJoinClub)
                {
                    clubMemberDiscount = originalCostOfPizza * .95
                }
                else
                {
                    clubMemberDiscount = originalCostOfPizza
                }

                finalPrice = clubMemberDiscount * (1-discount/10);
                userInClub = didUserJoinClub == true? "Yes":"No";
                finalPrice = finalPrice.toFixed(2);

                document.getElementById('output_summary').innerHTML = "Thank you," + " " + name + " " + "for your order of a" + " " +
                sizeOfPizza + " " + "pizza!" + "<br>The toppings you requested are:" + " " + allToppings + "<p>Join the club?" 
                + " " + userInClub + "<br>Discount? Congratulations, you won a" + " " + discount * 10 + "%" + " " + "discount!" 
                + "<p>The total cost of your pizza is:" + " " + "$" + finalPrice + "." + " " + "See you soon!"


            }
        </script>
    </main>
</p>
</body>
</html>

#CSS included below

.page-style
{
    width: 440px;
    border: 2px solid #000000;
    padding: 5px;
}

img 
{
    width: 60px;
    height: 60px;
}


