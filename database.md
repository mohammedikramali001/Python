#Creating a store database that will support inventory tracking, sales reporting, and event scheduling for authors and performers
 
 > Inventory
 >Sales reports
 > Schedules for author and performer appearances
 
 *new inventory form*:
| name | type |
| --- | ----------- |
| date | Date |
| author | string |
| title | string |
| product type | string |
| Publisher | string |
| UPC (ID) | integer |
| ISBN | integer |
| Reatil Price | Decimal |
| Quantity Recieved | integer |
| **Genre** | string |
 
 
Resources
 
 
- New inventory form: Paper form to collect information on the new titles that the store has received. One of the managers uses this form to update a spreadsheet that tracks store inventory.
- Inventory spreadsheet: A shared spreadsheet that lists all the inventory that the store owns.
- Customer receipt: An example of a sales receipt that customers receive.
- Monthly sales report: Each month, one of the managers manually produces a monthly sales report, which they provide to the store owners and management team.
 
 #### What additional questions might you have based on the inventory spreadsheet?
 * Is the spread sheet updated  automatically updated or manually
 * Does the spread sheet use a barcode system or user entry
 
 *inventory spreadsheat*:
| name | type |
| --- | ----------- |
| UPC (ID) | integer |
| title | string |
| last inventory | integer |
| sales since| Date |
| on hand | integer |

> date
author
title
year published
product type
Publisher
UPC (ID)
ISBN
Reatil Price
Quantity Recieved
**Genre**
 
*inventory spreadsheat*
UPC
title
last inventory
sales since
on hand
 
 #### What additional questions might you have based on the customer receipt?

 > * how many recipts have been backedup
>* how long do you keep the receipts
>* how large is the log of reciepts
*customer receipt*
UPC
QTY
Discount code
net

#### What additional questions might you have based on the monthly sales report?
 
*monthly sales report*
title
retail price
quantity
net after discounts
 
 
 
post a calendar of these upcoming events on the store’s website
 
receive a reminder when ordering products to make sure extra copies of the author’s book or the artist’s CDs are in stock.
 
 *event booking*:
| name | type |
| --- | ----------- |
| event id| string |
| UPC (for books and cds) | integer |
| date | Date |
| on hand| integer |

*event booking*
event id
UPC (for books and cds)
artist name
date
on hand
 
*guest list*
event id
name
e-mail
event date

 
 
 

 
 
 
*customer receipt*:
| name | type |
| --- | ----------- |
| UPC (ID) | integer |
| QTY | string |
| Discount code | integer |
| net| Decimal |
 
 
 
*monthly sales report*:
| name | type |
| --- | ----------- |
| title | string |
| retail price | Decimal |
| quantity | integer |
| net after discounts| Decimal |
 
 
 
* post a calendar of these upcoming events on the store’s website
 
* receive a reminder when ordering products to make sure extra copies of the author’s book or the artist’s CDs are in stock.
 
 

 
 
 
*guest list*:
| name | type |
| --- | ----------- |
| event id | string |
| name | string |
| event date | Date |
| e-mail | string |

|    Date    |        Food Category         |     Food Subcategory      |   Country   | Country Code |  Continent  |      City      | Unit Sales |
|------------|-----------------------------|--------------------------|------------|--------------|-------------|---------------|------------|
| 2021-10-06 |         Beverages            | Carbonated non-alcoholic |  Belgium   |     BEL      |   Europe    |    Brussels    | 1,906,983  |
| 2021-10-13 |           Dairy              |       Low-fat milk        |   Brazil   |     BRA      | South America | Rio de Janeiro |   652,432  |
| 2021-11-10 | Meats, eggs, and nuts       | Nuts and seeds raw       |   Canada   |     CAN      | North America |   Vancouver    |   354,097  |
| 2021-11-24 |           Fruits             |      Fruit juice          |  Germany   |     DEU      |   Europe    |     Berlin     |   132,004  |
| 2021-12-07 | Commercially prepared items |      Packaged nuts        |  Denmark   |     DNK      |   Europe    |  Copenhagen    |   80,125   |
| 2021-12-15 |           Fruits             |   Canned fruit juice      |   France   |     FRA      |   Europe    |     Paris      |  754,945  |
| 2021-12-22 | Commercially prepared items | Not sweet canned (soups, sauces, and more) |  Ireland | IRL | Europe | Dublin | 112,873 |
| 2022-01-07 | Commercially prepared items | Sweet ready-to-eat (bakery items) | United States | USA | North America | Washington D.C. | 90,086 |
| 2022-01-15 | Commercially prepared items | Not sweet packaged, snacks | Uruguay | URY | South America | Montevideo | 140,941 |
| 2022-01-22 | Commercially prepared items | Sweet frozen (ice cream, frozen desserts) | Samoa | WSM | Oceania | Apia | 6,000 |


![Alt Text](https://i.vimeocdn.com/video/1123785282-2ee2f62503c8911a2644c35da4700e9caab570ebb9da5c3e0cbe4025d9127f16-d?f=webp)