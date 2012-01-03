//
//  LibraryManager.m
//  Qcumber
//
//  Created by Chris Cooper on 12-01-01.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "LibraryManager.h"

@interface LibraryManager (Private)



@end

@implementation LibraryManager


static LibraryManager *sharedInstance;

+ (void)initialize
{
    static BOOL initialized = NO;
    if (!initialized) {
        initialized = YES;
        sharedInstance = [[LibraryManager alloc] init];
    }
}

+ (void) loadIfNecessary {
    
}

/*+ (void) loadIfNecessary {
    
    
    
    
    
    
    
    NSDictionary* jsonDict = [sharedInstance  
    
    NSError* error;
    NSDictionary* json = [NSJSONSerialization JSONObjectWithData:responseData options:kNilOptions error:&error];
    
}

- (NSDictionary *) dictionaryFrom
*/
@end
