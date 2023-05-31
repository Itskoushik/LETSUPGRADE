<?php
function printMultiplicationTable($number) {
    for ($i = 1; $i <= 10; $i++) {
        $result = $number * $i;
        echo $number . " x " . $i . " = " . $result . "<br>";
    }
}

$givenNumber = 5;
echo "Multiplication Table of " . $givenNumber . "<br>";
echo "-----------------------------<br>";
printMultiplicationTable($givenNumber);
?>
