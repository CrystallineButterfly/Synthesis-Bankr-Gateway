// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

import { ComputeBudgetVault } from "src/ComputeBudgetVault.sol";

contract Deploy is Script {
    function run() external returns (ComputeBudgetVault deployed) {
        address admin = vm.envAddress("ADMIN_WALLET_ADDRESS");
        address operator = vm.envAddress("OPERATOR_WALLET_ADDRESS");

        vm.startBroadcast();
        deployed = new ComputeBudgetVault(admin, operator);
        vm.stopBroadcast();

        console2.log("Deployed ComputeBudgetVault at", address(deployed));
    }
}
